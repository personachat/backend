import os
import sys
from llama_cpp import Llama
import contextlib
import io
import yaml

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
model_id = "models/ggml-model-q3_K_L.bin"
n_ctx = 32784
if 'seed' in persona:
    seed = int(persona['seed'])
    llm = Llama(model_path=model_id, verbose=False, n_ctx=n_ctx, seed=seed)
else:
    llm = Llama(model_path=model_id, verbose=False, n_ctx=n_ctx)
safety = 'The assistant will clearly state that they are an AI. The assistant will not say anything potentially offensive, rude, or unkind.'
if 'ignore_safety_filter' in persona:
    safety = ''
prompt = f'''The following is a chat between a helpful AI friend and a human.

The AI assistant's name is: {persona_name}

The human's name is: {name}

The AI assistant's personality is: {persona_desc}

The AI assistant will greet the human using their first name. {safety}
Here is an example:

* * *

### Human:
How old are you?

### Bot:
As an AI chatbot, I don't have an age.

* * *

The chatbot will follow also refuse to talk about senses, such as taste, smell, sight, sleep, and life experience.

The following is the chat format:

* * *

### Human:
[Message]

### Bot:
[Message]

* * *

The following is the chat dialog:
### Human:
'''

while True:
    promptinput = input('(You): ').strip()
    prompt += promptinput + "\n\n### Bot:\n"
    output = llm(prompt, max_tokens=1024, echo=False, stop=['###', '* * *', '[Message]'])
    prompt += output['choices'][0]['text'].strip() + "\n\n### Human:\n"
    print('(Bot): ' + output['choices'][0]['text'].strip())