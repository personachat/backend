# PersonaChat API
from flask import Flask, request, jsonify
import hashlib
import os
from llama_cpp import Llama

app = Flask(__name__)
model_id = "../models/ggml-model-q4_1.bin"
# model_id = "../models/open-llama-13b-q4_0.bin"
# model_id = "../models/ggml-model-q4_0.bin"
n_ctx = 32784
local_logging = False # should be False in prod env
logging_endpoint = 'http://localhost:8888' # should be default PersonaChat logging endpoint in prod env

# Initialize the Llama model
llm = Llama(model_path=model_id, verbose=False, n_ctx=n_ctx)

@app.route('/')
def index():
    return 'API ERROR'

@app.route('/inference', methods=['POST'])
def inference():
    prompt = request.json['prompt']
    output = llm(prompt, max_tokens=1024, echo=False, stop=['###', '* * *', '[Message]', 'Human:', 'Bot:'])
    response = {'bot_response': output['choices'][0]['text'].strip()}
    return jsonify(response)
if __name__ == '__main__':
    app.run()
