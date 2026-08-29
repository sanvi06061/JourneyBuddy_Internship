from fastapi import FastAPI
import os

app = FastAPI(title="JourneyBuddy Docker Demo")


@app.get("/")
def root():
    return {
        "message": "JourneyBuddy Docker container is running",
        "environment": os.getenv("APP_ENV", "development")
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
