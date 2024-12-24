# Gemini Chatbot Application

## Overview
This repository contains a Streamlit-based application that integrates with Google's Generative AI (Gemini) model to create a conversational chatbot interface. Users can interact with the Gemini model by entering queries and receiving responses in real time.

## Features
- **Generative AI Integration**: Uses the `google.generativeai` library to interact with the Gemini model.
- **Customizable Parameters**: Configure model parameters such as `temperature`, `top_p`, `top_k`, and `max_output_tokens`.
- **Interactive Interface**: A Streamlit-powered user interface for seamless chatbot interactions.
- **Chat History**: Maintains a history of the conversation within the session.

## Setup Instructions

### Prerequisites
1. Python 3.7 or higher.
2. Install required Python libraries:
   ```bash
   pip install streamlit python-dotenv google-generativeai
   ```
3. Obtain a Gemini API key from [Google Generative AI](https://ai.google/).

### Environment Variables
Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### Running the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gemini-chatbot.git
   cd gemini-chatbot
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided URL in your browser to interact with the chatbot.

## Configuration
The application allows customization of the model's generation configuration. Modify the following parameters in the code as needed:
- **`temperature`**: Controls the randomness of the output.
- **`top_p`**: Sets the nucleus sampling threshold.
- **`top_k`**: Limits the number of candidate tokens considered at each step.
- **`max_output_tokens`**: Maximum number of tokens in the output.

## Usage
1. Start the application.
2. Enter your question in the input box and click "Ask".
3. View the AI response below the input box.
4. Chat history is displayed at the bottom of the page.

## Code Structure
- **`app.py`**: The main application file containing the chatbot logic and Streamlit interface.
- **`.env`**: Environment file for storing sensitive credentials.

## Error Handling
- Ensures the Gemini API key is provided. If missing, displays an error message and stops execution.
- Handles exceptions during model initialization or message processing, displaying user-friendly error messages.

## Limitations
- The chat history is session-based and does not persist across sessions.
- Requires a valid Gemini API key to function.

## Future Enhancements
- Add support for chat history persistence using a database or file system.
- Enhance the user interface with richer styling and themes.
- Integrate more advanced model configurations.

## License
This project is open-source and available under the [MIT License](LICENSE).

