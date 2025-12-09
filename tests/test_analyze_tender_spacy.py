import pytest
import httpx
from src.data.sample_tender_documents import SAMPLE_TEST_DATA


@pytest.mark.asyncio
@pytest.mark.parametrize("tender", SAMPLE_TEST_DATA)
async def test_analyze_tender_spacy(tender):
    # Use httpx.AsyncClient for async requests
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        # Send POST request to the analyze_tender_spacy endpoint
        response = await client.post("/api/v1/analyze_tender_spacy", json={"tender_text": tender["text"]})
    
    # Assert the response status code
    assert response.status_code == 200
    
    # Parse the response JSON
    result = response.json()

    # Assert the response has the correct structure
    assert "barrier_score" in result
    assert "flagged_phrases" in result
    assert "recommendation" in result
    
    # Optional: You can add further assertions to check if the barrier score and recommendations meet expectations
    assert isinstance(result["barrier_score"], int)  # Ensure the barrier score is an integer
    assert isinstance(result["flagged_phrases"], list)  # Ensure flagged phrases are in a list
    assert isinstance(result["recommendation"], str)  # Ensure the recommendation is a string
