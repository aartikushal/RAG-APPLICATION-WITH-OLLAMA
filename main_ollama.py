from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

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
        "options": {
            "num_predict": request.max_tokens
        },
        "stream": False
    }

    response = requests.post(OLLAMA_API_URL, json=payload)

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    story_text = data.get("response", "")

    return {"story": story_text}
