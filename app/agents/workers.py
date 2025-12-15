from app.agents.base import Agent
from app.services.mock_data import (
    get_clinical_trials, 
    get_uspto_data, 
    get_iqvia_data, 
    get_web_intelligence, 
    get_exim_data
)
from app.services.pdf_generator import generate_pdf_report
from app.models import AnalysisResult

# ==========================================
# 1. IQVIA Insights Agent
# ==========================================
class IQVIAInsightsAgent(Agent):
    def __init__(self):
        super().__init__(name="IQVIA Insights Agent", role="Analyze market size, CAGR, and competition")

    def execute(self, query: str):
        print(f"[{self.name}] Fetching market intelligence for: {query}")
        return get_iqvia_data(query)

# ==========================================
# 2. EXIM Trends Agent
# ==========================================
class EXIMTrendsAgent(Agent):
    def __init__(self):
        super().__init__(name="EXIM Trends Agent", role="Analyze export/import trends and supply chain risk")

    def execute(self, query: str):
        print(f"[{self.name}] Analyzing trade volumes for: {query}")
        return get_exim_data(query)

# ==========================================
# 3. Patent Landscape Agent
# ==========================================
class PatentLandscapeAgent(Agent):
    def __init__(self):
        super().__init__(name="Patent Landscape Agent", role="Assess patent count, expiry, and FTO risk")

    def execute(self, query: str):
        print(f"[{self.name}] Searching patent databases for: {query}")
        return get_uspto_data(query)

# ==========================================
# 4. Clinical Trials Agent
# ==========================================
class ClinicalTrialsAgent(Agent):
    def __init__(self):
        super().__init__(name="Clinical Trials Agent", role="Identify active trials, phases, and sponsors")

    def execute(self, query: str):
        print(f"[{self.name}] Querying clinical registries for: {query}")
        return get_clinical_trials(query)

# ==========================================
# 5. Internal Knowledge Agent
# ==========================================
class InternalKnowledgeAgent(Agent):
    def __init__(self):
        super().__init__(name="Internal Knowledge Agent", role="Retrieve insights from internal PDFs and documents")

    def execute(self, query: str):
        print(f"[{self.name}] Searching internal knowledge base for: {query}")
        # Mocking internal doc retrieval
        return [
            {"doc_id": "INT-2024-001", "title": "Internal Strategy Memo: Metformin Repurposing", "snippet": "Preliminary internal review suggests high feasibility..."},
            {"doc_id": "INT-2023-089", "title": "Lab Notebook: Formulation Stability", "snippet": "Stable at room temperature for 24 months..."}
        ]

# ==========================================
# 6. Web Intelligence Agent
# ==========================================
class WebIntelligenceAgent(Agent):
    def __init__(self):
        super().__init__(name="Web Intelligence Agent", role="Scrape guidelines and news for real-world context")

    def execute(self, query: str):
        print(f"[{self.name}] Scanning web sources for: {query}")
        return get_web_intelligence(query)

# ==========================================
# 7. Report Generator Agent
# ==========================================
class ReportGeneratorAgent(Agent):
    def __init__(self):
        super().__init__(name="Report Generator Agent", role="Compile analysis into a PDF report")

    def execute(self, data: AnalysisResult):
        print(f"[{self.name}] Generating PDF report...")
        # This agent takes the full AnalysisResult object, not just a query string
        return generate_pdf_report(data)
