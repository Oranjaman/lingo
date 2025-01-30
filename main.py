from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from typing import Optional

app = FastAPI()

class MessageRequest(BaseModel):
    original_message: str
    tone: str
    recipient: Optional[str] = None

class MessageResponse(BaseModel):
    enhanced_message: str

@app.get("/")
def read_root():
    return {"status": "API is running"}

@app.post("/generate")
async def generate_message(request: MessageRequest):
    try:
        # Here you'll add the actual message generation logic
        # For now, just returning a test response
        enhanced = f"Enhanced {request.tone} message for: {request.original_message}"
        return MessageResponse(enhanced_message=enhanced)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
