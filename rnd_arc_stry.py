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


def chat_request_response(prompt):
    MODEL = "text-davinci-003"
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
    message = response["choices"][0]["text"].strip()
    return message


def extract_story_elements(text):
    # Implement a custom function to extract story elements like characters, places, etc.
    # This is just a simple example; you can improve the function based on your requirements.
    story_elements = {
        "characters": [],
        "places": []
    }
    # Add your extraction logic here
    return story_elements


def return_json(random_arc, phases, chat_history):
    return {'story_arc': random_arc, 'phases': phases, 'chat_history': chat_history}


load_env_vars()
chat_history = []

random_arc, phases = select_story_arc()

first_prompt = f"Write the introduction to a novel in the {random_arc} arc style."
response = chat_request_response(first_prompt)
story_elements = extract_story_elements(response)
chat_history.append(
    {'phase': 'introduction', 'text': response, 'story_elements': story_elements})

for phase in phases:
    prompt = f"Write a paragraph in the '{phase}' phase of the {random_arc} arc style."
    response = chat_request_response(prompt)
    story_elements = extract_story_elements(response)
    chat_history.append({'phase': phase, 'text': response,
                        'story_elements': story_elements})

response_data = return_json(random_arc, phases, chat_history)

with open('output.json', 'w') as outfile:
    json.dump(response_data, outfile, indent=4)
