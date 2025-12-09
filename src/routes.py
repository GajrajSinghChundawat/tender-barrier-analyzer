from fastapi import APIRouter
from src.requests import TenderAnalysisRequest, TenderAnalysisResponse
from src.services import analyze_tender_service, analyze_tender_spacy_service

tender_barrier_router = APIRouter(prefix="/api/v1", tags=["Tender Barrier API"])


@tender_barrier_router.post("/analyze_tender", response_model=TenderAnalysisResponse)
async def analyze_tender(payload: TenderAnalysisRequest):
    """
    Analyze a tender document for SME barriers.
    
    Args:
        request: TenderAnalysisRequest containing the tender text
        
    Returns:
        TenderAnalysisResponse with barrier score, flagged phrases, and recommendation
    """
    return await analyze_tender_service(payload)


@tender_barrier_router.post("/analyze_tender_spacy", response_model=TenderAnalysisResponse)
async def analyze_tender_spacy(payload: TenderAnalysisRequest):
    """
    Analyze a tender document for SME barriers using Spacy.
    
    Args:
        request: TenderAnalysisRequest containing the tender text
        
    Returns:
        TenderAnalysisResponse with barrier score, flagged phrases, and recommendation
    """
    return await analyze_tender_spacy_service(payload)
