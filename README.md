<div align="center">
    <img src="https://huggingface.co/datasets/llama-research/assets/resolve/main/llama.png" width="250">
    <h1>PersonaChat</h1>
    <h2>Introduction</h2>
    <p>PersonaChat allows you to easily create chatbots with customized personalities.</p>
    <p>Although PersonaChat is powered by LLMs (Large Language Models), it can be run on consumer hardware using quantization.</p>
    <h2>Get Started</h2>
    <p>To start, please download and extract the models.</p>
    <p>We have multiple model mirrors:</p>
    <ul>
        <li><a href="https://github.com/fakerybakery/o7b-rscs/releases">GitHub</a> - Latest &amp; fastest, but files are split with <a href="https://github.com/fakerybakery/simplesplit">SimpleSplit</a>. Download the free SimpleSplit program to merge it.</li>
        <li><a href="https://huggingface.co/llama-research/openllama-7b-ggml/blob/main/models.7z">Hugging Face</a> - Updated less regularly &amp; slower, but files are combined.</li>
    </ul>
    <p>Next, please run the following commands:</p>
    <pre>python3 -m pip install -r requirements.txt</pre>
    <pre>python3 main.py</pre>
    <p>You'll be asked for a personality profile and your name. To chat with the default bot (friendly and smart), enter <code>friend</code> or <code>friend.yaml</code>. You can also customize the bots by adding a <code>yaml</code> file to the <code>personas</code> directory.</p>
    <h2>Features</h2>
    <p>TODO: Summary of WebUI</p>
    <h2>Variants</h2>
    <h3>Helper</h3>
    <p>We have an virtual assistant-like bot somewhat like what's on many mobile devices. This system aims to provide access to actions, such as searching contacts and sending messages.</p>
    <p>This version is not ready for production yet, and access to APIs has not been completed. Quality is also extremely poor.</p>
    <p>Use at your own risk.</p>
    <p>The file is in <code>helper.py</code>.</p>
    <h2>Disclaimer</h2>
    <p>PersonaChat is an AI-powered product developed to simulate conversations and engage in interactive dialogues. It is important to note that due to the nature of machine learning algorithms, PersonaChat may occasionally generate offensive, inappropriate, or incorrect content. The generated responses do not reflect the opinions, beliefs, or endorsements of the creators or developers of PersonaChat.</p>
    <p>While extensive efforts have been made to train and fine-tune PersonaChat to provide useful and respectful conversations, there are inherent limitations in language models that may result in unexpected outcomes. The AI system learns from a diverse range of text sources and attempts to generate responses based on patterns and examples found in the training data. However, it is impossible to guarantee that every generated response will be accurate, up-to-date, or free from biases.</p>
    <p>Users of PersonaChat are encouraged to exercise caution and use their discretion when engaging with the AI-generated content. The creators of PersonaChat cannot be held responsible for any offense, misinformation, or harm caused by the AI-generated responses. It is advisable to independently verify any information obtained from PersonaChat and to consider alternative perspectives.</p>
</div>