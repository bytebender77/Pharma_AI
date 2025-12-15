# How to Run the Agentic AI Pharma Platform

## Prerequisites
- Python 3.10+
- Node.js (for frontend, optional if using pre-built)

## Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server**
   Use the provided startup script:
   ```bash
   python run.py
   ```
   
   OR run directly with uvicorn:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Access the Application**
   - **Frontend Dashboard**: Open `http://localhost:8000`
   - **API Docs (Swagger)**: Open `http://localhost:8000/docs`

4. **Test the Chat Endpoint**
   You can test via Swagger UI or curl:
   ```bash
   curl -X POST "http://localhost:8000/chat" \
        -H "Content-Type: application/json" \
        -d '{"query": "Analyze pediatric metformin opportunities"}'
   ```
