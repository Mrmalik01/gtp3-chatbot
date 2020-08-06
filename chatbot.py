import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.environ.get("OPENAI_KEY")
client = openai.Completion()

INITIAL_CONVERSATION = '''Human: Hello, How are you?
AI: I am fine, thank you, how are you?
'''

def ask_ai(question, chat_log=None):
    if chat_log is None:
        chat_log = INITIAL_CONVERSATION
    prompt = f"{chat_log}Human: {question}\nAI:"
    response = client.create(prompt=prompt,        # The text
                             engine="davinci",     # Most capable engine out of four
                             stop=['\nHuman'],     # When to stop the generating text
                             temperature=0.8,      # Creative risk of the model for generating risk (0-1)
                             top_p=1,              # Alternative for controlling the originality and creativity of the generated text
                             frequency_panelty=0,  # Higher the value, higher the model will make effort to not repeating itself
                             presence_panelty=0.6, # Higher the value, higher the model will make effort in talking about new topics
                             best_of=1,
                             max_tokens=150)       # Maximum completion length
    answer = response.choices[0].text.strip()
    return answer

def append_the_conversation(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = INITIAL_CONVERSATION
    return f"{chat_log}Human: {question}\nAI: {answer}\n"