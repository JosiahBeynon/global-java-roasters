import streamlit as st

if 'chat_active' not in st.session_state:
    st.session_state['chat_active'] = False
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ''

user_input = st.text_input('Enter your name:', value=st.session_state['user_name'])

if st.button('Begin Chat'):
    if user_input:
        st.session_state['chat_active'] = True
        st.session_state['user_name'] = user_input

if st.session_state['chat_active'] and st.session_state['user_name']:
    st.write(f"Hello {st.session_state['user_name']}, welcome to our chat service!")
    st.write("You are now chatting with GlobalJava Roasters.")
else:
    if st.session_state['chat_active']:
        st.write("Please enter your name to begin the chat.")







import streamlit as st
import random

bot_responses = [
        "Sure, let me check that for you.",
        "I'm not quite sure. Let me find out.",
        "Hmm, I need to think about that.",
        "Interesting question! Give me a moment."
    ]

class ChatManager:
    def __init__(self):
        self.chat_history = []

    def add_message(self, sender, message):
        self.chat_history.append({"sender": sender, "message": message})

    def get_chat_history(self):
        return self.chat_history
    
    # Add new method here:
    def clear_chat_history(self):
        self.chat_history = []
    

if 'chat_manager' not in st.session_state:
    st.session_state['chat_manager'] = ChatManager()

chat_manager = st.session_state['chat_manager']

user_input = st.chat_input("Write a message")

if user_input:
    chat_manager.add_message("user", user_input)
    bot_response = random.choice(bot_responses)
    chat_manager.add_message("bot", bot_response)

for chat in chat_manager.get_chat_history():
    with st.chat_message(chat["sender"]):
        st.write(chat["message"])
        
# Add new button widget here:
st.button("Clear chat history", on_click=chat_manager.clear_chat_history)