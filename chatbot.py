import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()

# Create the Claude client
client = Anthropic()

# This list is the "memory" — it stores the full conversation history
conversation_history = []

def chat(user_message):
    # Add the user's message to memory
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Send the FULL history to Claude every time — this is how memory works
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system="You are a helpful assistant.",
        messages=conversation_history
    )
    
    # Extract Claude's reply
    assistant_message = response.content[0].text
    
    # Add Claude's reply to memory too
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message

# Main loop — keeps chatbot running until you type 'quit'
print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    response = chat(user_input)
    print(f"\nClaude: {response}\n")