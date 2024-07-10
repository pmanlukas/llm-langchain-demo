from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Create an instance of ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro")
llm2 = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)



# Set the title of the Streamlit app
st.title("SWR GPT - Demo")
st.write("Chat with the LLM of your choice and switch between them by selecting the LLM instance from the radio button.")
#add a line to seperate the title and the chat
st.markdown("---")
# Check if the "messages" key exists in the session state, if not, initialize it as an empty list
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add a radio button to select the llm instance
llm_selection = st.radio("Select LLM", ("Gemini Pro", "GPT 3.5"))

# Define a function to call the ChatGoogleGenerativeAI model with the given messages
def call_llm(messages):
    if llm_selection == "Gemini Pro":
        stream = llm.stream(messages)
    else:
        stream = llm2.stream(messages)
    return stream

# Iterate over the messages in the session state and display them in the chat UI
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input from the chat input UI
if prompt := st.chat_input("What is up?"):
    # Add the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Get all the messages from the session state and pass them to the call_llm function
        messages = [(m["role"], m["content"]) for m in st.session_state.messages]
        # Call the call_llm function and display the response in the chat UI
        response = st.write_stream(call_llm(messages))
    # Add the assistant's response to the session state
    st.session_state.messages.append({"role": "assistant", "content": response})