import openai
import os
from dotenv import load_dotenv
import json

# Create a variable to store the chat history
chat_history = []


def summonCthulu():
    # load environment variables from .env file
    load_dotenv('.secrets.env')
    # set API key from environment variable
    openai.api_key = os.environ["openaiApi"]
    # Define the model name
    MODEL = "gpt-3.5-turbo"
    # Define the content to start the prompt
    CONTENT = "You are a novelist."
    # Define the prompt
    PROMPT = f"Write a sentence describing a monster eating a man in the style of HP Lovecraft."
    # Example OpenAI Python library request
    response = openai.ChatCompletion.create(model=MODEL, messages=[{"role": "system", "content": CONTENT}, {
                                            "role": "user", "content": PROMPT}], temperature=0)
    # Get the message object from the first choice
    message = response["choices"][0]["message"]
    # Format the message content as a dictionary
    message_content = {"role": message["role"], "content": message["content"]}
    # Append the message content to the chat history
    chat_history.append(message_content)
    # Example OpenAI Python library request
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=chat_history,
        temperature=0,
    )
    # Get the message object from the first choice
    message = response["choices"][0]["message"]
    # Format the message content as a dictionary
    message_content = {"role": message["role"], "content": message["content"]}
    # Append the message content to the chat history
    chat_history.append(message_content)


summonCthulu()

for i in range(len(chat_history)):
    print(chat_history[i]["content"])
