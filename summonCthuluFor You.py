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

summonCthulu()

for i in range(len(chat_history)):
    print(chat_history[i]["content"])
'''
As the grotesque abomination feasted upon the flesh of the hapless Justin, its writhing tentacles and gaping maw exuded an otherworldly stench that would haunt the dreams of any who bore witness to its unspeakable horror.

...

The creature's eyes glowed with a sickly green light as it tore into Justin's body, its razor-sharp teeth tearing through flesh and bone with ease. The sound of bones cracking and flesh tearing filled the air, accompanied by Justin's screams of agony.

As the creature continued to feed, its form seemed to shift and contort, as if it were not entirely of this world. Its tentacles writhed and twisted, each one ending in a sharp, barbed tip that it used to tear into its prey.

Despite the horror of the scene before them, the onlookers were unable to tear their eyes away. They were frozen in place, unable to move or even scream as they watched the creature devour Justin.

Finally, after what seemed like an eternity, the creature finished its meal and turned its attention to the horrified witnesses. With a guttural growl, it lunged towards them, its tentacles flailing and its jaws snapping hungrily.

In that moment, the onlookers knew that they were doomed. They had stumbled upon something beyond their understanding, and now they would pay the ultimate price for their curiosity.
'''