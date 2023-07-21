Further development has been [moved to Codeberg](https://codeberg.org/personachat/backend).

<div align="center">
    <h1>PersonaChat</h1>
    <h2>Notice</h2>
    <p>PersonaChat is still in beta and should not be used in production. If you like this project or want further development, <b>please star this repository.</b> The authors of this project also work on many other projects, so stars will prompt us to continue working on this project.</p>
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
    <p>Coming soon!</p>
    <h2>WebUI</h2>
    <h3>Old webUI</h3>
    <p>This webUI is old and deprecated. Please see the new webUI <a href="https://github.com/personachat/webui">in this repository</a>.</p>
    <p>If you just want to try PersonaChat and don't care about new features, feel free to use our old webUI! Please note that the prompts may not be updated as often, so the quality may be lower than otherwise expected. The old UI only supports the default (<code>friend</code>) persona, but we're working on adding more!</p>
    <p>To try it out, please run the following commands:</p>
    <pre>cd pc_webui</pre>
    <pre>python3 main.py</pre>
    <h3><a href="https://github.com/personachat/webui" target="_blank">New webUI</a></h3>
    <h2>Variants</h2>
    <h3>Helper</h3>
    <p>We have an virtual assistant-like bot somewhat like what's on many mobile devices. This system aims to provide access to actions, such as searching contacts and sending messages.</p>
    <p>This version is not ready for production yet, and access to APIs has not been completed. Quality is also extremely poor.</p>
    <p>Use at your own risk.</p>
    <p>The file is in <code>helper.py</code>.</p>
    <h2>Important</h2>
    <p>Please note that by interacting with PersonaChat, your conversations may be logged and added to our dataset, which may be published publicly.</p>
    <h2>Disclaimer</h2>
    <p>PersonaChat is an AI-powered product developed to simulate conversations and engage in interactive dialogues. It is important to note that due to the nature of machine learning algorithms, PersonaChat may occasionally generate offensive, inappropriate, or incorrect content. The generated responses do not reflect the opinions, beliefs, or endorsements of the creators or developers of PersonaChat.</p>
    <p>While extensive efforts have been made to train and fine-tune PersonaChat to provide useful and respectful conversations, there are inherent limitations in language models that may result in unexpected outcomes. The AI system learns from a diverse range of text sources and attempts to generate responses based on patterns and examples found in the training data. However, it is impossible to guarantee that every generated response will be accurate, up-to-date, or free from biases.</p>
    <p>Users of PersonaChat are encouraged to exercise caution and use their discretion when engaging with the AI-generated content. The creators of PersonaChat cannot be held responsible for any offense, misinformation, or harm caused by the AI-generated responses. It is advisable to independently verify any information obtained from PersonaChat and to consider alternative perspectives.</p>
</div>
