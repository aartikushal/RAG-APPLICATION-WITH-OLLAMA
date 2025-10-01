📖 FastAPI Story Generator with Ollama

This project provides a simple FastAPI service that connects to an Ollama LLM model (e.g., qwen3:4b) to generate creative stories based on user prompts.

🚀 Features

REST API built with FastAPI

Generates creative stories from user-provided prompts

Connects to Ollama local API (http://127.0.0.1:8000/docs)

Configurable token limit (max_tokens)

CORS support for frontend integration

📂 Project Structure
.
├── main.py        # FastAPI application
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/fastapi-ollama-storygen.git
cd fastapi-ollama-storygen


Create a virtual environment and install dependencies

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Install Ollama
Download & install Ollama
 for your OS.
Then pull the required model (e.g., qwen3:4b):

ollama pull qwen3:4b

▶️ Running the App

Start Ollama server in the background:

ollama serve


Run the FastAPI app:

uvicorn main:app --reload --host 0.0.0.0 --port 8000

📡 API Usage
Endpoint

POST /generate-story

Request Body
{
  "prompt": "A brave knight explores an ancient cave",
  "max_tokens": 300
}

Example cURL
curl -X POST "http://127.0.0.1:8000/generate-story" \
     -H "Content-Type: application/json" \
     -d '{"prompt":"A mysterious forest with glowing trees","max_tokens":200}'

Response
{
  "story": "Once upon a time, in a forest that glowed with magic..."
}

🛠️ Requirements

Python 3.9+

FastAPI

Requests

Uvicorn

Ollama installed locally

Install requirements:

pip install fastapi uvicorn requests

🌟 Future Improvements

Add async support with httpx

Support for streaming responses

Frontend integration with React/Vue
