import os
from dotenv import load_dotenv
from app.agents.master import generate_ai_summary
import json

# Load environment variables
load_dotenv()

def test_openai_connection():
    print("--- Verifying OpenAI Connection ---")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY is NOT set in the environment.")
        print("Please make sure you have added your key to the .env file.")
        return

    print(f"✅ OPENAI_API_KEY found: {api_key[:3]}...{api_key[-4:]}")
    
    # Create dummy context
    context = {
        "market": {"size": "10B", "growth": "5%"},
        "trials": [{"id": "NCT123", "status": "Recruiting"}],
        "patents": [],
        "exim": {},
        "web": []
    }
    
    print("\nAttempting to generate summary using OpenAI API...")
    summary = generate_ai_summary("Test Query", context)
    
    if summary:
        print("\n✅ SUCCESS! OpenAI API returned a summary:")
        print(f"Thesis: {summary.thesis}")
        print(f"Confidence: {summary.confidence}")
        print(f"Risks: {summary.riskFlags}")
    else:
        print("\n❌ FAILURE. OpenAI API call failed. Check the logs above for details.")

if __name__ == "__main__":
    test_openai_connection()
