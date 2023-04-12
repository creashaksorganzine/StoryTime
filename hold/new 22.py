import json
import openai
import os
import random
from dotenv import load_dotenv as dotenv_load_dotenv


def load_dotenv_file():
    dotenv_load_dotenv('.secrets.env')


def load_env_vars():
    load_dotenv_file()
    openai.api_key = os.getenv("OPENAI_API_KEY")


def load_json():
    with open('arcsDicts.json') as f:
        data = json.load(f)
    return data


def select_story_arc():
    data = load_json()
    random_arc_data = random.choice(data)
    random_arc = random_arc_data["arc"]
    phases = list(random_arc_data["phases"].values())
    return random_arc, phases


def chat_request_response(prompt, chat_history):
    full_prompt = "\n\n".join(chat_history) + "\n\n" + prompt
    MODEL = "text-davinci-002"
    response = openai.Completion.create(
        engine=MODEL,
        prompt=full_prompt,
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0,
    )
    message = response["choices"][0]["text"].strip()
    return message


def return_json(random_arc, phases, chat_history):
    return {'story_arc': random_arc, 'phases': phases, 'chat_history': chat_history}


load_env_vars()
chat_history = []

random_arc, phases = select_story_arc()

response_data = return_json(random_arc, phases, chat_history)

with open('output.json', 'w') as outfile:
    json.dump(response_data, outfile, indent=4)
