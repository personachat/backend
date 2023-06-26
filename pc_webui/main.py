from flask import Flask, request, render_template, jsonify
import hashlib
import os
from llama_cpp import Llama
import yaml
import requests

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
    return render_template('index.html')

@app.route('/inference', methods=['POST'])
def inference():
    prompt = request.json['prompt']
    output = llm(prompt, max_tokens=1024, echo=False, stop=['###', '* * *', '[Message]', 'Human:', 'Bot:'])
    response = {'bot_response': output['choices'][0]['text'].strip()}
    return jsonify(response)

@app.route('/vote', methods=['POST'])
def vote():
    prompt = request.json['prompt'].strip().removesuffix('### Human:').removesuffix('### Bot:').strip()
    if local_logging:
        if not os.path.exists('votes'):
            os.mkdir('votes')
        prompthash = str(hashlib.md5(prompt.encode('utf-8')).hexdigest()) # not only does md5 hash generate a unique filename, but it also removes duplicates
        with open('votes/' + prompthash + '.txt', 'w') as f:
            f.write(prompt)
        response = {'success': True}
    else:
        response = {'success': int(requests.post(logging_endpoint, data={'log': prompt}).status_code) == 200}
    return jsonify(response)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
