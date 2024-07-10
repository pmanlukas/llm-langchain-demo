#GPT Demo for Media Customer

This demo allows you to chat with two powerful Large Language Models (LLMs):

* **Google Gemini Pro:** A cutting-edge LLM developed by Google.
* **OpenAI GPT-3.5 Turbo:** The latest version of OpenAI's widely used model.

The demo uses the Streamlit framework for a user-friendly interface and LangChain to seamlessly integrate the LLMs.

## Features

* **Chat Interface:** Engage in conversations with either Gemini Pro or GPT-3.5 Turbo.
* **LLM Switching:** Easily switch between the two LLMs using a radio button.
* **Streaming Responses:**  Experience the models' responses as they're being generated.
* **Chat History:**  See the full conversation history, including both your prompts and the LLM responses.
* **Environment Variable Loading:** Securely manages API keys using `.env` file.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://your-repository-url.git
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Obtain API Keys:**
   * **Google Gemini Pro:** Get your API key from the Google Cloud Console.
   * **OpenAI GPT-3.5 Turbo:** Get your API key from the OpenAI platform.
   
2. **Set Environment Variables:**
    - Create a `.env` file in the project's root directory with the following contents:
       ```
       OPENAI_API_KEY=your_openai_api_key
       GOOGLE_API_KEY=your_google_api_key
       ```
       

## Running the Demo

1. **Activate your virtual environment (if you created one):**
   ```bash
   source venv/bin/activate
   ```
   
2. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```


3. **Open your browser:**
   * The app will open automatically in your default browser (usually at `http://localhost:8501`).
    
## Usage

1. **Select LLM:** Use the radio button to choose between "Gemini Pro" or "GPT 3.5".
2. **Start Chatting:** Type your message in the chat input box and press Enter.
3. **See the Response:** The LLM's response will stream in real-time.
4. **Switch LLMs:** You can switch between LLMs at any time, and the chat history will be preserved.


## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgments

* **Streamlit:**  For the fantastic app framework.
* **LangChain:** For simplifying LLM integration.
* **Google and OpenAI:** For their amazing AI models.
