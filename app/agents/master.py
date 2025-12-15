from app.agents.base import Agent
from app.agents.workers import (
    IQVIAInsightsAgent, 
    EXIMTrendsAgent, 
    PatentLandscapeAgent, 
    ClinicalTrialsAgent, 
    InternalKnowledgeAgent, 
    WebIntelligenceAgent,
    ReportGeneratorAgent
)
from app.models import AnalysisResult, Summary, Recommendation, EximData
from app.services.mock_data import get_scenario, SCENARIOS
from typing import List, Dict, Any
import openai
import os
import json

def generate_ai_summary(query: str, context: Dict[str, Any]) -> Summary:
    """
    Generates a dynamic summary using OpenAI's API based on the aggregated data.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[Master Agent] OPENAI_API_KEY not found. Using mock summary.")
        return None

    client = openai.OpenAI(api_key=api_key)
    
    # Construct a rich prompt with the context
    prompt = f"""
    You are a Pharmaceutical Strategy Expert. 
    Analyze the following data for the query: "{query}"
    
    Data Context:
    {json.dumps(context, indent=2, default=str)}
    
    Output a JSON object with the following fields:
    - thesis: A concise executive summary (2-3 sentences) synthesizing the market opportunity, clinical status, and risks.
    - confidence: "High", "Medium", or "Low" based on data availability.
    - riskFlags: A list of 3-4 key risks (e.g., patent expiry, regulatory hurdles, competitive density).
    
    Return ONLY valid JSON.
    """

    try:
        print("[Master Agent] Calling OpenAI for dynamic summary...")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that outputs JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        
        return Summary(
            thesis=data.get("thesis", "Analysis complete."),
            confidence=data.get("confidence", "Medium"),
            riskFlags=data.get("riskFlags", [])
        )
    except Exception as e:
        print(f"[Master Agent] OpenAI API Error: {e}")
        return None


class MasterAgent(Agent):
    def __init__(self):
        super().__init__(name="Master Agent", role="Orchestrator of Pharma Strategy Analysis")
        # Initialize all worker agents
        self.iqvia_agent = IQVIAInsightsAgent()
        self.exim_agent = EXIMTrendsAgent()
        self.patent_agent = PatentLandscapeAgent()
        self.trials_agent = ClinicalTrialsAgent()
        self.internal_agent = InternalKnowledgeAgent()
        self.web_agent = WebIntelligenceAgent()
        self.report_agent = ReportGeneratorAgent()

    def decompose_query(self, query: str) -> Dict[str, str]:
        """
        Decomposes the user query into structured components.
        In a real system, this would use an LLM. Here we use rule-based parsing.
        """
        print(f"[{self.name}] Decomposing query: '{query}'")
        
        # Default decomposition
        decomposition = {
            "therapy_area": "General",
            "indication": "Unknown",
            "geography": "Global",
            "strategic_intent": "General Research"
        }
        
        # Simple keyword matching for demo purposes
        query_lower = query.lower()
        
        if "pediatric" in query_lower:
            decomposition["therapy_area"] = "Pediatrics"
        if "metformin" in query_lower:
            decomposition["indication"] = "Metabolic Disease" # inferred context
        if "india" in query_lower:
            decomposition["geography"] = "India"
        
        if "repurposing" in query_lower:
            decomposition["strategic_intent"] = "Repurposing"
        elif "market" in query_lower:
            decomposition["strategic_intent"] = "Market Entry"
        elif "patent" in query_lower:
            decomposition["strategic_intent"] = "IP Analysis"
            
        print(f"[{self.name}] Decomposition Result: {decomposition}")
        return decomposition

    def select_agents(self, intent: str) -> List[Agent]:
        """
        Decides which agents to invoke based on strategic intent.
        """
        print(f"[{self.name}] Selecting agents for intent: '{intent}'")
        
        # Core agents that almost always run
        selected_agents = [
            self.internal_agent,
            self.web_agent
        ]
        
        if intent == "Repurposing":
            selected_agents.extend([
                self.trials_agent,
                self.patent_agent,
                self.iqvia_agent
            ])
        elif intent == "Market Entry":
            selected_agents.extend([
                self.iqvia_agent,
                self.exim_agent,
                self.patent_agent
            ])
        elif intent == "IP Analysis":
            selected_agents.extend([
                self.patent_agent,
                self.trials_agent
            ])
        else:
            # Default: Run all relevant research agents
            selected_agents.extend([
                self.iqvia_agent,
                self.exim_agent,
                self.patent_agent,
                self.trials_agent
            ])
            
        # Remove duplicates if any
        return list(set(selected_agents))

    def execute(self, query: str) -> AnalysisResult:
        """
        Orchestrates the analysis process step-by-step.
        """
        print(f"\n=== [{self.name}] Received Query: {query} ===")
        
        # Step 1: Decompose Query
        decomposition = self.decompose_query(query)
        
        # Step 2: Select Agents
        active_agents = self.select_agents(decomposition["strategic_intent"])
        print(f"[{self.name}] Activated {len(active_agents)} agents: {[a.name for a in active_agents]}")
        
        # Step 3: Execute Agents (Sequential for simplicity/clarity in logs)
        results = {}
        
        # Initialize default empty results to avoid validation errors if an agent isn't selected
        # In a real dynamic system, the result model would be more flexible.
        # Here we ensure we populate the AnalysisResult correctly.
        
        # Pre-fetch default data to ensure we have a valid return object even if agents are skipped
        # (This is a hackathon safety measure)
        trial_data = []
        market_data = self.iqvia_agent.execute(query) # Default to always fetch market for structure
        exim_data = None
        patent_data = []
        web_evidence = []
        
        for agent in active_agents:
            print(f"[{self.name}] >>> Invoking {agent.name}...")
            data = agent.execute(query)
            
            # Store results based on agent type
            if isinstance(agent, ClinicalTrialsAgent):
                trial_data = data
                print(f"[{self.name}] <<< {agent.name} returned {len(data)} trials.")
            elif isinstance(agent, IQVIAInsightsAgent):
                market_data = data
                print(f"[{self.name}] <<< {agent.name} returned market data for {data.country}.")
            elif isinstance(agent, EXIMTrendsAgent):
                exim_data = data
                print(f"[{self.name}] <<< {agent.name} returned trade volume: {data.exportVolume}.")
            elif isinstance(agent, PatentLandscapeAgent):
                patent_data = data
                print(f"[{self.name}] <<< {agent.name} returned {len(data)} patents.")
            elif isinstance(agent, WebIntelligenceAgent):
                web_evidence = data
                print(f"[{self.name}] <<< {agent.name} returned {len(data)} web items.")
            elif isinstance(agent, InternalKnowledgeAgent):
                # Internal docs are not strictly part of the AnalysisResult model in the prompt's initial JSON
                # but we can log them or append to web evidence for now if needed.
                # For this specific schema, we'll just log them.
                print(f"[{self.name}] <<< {agent.name} returned {len(data)} internal docs.")
        
        # Step 4: Synthesize Results
        print(f"[{self.name}] Step 4: Synthesizing final response...")
        
        # Get scenario-specific summary and recommendation (Fallback)
        scenario = get_scenario(query)
        scenario_data = SCENARIOS[scenario]
        
        # Attempt Dynamic AI Summary
        context_data = {
            "market": market_data.dict() if market_data else {},
            "trials": [t.dict() for t in trial_data],
            "patents": [p.dict() for p in patent_data],
            "exim": exim_data.dict() if exim_data else {},
            "web": [w.dict() for w in web_evidence]
        }
        
        ai_summary = generate_ai_summary(query, context_data)
        final_summary = ai_summary if ai_summary else scenario_data["summary"]

        result = AnalysisResult(
            summary=final_summary,
            trials=trial_data,
            market=market_data,
            exim=exim_data,
            patents=patent_data,
            webEvidence=web_evidence,
            recommendation=scenario_data["recommendation"]
        )
        
        print(f"[{self.name}] Analysis complete. Aggregation finished.")
        return result
