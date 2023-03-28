import openai
import os
from dotenv import load_dotenv
import json

chat_history = []
PROMPT = "Write a passage describing radio wave propegation."
MODEL = "gpt-3.5-turbo"
CONTENT = "You are an MC on the History Channel Show Modern Marvels"


def getContent(PROMPT, MODEL, CONTENT):
    # Create a variable to store the chat history
    chat_history = []
    # set API key from enviroment variable
    load_dotenv('.secrets.env')
    # set API key from environment variable
    openai.api_key = os.environ["openaiApi"]
    # API interaction
    response = openai.ChatCompletion.create(model=MODEL, messages=[{"role": "system", "content": CONTENT}, {
        "role": "user", "content": PROMPT}], temperature=0)
    message = response["choices"][0]["message"]
    message_content = {"role": message["role"], "content": message["content"]}
    # add to chat history
    chat_history.append(message_content)


getContent(PROMPT, MODEL, CONTENT)

# print acumulated content
for i in range(len(chat_history)):
    print(chat_history[i]["content"])
