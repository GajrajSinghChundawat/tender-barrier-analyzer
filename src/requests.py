from typing import List
from pydantic import BaseModel


class TenderAnalysisRequest(BaseModel):
    tender_text: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "tender_text": "The supplier must demonstrate a minimum of 10 years uninterrupted trading history."
            }
        }

class TenderAnalysisResponse(BaseModel):
    barrier_score: int
    flagged_phrases: List[str]
    recommendation: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "barrier_score": 45,
                "flagged_phrases": ["10 years uninterrupted trading history"],
                "recommendation": "Medium barrier risk - review requirements for proportionality"
            }
        }