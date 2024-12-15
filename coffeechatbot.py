import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure the API key is set
if "GEMINI_API_KEY" not in os.environ:
    st.error("Environment variable GEMINI_API_KEY is missing. Set it in your environment or .env file.")
    st.stop()

# Configure the Generative AI client
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the Generative AI model
try:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    chat_session = model.start_chat(history=[])
except Exception as e:
    st.error(f"Failed to initialize the Gemini model: {e}")
    st.stop()

# Streamlit App Configuration
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("Gemini Chatbot")
st.write("Interact with the Gemini LLM. Enter your query below!")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Custom CSS to style the font weight
st.markdown(
    """
    <style>
        .stTextInput > label {
            font-weight: 350;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# User input section
user_input = st.text_input("Your question:", key="user_input", placeholder="Type your message here...")
submit = st.button("Ask")

if submit and user_input:
    try:
        # Send user input to Gemini and get response
        response = chat_session.send_message(user_input)
        response_text = response.text

        # Save interaction in chat history
        st.session_state["chat_history"].append(("You", user_input))
        st.session_state["chat_history"].append(("Gemini", response_text))

        # Show the immediate response
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**Gemini:** {response_text}")

    except Exception as e:
        st.error(f"An error occurred while processing your request: {e}")

# Display the chat history after showing the immediate response
if st.session_state["chat_history"]:
    st.subheader("Chat History:")
    for role, text in st.session_state["chat_history"]:
        st.markdown(f"**{role}:** {text}")
