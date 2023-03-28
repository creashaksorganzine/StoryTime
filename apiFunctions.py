import openai
import os
from dotenv import load_dotenv
import json

chat_history = []


def first_chat_request_response():
    # load environment variables from .env file
    load_dotenv('.secrets.env')
    # set API key from environment variable
    openai.api_key = os.environ["openaiApi"]
    # Define the model name
    MODEL = "gpt-3.5-turbo"
    # Example OpenAI Python library request
    response = openai.ChatCompletion.create(model=MODEL, messages=[{"role": "system", "content": "You are a novelist."}, {
                                            "role": "user", "content": "Write a sentence describing a banana in the style of HP Lovecraft."}], temperature=0)
    # Get the message object from the first choice
    message = response["choices"][0]["message"]
    # Format the message content as a dictionary
    message_content = {"role": message["role"], "content": message["content"]}
    # Append the message content to the chat history
    chat_history.append(message_content)


# Call the function to start the chat
first_chat_request_response()

# print(len(chat_history))
# print(chat_history)


def subsequent_chat_request_response():
    # Example OpenAI Python library request
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=chat_history,
        temperature=0,
    )
    # print(response)
    # reposense = response
    # Get the message object from the first choice
    message = response["choices"][0]["message"]
    # Format the message content as a dictionary
    message_content = {"role": message["role"], "content": message["content"]}
    # Append the message content to the chat history
    chat_history.append(message_content)


# Call the function to generate a response
subsequent_chat_request_response()

# print(len(chat_history))
# print(chat_history)
