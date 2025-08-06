import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('PROJECT_ENDPOINT')

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://kumaa-mdv6ddmb-swedencentral.cognitiveservices.azure.com/",
    api_key=api_key,
)

import os
from openai import AzureOpenAI

endpoint = "https://kumaa-mdv6ddmb-swedencentral.cognitiveservices.azure.com/"
model_name = "gpt-4o"
deployment = "gpt-4o"

subscription_key = "<your-api-key>"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(response.choices[0].message.content)

