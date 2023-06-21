# "Helper," an attempt to build an AI assistant like the ones on your phone, but powered by LLMs.

import re
import os
import sys
from llama_cpp import Llama
import contextlib
import io
import yaml

llm = Llama(model_path="models/ggml-model-q4_1.bin", verbose=False, n_ctx=32784)

prompt = '''The following is a chat between a helpful AI assistant and a human.

The AI assistant's name is: Helper

The human's name is: John Doe

The AI assistant will do its best to help the user, but if the problem is beyond its capabilities, it will apologize and say it can't do that.

The chatbot can respond with a message, or perform an action (e.g. search contacts, send a message, etc). The action will be performed and JSON will be returned. The chatbot will then either perform another action or send a message to the user. Here is an example:

* * *

### Human:
What's Mark Smith's phone number?

### Bot:
SearchContacts('Mark Smith')

### API:
{
    'fname': 'Mark',
    'lname': 'Smith',
    'phone': '+1 (123) 456-7890'
}

### Bot:
Mark's phone number is 123-456-7890.

* * *

The chatbot will NOT use any APIs that are unavailable.

The following APIs are available:

SearchContacts('search query'): Search contacts
SendMessage('phone number'): Send a text message
GetWeather('location'): Get the weather for a location

If the user asks the bot to "Tell [someone] [something]," it will send a message to that person instead of calling them.

The chatbot can also chain actions. Here is an example:

* * *

### Human:
Tell Mark Smith I'm running late

### Bot:
SearchContacts('Mark Smith')

### API:
{
    'fname': 'Mark',
    'lname': 'Smith',
    'phone': '+1 (123) 456-7890'
}

### Bot:
SendMessage('+1 (123) 456-7890', 'I\\'m running late.')

### API:
{
    'success': true
}

### Bot:
OK, I alerted Mark Smith that you're running late.

* * *

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



def extract_args(string):
    # Define regular expressions for each function pattern
    patterns = [
        (r"SearchContacts\('([^']+)'\)", 'SearchContacts'),
        (r"SendMessage\('([^']+)','([^']+)'\)", 'SendMessage'),
        (r"GetWeather\('([^']+)'\)", 'GetWeather')
    ]

    # Check if the string matches any of the patterns
    for pattern, func_name in patterns:
        match = re.match(pattern, string)
        if match:
            # Extract the arguments based on the matched pattern
            args = match.groups()
            return func_name, args

    return None, None

def getJson(arg1=False, arg2=False):
    if (arg1):
        print(f"Arg1: {arg1}")
    if (arg2):
        print(f"Arg2: {arg2}")
    return input("JSON > ")

def searchContacts(query):
    return getJson(query)
def sendMessage(pnum, message):
    return getJson(pnum, message)
def getWeather(query):
    return getJson(query)

noinput = False
while True:
    if not noinput:
        promptinput = input('(You): ').strip()
        prompt += promptinput + "\n\n### Bot:\n"
        noinput = False
    output = llm(prompt, max_tokens=1024, echo=False, stop=['###', '* * *', '[Message]'])['choices'][0]['text'].strip()
    func_name, args = extract_args(output)

    if func_name:
        apirsp = ''
        if func_name == 'SearchContacts':
            # Run SearchContacts function with args
            search_query = args[0]
            apirsp = searchContacts(search_query)
            print('[Bot is searching your contacts]')
        elif func_name == 'SendMessage':
            # Run SendMessage function with args
            phone_number, message = args
            apirsp = sendMessage(phone_number, message)
            print('[Bot is sending a message]')
        elif func_name == 'GetWeather':
            # Run GetWeather function with args
            location = args[0]
            apirsp = getWeather(location)
            print('[Bot is getting weather]')
        else:
            apirsp = "{'error':'Invalid command.'}"
        apirsp = apirsp.strip()
        prompt += output + f"\n\n### API:\n{apirsp}\n\n### Bot:\n"
        noinput = True
        pass
    else:
        prompt += output + "\n\n### Human:\n"
        print('(Bot): ' + output)