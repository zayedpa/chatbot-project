## CLI Chatbot with Memory ##

A terminal-based chatbot built with Python and Claude AI that remembers conversation history.

## What it does
- Maintains full conversation memory across the session
- Calls Anthropic's Claude API
- Runs directly in the terminal

## Tech used
- Python 3.11
- Anthropic Claude API
- python-dotenv

## How to run
1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/Scripts/activate`
4. Install dependencies: `pip install anthropic python-dotenv`
5. Copy `.env.example` to `.env` and add your API key
6. Run: `python chatbot.py`
