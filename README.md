# Coffee Bot : Based on Gemini API

## Overview
This repository contains a FastAPI-based application that integrates with Google's Generative AI (Gemini) model to create a conversational chatbot interface. Users can interact with the Gemini model by entering queries and receiving responses in real time.

## Features
- **Generative AI Integration**: Uses the `google.generativeai` library to interact with the Gemini model.
- **Customizable Parameters**: Configure model parameters such as `temperature`, `top_p`, `top_k`, and `max_output_tokens`.
- **Interactive Interface**: Made with Vite based React, TypeScript and Tailwind.

## Setup Instructions

### Prerequisites for Backend
1. Python 3.X.
2. Install required Python libraries:
   ```bash
   pip install fastapi python-dotenv google-generativeai pydantic
   ```
3. Obtain a Gemini API key from [Google AI](https://ai.google.dev/gemini-api/docs/).

### Environment Variables
Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### Running the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gemini-chatbot.git
   cd coffeebot
   ```

2. Run the fastAPI backend:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000
   ```

3. Open the provided URL in your browser to interact with the chatbot.

4. Open another terminal and change directory for frontend:

```bash
cd frontend

npm install # to setup frontend

npm run dev # to start frontend in development mode
```

## Configuration

The application allows customization of the model's generation configuration. Modify the following parameters in the code as needed:

- **`temperature`**: Controls the randomness of the output.
- **`top_p`**: Sets the nucleus sampling threshold.
- **`top_k`**: Limits the number of candidate tokens considered at each step.
- **`max_output_tokens`**: Maximum number of tokens in the output.

## Usage
1. Start the application.
2. Enter your question in the input box and click "Enter".
3. View the AI response below the input box.

## Code Structure
- **`app.py`**: The main application file containing the chatbot logic and Streamlit interface.
- **`.env`**: Environment file for storing Gemini API Key.

## Error Handling
- Ensures the Gemini API key is provided. If missing, displays an error message and stops execution.
- Handles exceptions during model initialization or message processing, displaying user-friendly error messages.


## Testing using Postman

Message

```json
{
    "message": "Hello, dear Coffee Bot"
}
```

Response

```json
{
    "reply": "Hello there!  How can I help you with your coffee needs today?\n"
}
```

## Limitations
- There is no feature to save the chat history.
- Requires a valid Gemini API key to function.


## License
This project is open-source and available under the [MIT License](LICENSE).

