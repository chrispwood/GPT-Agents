import os
from openai import OpenAI
from dotenv import load_dotenv
import json

# Load API key from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
# Ensure the API key is available
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key)


# Example function to query ChatGPT
def ask_chatgpt(messages):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        # temperature=0.7, # high temperature gives it more creativity and variability
        temperature=0.0 # low temperature gives it less creativity and more predictability
        )     
    
    response_model = response.model_dump()
    print(json.dumps(response_model, indent=4))  
    
    return response.choices[0].message.content


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."  
        },
    {
        "role": "user",
        "content": "What is the capital of France?"
        },
    {
        "role": "assistant",
        "content": "The capital of France is Paris."
        },
    {
        "role": "user",
        "content": "What is an interesting fact of Paris."
        }
    ]
response = ask_chatgpt(messages)
print(response)
