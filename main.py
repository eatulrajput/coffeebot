import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Environment variable GEMINI_API_KEY is missing. Set it in your environment or .env file.")

# Configure Generative AI client
genai.configure(api_key=API_KEY)

# Define generation config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

app = FastAPI(title="Coffee Chatbot API")


app.mount("/static", StaticFiles(directory="static"), name="static")


# Allow CORS from all origins (customize for your frontend domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Gemini model and chat session on startup
try:
    model = genai.GenerativeModel("gemini-1.5-flash", generation_config=generation_config)
except Exception as e:
    raise RuntimeError(f"Failed to initialize Gemini model: {e}")

# We will create a new chat session per request for statelessness, or
# optionally, maintain sessions with IDs if needed.
# For simplicity, here we create a session per request.

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/")
def get_index():
    return FileResponse("static/index.html")


@app.post("/chat", response_model=ChatResponse)
async def chat_with_coffee_bot(request: ChatRequest):
    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(request.message)
        return ChatResponse(reply=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {e}")
