import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure API key is set
if "GEMINI_API_KEY" not in os.environ:
    st.error("Environment variable GEMINI_API_KEY is missing. Set it in your environment or .env file.")
    st.stop()

# Configure Generative AI client
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Define generation config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create Generative AI model
try:
    model = genai.GenerativeModel("gemini-1.5-flash", generation_config=generation_config)
    chat_session = model.start_chat(history=[])
except Exception as e:
    st.error(f"Failed to initialize the Coffee Chatbot AI: {e}")
    st.stop()

# Streamlit App Configuration
st.set_page_config(page_title="Coffee Chatbot ☕", page_icon="☕", layout="centered")

# Custom CSS for Coffee Theme
st.markdown(
    """
    <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700&display=swap');

        body {
            font-family: 'Merriweather', serif;
            background-color: #f3e5ab;
        }

        .main {
            background: #fffaf0;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }

        h1 {
            color: #6F4E37;
            font-weight: 700;
            text-align: center;
        }

        .stTextInput>label {
            font-size: 16px;
            font-weight: 500;
            color: #4A3F35;
        }

        .chat-bubble {
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 10px;
            max-width: 85%;
            font-size: 15px;
        }

        .user-bubble {
            background-color: #6F4E37;
            color: white;
            align-self: flex-end;
        }

        .bot-bubble {
            background-color: #DCC7AA;
            color: #3E2723;
            align-self: flex-start;
        }

        .submit-button {
            background: linear-gradient(to right, #6F4E37, #9C6644);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: 0.3s;
        }

        .submit-button:hover {
            background: linear-gradient(to right, #9C6644, #6F4E37);
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# Title with coffee emoji
st.markdown("<h1>☕ Coffee Chatbot</h1>", unsafe_allow_html=True)
st.write("Relax with a cup of coffee and chat with AI!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# User input
user_input = st.text_input("Your Question:", key="user_input", placeholder="Ask anything...")

# Submit button
submit = st.button("☕ Ask Coffee Chatbot", key="ask_button")

if submit and user_input:
    try:
        # Get AI response
        response = chat_session.send_message(user_input)
        response_text = response.text

        # Store in chat history
        st.session_state["chat_history"].append(("You", user_input))
        st.session_state["chat_history"].append(("Coffee Chatbot", response_text))

    except Exception as e:
        st.error(f"Error processing request: {e}")

# Display chat history with cozy coffee-themed chat bubbles
if st.session_state["chat_history"]:
    st.subheader("🍂 Chat History")
    for role, text in st.session_state["chat_history"]:
        bubble_class = "user-bubble" if role == "You" else "bot-bubble"
        st.markdown(f'<div class="chat-bubble {bubble_class}"><b>{role}:</b> {text}</div>', unsafe_allow_html=True)
