# Tender Barrier Analyzer API

## Project Description

The **Tender Barrier Analyzer** API provides an automated solution to analyze tender documents and identify potential barriers for Small and Medium Enterprises (SMEs). It uses Natural Language Processing (NLP) techniques to assess the tender text, flag potential barriers, and generate recommendations for making the tender more SME-friendly.

This API offers two endpoints:
1. **Normal Tender Analysis** (`/analyze_tender`) – Simple analysis based on predefined patterns.
2. **SpaCy-based Tender Analysis** (`/analyze_tender_spacy`) – Advanced analysis using spaCy's NLP capabilities for better accuracy and detailed analysis.

## Features

- **Barrier Detection**: Identifies phrases that might pose a barrier for SMEs, such as excessive financial requirements, certifications, or high penalties.
- **Scoring System**: Provides a "barrier score" that quantifies the potential risks posed by the tender.
- **Recommendations**: Generates a recommendation to help businesses assess the level of risk and whether the tender is SME-friendly.

## API Endpoints

### 1. `/api/v1/analyze_tender` (Normal Analysis)
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "tender_text": "The supplier must demonstrate a minimum of 10 years uninterrupted trading history."
    }
    ```
- **Response**:
    ```json
    {
      "barrier_score": 45,
      "flagged_phrases": ["10 years uninterrupted trading history"],
      "recommendation": "Medium barrier risk - review requirements for proportionality"
    }
    ```
  
### 2. `/api/v1/analyze_tender_spacy` (SpaCy-based Analysis)
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "tender_text": "The supplier must demonstrate a minimum of 10 years uninterrupted trading history."
    }
    ```
- **Response**:
    ```json
    {
      "barrier_score": 45,
      "flagged_phrases": ["10 years uninterrupted trading history"],
      "recommendation": "Medium barrier risk - review requirements for proportionality"
    }
    ```

## Project Structure
```
├── tests/
│   ├── __init__.py
│   ├── test_analyze_tender.py.py
│   └── test_analyze_tender_spacy.py
├── src/
│   ├── data/
│   │   ├── barrier_phrases.py
│   │   └── sample_tender_documents.py
│   ├── requests.py
│   ├── routes.py
│   └── services.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Setup & Installation

### Prerequisites
1. **Python 3.8+** (Recommended: Python 3.12)
2. **pip** (Package Installer for Python)

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/GajrajSinghChundawat/tender-barrier-analyzer.git
    cd tender-barrier-analyzer
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    # For Windows
    venv\Scripts\activate
    # For Mac/Linux
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download spaCy model** (for SpaCy-based analysis):
    ```bash
    python -m spacy download en_core_web_sm
    ```

5. **Run the FastAPI app**:
    ```bash
    uvicorn main:app --reload --port 8000
    ```

    This will start the server at `http://localhost:8000`.

## Testing

### Running Tests
This project includes tests for both the normal and SpaCy-based tender analysis endpoints. You can run the tests using `pytest`:

1. **Install test dependencies**:
    ```bash
    pip install pytest pytest-asyncio httpx
    ```

2. **Run tests**:
    ```bash
    pytest tests/
    ```

Tests will run for each tender document in the sample data and verify the responses from the API.

### Test File Structure
- `tests/test_analyze_tender.py`: Tests for the normal `analyze_tender` endpoint.
- `tests/test_analyze_tender_spacy.py`: Tests for the `analyze_tender_spacy` endpoint using spaCy.

### Example Test Output
```bash
$ pytest tests/test_analyze_tender.py
=============================== test session starts =====================================
platform win32 -- Python 3.12.0, pytest-9.0.2, pluggy-1.6.0
collected 30 item

tests/test_analyze_tender.py                                       [50%]
tests\test_analyze_tender_spacy.py                                 [100%]
=============================== 30 passed in 1.02 seconds ===============================
