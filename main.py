from uvicorn import run
from fastapi import FastAPI
from src.routes import tender_barrier_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Health check endpoint
@app.get("/")
def read_root():
    return {
        "message": "Procurement Barrier Analysis API",
        "status": "running",
        "endpoints": {
            "POST /analyze_tender": "Analyze tender document for barriers"
        }
    }

app.include_router(router=tender_barrier_router)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
