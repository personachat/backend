from flask import Flask, request, render_template, jsonify
import os
import sqlite3
from llama_cpp import Llama
import yaml

app = Flask(__name__)
# model_id = "../models/ggml-model-q4_1.bin"
model_id = "../models/ggml-model-q3_K_L.bin" # K_L: higher quality K_M lower quality
n_ctx = 32784

# Initialize the Llama model
llm = Llama(model_path=model_id, verbose=False, n_ctx=n_ctx)

# Create or connect to the SQLite database
conn = sqlite3.connect('cache.db')
conn.execute('PRAGMA foreign_keys = ON')
c = conn.cursor()

# Create a table to store cached responses
c.execute('''CREATE TABLE IF NOT EXISTS cache
             (prompt TEXT PRIMARY KEY, response TEXT)''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inference', methods=['POST'])
def inference():
    prompt = request.json['prompt']

    # Check if the response is already cached
    c.execute('SELECT response FROM cache WHERE prompt = ?', (prompt,))
    cached_response = c.fetchone()

    if cached_response:
        response = {'bot_response': cached_response[0]}
    else:
        # Perform the inference if response is not cached
        output = llm(prompt, max_tokens=1024, echo=False, stop=['###', '* * *', '[Message]'])
        response_text = output['choices'][0]['text'].strip()
        response = {'bot_response': response_text}

        # Cache the response
        c.execute('INSERT OR REPLACE INTO cache (prompt, response) VALUES (?, ?)', (prompt, response_text))
        conn.commit()

    return jsonify(response)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()

# Close the database connection when the application exits
conn.close()
