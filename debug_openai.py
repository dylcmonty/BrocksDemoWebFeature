import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the key from .env
load_dotenv('/home/ubuntu/BrocksDemo/openAIKEY.env')
api_key = os.getenv('OPENAI_API_KEY')

print("Loaded API Key:", api_key)

client = OpenAI(api_key=api_key)

try:
    models = client.models.list()
    print("Successfully connected! Available models:")
    for m in models.data:
        print("-", m.id)
except Exception as e:
    print("Error connecting to OpenAI API:", e)
