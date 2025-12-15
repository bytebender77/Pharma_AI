from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class SearchRequest(BaseModel):
    query: str
    filters: Optional[Dict[str, Any]] = None

class TrialData(BaseModel):
    nct: str
    title: str
    phase: str
    status: str
    sponsor: str
    enrollment: int
    startDate: str
    completionDate: str
    primaryEndpoint: str
    results: bool

class PatentData(BaseModel):
    patentId: str
    title: str
    assignee: str
    filingDate: str
    grantDate: str
    expiryDate: str
    claims: List[str]
    ftoFlag: str
    source: str

class EximData(BaseModel):
    exportVolume: int
    importVolume: int
    dependencyRisk: str
    trend: str

class MarketData(BaseModel):
    therapy: str
    country: str
    marketSize: int
    yearly: List[Dict[str, Any]]
    cagr: float
    competitors: List[Dict[str, Any]]

class WebEvidence(BaseModel):
    source: str
    type: str
    summary: str
    link: str

class Recommendation(BaseModel):
    path: str
    timeline: str
    nextSteps: List[str]
    commercialPotential: str

class Summary(BaseModel):
    thesis: str
    confidence: str
    riskFlags: List[str]

class AnalysisResult(BaseModel):
    summary: Summary
    trials: List[TrialData]
    market: MarketData
    exim: Optional[EximData] = None
    patents: List[PatentData]
    webEvidence: List[WebEvidence]
    recommendation: Recommendation

class ChatResponse(BaseModel):
    analysis: AnalysisResult
    pdf_url: str
    message: str
