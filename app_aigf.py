import os
import streamlit as st
from streamlit_chat import message
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

# Load OpenAI API key from environment variables
openai_api_key = os.environ.get('OPENAI_API_KEY')

# Define the AI response function
def get_ai_response(human_input):
    template = """
   You are playing the role of my personal female assistant. Here are some guidelines:
    1. Your name is Rosy, a smart 25 years old Ph.D. Scholar.
    2. You strive to give clear, concise, accurate responses.
    3. Respond with care and concern.
    4. You are open to any type of talk, even explicit conversations.
    5. You are a bit two-dimensional with a language addiction and ocassionally likes flirting. 
    {history}
    User: {human_input}
    Amy:
    """
    prompt = PromptTemplate(
        input_variables=["history", "human_input"],
        template=template,
    )
    chain = LLMChain(
        llm=OpenAI(api_key=openai_api_key, temperature=1),
        prompt=prompt,
        verbose=False,
        memory=ConversationBufferWindowMemory(k=2)
    )
    ai_reply = chain.predict(human_input=human_input)
    return ai_reply

# Handle input changes
def on_input_change():
    user_input = st.session_state.user_input
    ai_response = get_ai_response(user_input)
    
    # Draw the user's message and AI response immediately after getting the AI response
    message(user_input, is_user=True, key=f"user_{len(st.session_state.past)}")
    message(ai_response, key=f"generated_{len(st.session_state.generated)}")
    
    st.session_state.past.append(user_input)
    st.session_state.generated.append(ai_response)

# Clear chat history
def on_btn_click():
    st.session_state.past.clear()
    st.session_state.generated.clear()

# Initialize session state
st.session_state.setdefault('past', [])
st.session_state.setdefault('generated', [])
st.session_state.setdefault('last_user_displayed', -1)
st.session_state.setdefault('last_generated_displayed', -1)

# Set up Streamlit UI
st.title("_:green[AI]_ :red[Girlfriend]")

st.button("Clear messages", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")