import json
import openai
import os
import random
from dotenv import load_dotenv

# Define function to load environment variables from .env file


def load_dotenv():
    # load environment variables from .env file
    load_dotenv('.secrets.env')


def load_env_vars():
    load_dotenv()
    # set API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")


# load environment variables from .env file
load_env_vars()

# Load arcsDicts.json

# Load arcsDicts.json


def load_json():
    with open('arcsDicts.json') as f:
        data = json.load(f)
    return data


# Call the function to get the selected arc and its phases
data = load_json()
random_arc_data = random.choice(data)
random_arc = random_arc_data["arc"]
phases = list(random_arc_data["phases"].values())

print("Selected arc:")
print(random_arc)

# Path: apiFunctions.py
parameters = {
    "model": "text-davinci-003",
    "prompt": "List classic story arcs in fiction.",
    "temperature": 0,  # 0 means no randomness 1 means completely random
    "max_tokens": 50,  # max number of tokens to generate
    "top_p": 1,  # 1 means no filtering, 0 means only the most likely token`
    # 0 means no penalty, 1 means penalize new tokens based on their existing frequency
    "frequency_penalty": 1,
    # 0 means no penalty, 1 means penalize new tokens based on whether they appear in the prompt
    "presence_penalty": 1
}

# Create a variable to store the chat history
chat_history = []

# Define a function to generate a response to a prompt


def chat_request_response(prompt):
    # Example OpenAI Python library request
    MODEL = "text-davinci-002"
    response = openai.Completion.create(
        engine=MODEL,
        prompt=prompt,
        temperature=0.9,
        max_tokens=1000,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0,
    )
    # Get the message object from the first choice
    message = response["choices"][0]["text"].strip()
    return message


# Call the function to start the chat
first_prompt = f"Write the introduction to a novel in the {random_arc} arc style."
response = chat_request_response(first_prompt)
print(response)
chat_history.append(response)

# Call the function to generate subsequent responses
for phase in phases:
    prompt = f"Write a paragraph in the '{phase}' phase of the {random_arc} arc style."
    response = chat_request_response(prompt)
    print(response)
    chat_history.append(response)


print(random_arc)
print(chat_history)
