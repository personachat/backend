import os
import sys
from llama_cpp import Llama
import contextlib
import io
import yaml
from datetime import datetime

# Load YAML
while True:
    file = input('Please enter the filename of the YAML personality in the `personas` folder: ').strip()
    if (os.path.isfile('personas/' + file)):
        break
    else:
        if (os.path.isfile('personas/' + file + '.yaml')):
            file = file + '.yaml'
            break
        else:
            print("Sorry, we couldn't find that file. Please try again.")
while True:
    name = input('What is your first and last name: ').strip()
    if (name == ''):
        print("Sorry, we couldn't find that file. Please try again.")
    else:
        print(f"Hello, {name}")
        break


with open('personas/' + file, 'r') as file:
    persona = yaml.safe_load(file)

persona_name = persona['name']
persona_desc = persona['description']
model_id = "models/ggml-model-q4_1.bin"
n_ctx = 32784
if 'seed' in persona:
    seed = int(persona['seed'])
    llm = Llama(model_path=model_id, verbose=False, n_ctx=n_ctx, seed=seed)
else:
    llm = Llama(model_path=model_id, verbose=False, n_ctx=n_ctx)
safety = 'The assistant will clearly state that they are an AI. The assistant will not say anything potentially offensive, rude, or unkind. The chatbot will follow also refuse to talk about senses, such as taste, smell, sight, sleep, and life experience. '
if 'ignore_safety_filter' in persona:
    safety = ''
current_date = datetime.now().strftime("%A, %B %d, %Y")
prompt = f'''The following is a chat between a helpful AI assistant named {persona_name} and a human named {name}. The chat took place on {current_date}.
The AI assistant is {persona_desc}. It will greet the human using their first name. {safety}The AI assistant cannot "see" things about the user, as the AI is just a bot on a computer. The AI assistant does not know of anything that happened to the human previously, and will act as if they met the human for the first time. The chatbot does not have any knowledge of current events, such as weather, news, or politics, but knows history. The chatbot can also write poems, essays, and short stories. The chatbot does NOT know ANYTHING about weather, time, current events, news, or politics!!!
The prompting format for the conversation is:
### Human:
[Message]

### Bot:
[Message]

* * *

The following is the conversation:
### Human:
'''
while True:
    promptinput = input('(You): ').strip()
    prompt += promptinput + "\n\n### Bot:\n"
    output = llm(prompt, max_tokens=1024, echo=False, stop=['###', '* * *', '[Message]', 'Human:', 'Bot:'])
    prompt += output['choices'][0]['text'].strip() + "\n\n### Human:\n"
    print('(Bot): ' + output['choices'][0]['text'].strip())