import openai
import os
from dotenv import load_dotenv
from typing import List, Dict

# Load environment variables from the .env file
load_dotenv()

class OpenAIService:
    def __init__(self):
        # Get the OpenAI API key from environment variables
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        openai.api_key = self.api_key

    def send_message(self, message: List[Dict[str, str]]) -> str:
        try:
            # Call OpenAI API with the provided message
            response = openai.chat.completions.create(
                model="gpt-4",  # Or use the latest model
                messages=message
            )
            # Return the generated text from OpenAI API
            return response.choices[0].message
        except Exception as e:
            raise Exception(f"Error interacting with OpenAI API: {str(e)}")