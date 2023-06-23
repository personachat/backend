from flask import Flask, request, render_template, jsonify
import os
from llama_cpp import Llama
import yaml

app = Flask(__name__)
# model_id = "../models/ggml-model-q4_1.bin"
model_id = "../models/ggml-model-q3_K_L.bin"
n_ctx = 32784

# Initialize the Llama model
llm = Llama(model_path=model_id, verbose=False, n_ctx=n_ctx)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inference', methods=['POST'])
def inference():
    prompt = request.json['prompt']
    output = llm(prompt, max_tokens=1024, echo=False, stop=['###', '* * *', '[Message]'])
    response = {'bot_response': output['choices'][0]['text'].strip()}
    return jsonify(response)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
