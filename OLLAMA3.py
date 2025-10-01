from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Enable CORS if frontend calls this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen3:4b"

class StoryRequest(BaseModel):
    prompt: str
    max_tokens: int = 500

@app.post("/generate-story")
def generate_story(request: StoryRequest):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": f"Write a creative story based on: {request.prompt}",
        "options": {"num_predict": request.max_tokens},
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Ollama API request failed: {str(e)}")

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    try:
        data = response.json()
        story_text = data.get("response", "")
    except Exception:
        raise HTTPException(status_code=500, detail="Invalid JSON response from Ollama")

    return {"story": story_text}
