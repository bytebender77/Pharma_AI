from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models import SearchRequest, AnalysisResult, ChatResponse
from app.agents.master import MasterAgent
from app.services.pdf_generator import generate_pdf_report
from dotenv import load_dotenv
import os
import uuid

# Load environment variables
load_dotenv()

app = FastAPI(title="Pharma Strategy Agent API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Master Agent
master_agent = MasterAgent()

# API Endpoints

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: SearchRequest):
    """
    Main entry point for the Agentic AI.
    1. Receives query
    2. Master Agent orchestrates analysis
    3. Generates PDF report
    4. Returns structured JSON + PDF link
    """
    try:
        print(f"Received chat query: {request.query}")
        
        # 1. Run Master Agent
        result = master_agent.execute(request.query)
        
        # 2. Generate PDF
        # Create a unique filename for this report
        filename = f"report_{uuid.uuid4().hex[:8]}.pdf"
        pdf_path = generate_pdf_report(result, filename=filename)
        
        # 3. Construct URL (assuming local execution)
        # In production, this would be a cloud storage URL
        pdf_url = f"/static/{filename}"
        
        return ChatResponse(
            analysis=result,
            pdf_url=pdf_url,
            message="Analysis complete. Report generated."
        )

    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Keep original endpoints for backward compatibility or specific testing
@app.post("/api/analyze", response_model=AnalysisResult)
async def analyze(request: SearchRequest):
    try:
        result = master_agent.execute(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/report")
async def generate_report(request: SearchRequest):
    try:
        result = master_agent.execute(request.query)
        pdf_path = generate_pdf_report(result)
        return FileResponse(pdf_path, media_type='application/pdf', filename="report.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve Static Files (Reports and Frontend)
# Ensure static directory exists
os.makedirs("app/static", exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve Frontend (if built)
if os.path.exists("frontend/dist"):
    app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="frontend")

@app.get("/")
async def read_root():
    if os.path.exists("frontend/dist/index.html"):
        return FileResponse("frontend/dist/index.html")
    return {"message": "Backend is running. Frontend not found in frontend/dist."}
