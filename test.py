import os
import boto3
import json
from openai import OpenAI
from datetime import datetime
from IPython.display import clear_output, display, display_markdown, Markdown

# Initialize both clients
client = OpenAI()  # For chat completions API
bedrock_client = boto3.client('bedrock-runtime', region_name='us-west-2')  
# response = client.chat.completions.create(
#     model="openai.gpt-oss-120b",
#     messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
#     )
# print(response)

response = client.chat.completions.create(
    model="openai.gpt-oss-120b",               
    messages=[
        {"role": "system", "content": "You are a concise, highly logical assistant."},
        {"role": "user",   "content": "What is the largest city in the southern hemisphere?"}
    ],
    temperature=0,
    max_completion_tokens=1000,
    reasoning_effort="low"            
)

# Extract and print the response text
print(response.choices[0].message.content)