import openai
from openai import OpenAI
import streamlit as st
from config import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL

class Chatbot:
    def __init__(self, system_message="You are a helpful AI assistant."):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_BASE_URL
        )
        self.system_message = system_message
        self.conversation_history = []
        
    def add_message(self, role, content):
        """Add a message to the conversation history"""
        self.conversation_history.append({"role": role, "content": content})
        
    def get_response(self, user_message):
        """Get response from OpenAI using the responses endpoint"""
        try:
            # Add user message to history
            self.add_message("user", user_message)
            
            # Prepare messages for API call
            messages = [{"role": "system", "content": self.system_message}] + self.conversation_history
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=messages,
                stream=False
            )
            
            # Extract assistant response
            assistant_response = response.choices[0].message.content
            
            # Add assistant response to history
            self.add_message("assistant", assistant_response)
            
            return assistant_response
            
        except Exception as e:
            st.error(f"Error communicating with OpenAI: {str(e)}")
            return "I'm sorry, I encountered an error. Please try again."
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
    
    def get_history(self):
        """Get current conversation history"""
        return self.conversation_history
