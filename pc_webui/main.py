from flask import Flask, request, render_template, jsonify
import hashlib
import os
from llama_cpp import Llama
import yaml

app = Flask(__name__)
model_id = "../models/ggml-model-q4_1.bin"
# model_id = "../models/open-llama-13b-q4_0.bin"
# model_id = "../models/ggml-model-q4_0.bin"
n_ctx = 32784

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
    prompt = request.json['prompt']
    if not os.path.exists('votes'):
        os.mkdir('votes')
    prompthash = hashlib.md5(prompt.encode('utf-8'))
    with open(prompthash + '.txt', 'w') as f:
        f.write(prompt)
    response = {'success': True}
    return jsonify(response)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
