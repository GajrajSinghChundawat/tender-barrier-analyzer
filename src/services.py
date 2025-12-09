import re
import spacy
from loguru import logger
from fastapi import HTTPException
from spacy.matcher import PhraseMatcher
from src.requests import TenderAnalysisResponse
from src.data.barrier_phrases import BARRIER_PHRASES

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize PhraseMatcher for advanced pattern matching
matcher = PhraseMatcher(nlp.vocab)


async def analyze_tender_service(payload):
    try:
        text = payload.tender_text

        if not text:
            raise HTTPException(status_code=400, detail="tender_text cannot be empty")
        
        total_score = 0
        flagged_phrases = []

        for level in ["high", "medium", "low"]:
            for phrase in BARRIER_PHRASES[level]:
                matches = re.findall(phrase["pattern"], text, flags=re.IGNORECASE)
                for match in matches:
                    flagged_phrases.append(match)
                    total_score += phrase["points"]

        # Cap score at 100
        if total_score > 100:
            total_score = 100

        # Recommendation
        if total_score <= 25:
            recommendation = "Low barrier risk - SME-friendly"
        elif total_score <= 50:
            recommendation = "Medium barrier risk - review requirements for proportionality"
        elif total_score <= 75:
            recommendation = "High barrier risk - recommend review"
        else:
            recommendation = "Very high barrier risk - likely excludes majority of SMEs"

        return TenderAnalysisResponse(
            barrier_score=total_score,
            flagged_phrases=flagged_phrases,
            recommendation=recommendation
        )

    except Exception as e:
        logger.error(f"Tender Analyze Error: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"Tender Analyze Error: {e}"
        )
    
async def analyze_tender_spacy_service(payload):
    try:
        text = payload.tender_text

        if not text:
            raise HTTPException(status_code=400, detail="Tender text cannot be empty")

        total_score = 0
        flagged_phrases = []

        # Process the text using spaCy
        doc = nlp(text)

        # Loop through high, medium, low barrier categories
        for _, patterns in BARRIER_PHRASES.items():
            for pattern_data in patterns:
                # Convert pattern into a list of tokens (spaCy Doc)
                pattern = [nlp.make_doc(pattern_data["pattern"])]  # Create a spaCy Doc from the string

                # Register the pattern with the matcher
                matcher.add(pattern_data["category"], pattern)

                # Apply the matcher to the document
                matches = matcher(doc)

                for _, start, end in matches:
                    matched_phrase = doc[start:end].text
                    flagged_phrases.append(matched_phrase)
                    total_score += pattern_data["points"]

                    # Handle thresholds for numerical values (if applicable)
                    if 'min_amount' in pattern_data:
                        matched_value_str = matched_phrase.split()[-2].strip("£").replace(",", "")
                        logger.debug(f"Matched Phrase: {matched_phrase}, Extracted Value: {matched_value_str}")
                        
                        # Check if the extracted value is numeric
                        if matched_value_str.isdigit():
                            matched_value = int(matched_value_str)
                            if matched_value < pattern_data['min_amount']:
                                total_score -= pattern_data['points']  # Remove points if threshold not met
                        else:
                            logger.warning(f"Invalid number format: {matched_value_str}")
                            matched_value = 0  # Default value in case of invalid format

        # Cap total score at 100
        if total_score > 100:
            total_score = 100

        # Generate recommendation based on the score
        if total_score <= 25:
            recommendation = "Low barrier risk - SME-friendly"
        elif total_score <= 50:
            recommendation = "Medium barrier risk - review requirements for proportionality"
        elif total_score <= 75:
            recommendation = "High barrier risk - recommend review"
        else:
            recommendation = "Very high barrier risk - likely excludes majority of SMEs"

        return TenderAnalysisResponse(
            barrier_score=total_score,
            flagged_phrases=flagged_phrases,
            recommendation=recommendation
        )

    except Exception as e:
        logger.error(f"Tender Analyze Spacy Error: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"Tender Analyze Spacy Error: {e}"
        )
