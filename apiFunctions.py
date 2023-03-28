import openai
import os
from dotenv import load_dotenv
import json

# Create a variable to store the chat history
chat_history = []

# Define a function to generate a response to a prompt


def first_chat_request_response():
    # load environment variables from .env file
    load_dotenv('.secrets.env')
    # set API key from environment variable
    openai.api_key = os.environ["openaiApi"]
    # Define the model name
    MODEL = "gpt-3.5-turbo"
    # Define the content to start the prompt
    CONTENT = "You are a novelist."
    # Define the prompt
    PROMPT = f"Write a sentence describing a monster in the style of HP Lovecraft."
    # Example OpenAI Python library request
    response = openai.ChatCompletion.create(model=MODEL, messages=[{"role": "system", "content": CONTENT}, {
                                            "role": "user", "content": PROMPT}], temperature=0)
    # Get the message object from the first choice
    message = response["choices"][0]["message"]
    # Format the message content as a dictionary
    message_content = {"role": message["role"], "content": message["content"]}
    # Append the message content to the chat history
    chat_history.append(message_content)

# Define a function to generate a response to a prompt


def subsequent_chat_request_response():
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


# Call the function to start the chat
first_chat_request_response()

# Call the function to generate a followup response
subsequent_chat_request_response()

# Call the function to generate a followup response
subsequent_chat_request_response()


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
    PROMPT = f"Write a sentence describing a monster eating a man named Justin in the style of HP Lovecraft."
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
