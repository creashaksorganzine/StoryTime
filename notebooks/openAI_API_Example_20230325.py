import openai
import os
from dotenv import load_dotenv

load_dotenv('.secrets.env')
openai.api_key = os.environ["openaiApi"]
MODEL = "gpt-3.5-turbo"
chat_history = [
    {
        "role": "system",
        "content": "You are a novelist."
    }
]

response = openai.Completion.create(
    engine=MODEL,
    prompt=chat_history,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

generated_text = response.choices[0].text

print(generated_text)

chat_history.append({
    "role": "user",
    "content": generated_text.strip()
})

response = openai.Completion.create(
    engine=MODEL,
    prompt=chat_history,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

generated_text = response.choices[0].text

print(generated_text)

'''
===========================================================
This is a Python code that uses the OpenAI API to generate text based on a prompt. The prompt is defined as the variable chat_history, which is a list of dictionaries that represent the conversation history. The initial prompt sets the role of the user as a novelist.

The code uses the openai.Completion.create() method to generate text based on the prompt. The generated text is stored in the generated_text variable and is printed to the console.

The chat_history list is then updated with the generated text and the process is repeated to generate a response from the AI model.

The temperature, max_tokens, top_p, frequency_penalty, and presence_penalty parameters are used to control the behavior of the AI model and the quality of the generated text.

The dotenv module is used to load the OpenAI API key from a .secrets.env file, which is not included in the code snippet.
===========================================================

'''
