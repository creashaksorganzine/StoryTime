import openai
import os
import random
from dotenv import load_dotenv


def openaiCompletionArcs(parameters):
    # load environment variables from .env file
    load_dotenv('.secrets.env')
    # set API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # call the OpenAI API to generate the list of story arcs
    response = openai.Completion.create(
        **parameters
    )

    # extract the list of story arcs from the API response
    story_arcs = [arc.strip()
                  for arc in response.choices[0].text.split("\n") if arc.strip()]

    # pick a random story arc and store it as a variable
    random_arc = random.choice(story_arcs)

    return story_arcs, random_arc


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

# parameters = {
#     "model": "text-davinci-003",
#     "prompt": "List classic story arcs in fiction.",
#     "temperature": 0,
#     "max_tokens": 150,
#     "top_p": 1,
#     "frequency_penalty": 1,
#     "presence_penalty": 1
# }

story_arcs, random_arc = openaiCompletionArcs(parameters)
print("Story arcs:")
print("\n".join(story_arcs))
print('\n')
print("Randomly selected arc:")
print(random_arc)

# Create a variable to store the chat history
chat_history = []

# Define a function to generate a response to a prompt


def first_chat_request_response():
    # load environment variables from .env file
    load_dotenv('.secrets.env')
    # set API key from environment variable
    openai.api_key = os.environ["OPENAI_API_KEY"]
    # Define the model name
    MODEL = "gpt-3.5-turbo"
    # Define the content to start the prompt
    CONTENT = f"You are a novelist writing in the {random_arc} arc style."
    # Define the prompt
    PROMPT = f"Write the introduction to a novel in the {random_arc} arc style."
    # Example OpenAI Python library request
    response = openai.ChatCompletion.create(model=MODEL, messages=[{"role": "system", "content": CONTENT}, {
                                            "role": "user", "content": PROMPT}], temperature=0.6)
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
        temperature=0.9,
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

print(random_arc)
print(chat_history)
