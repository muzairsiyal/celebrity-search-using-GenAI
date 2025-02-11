import os
from flask import Flask, render_template, request, jsonify
from langchain_community.llms import Cohere
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import SequentialChain

# Initialize Flask app
app = Flask(__name__)

# Set up Cohere API Key
os.environ["COHERE_API_KEY"] = "QvWdawj2acJPV5shE2hPayreoU9i0ncEykMXbyEQ"

# Define Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born?"
)

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events that happened around {dob} in the world"
)

# Define Memory Buffers
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# Initialize LLM
llm = Cohere(model="command", temperature=0.8)

# Define Chains
chain = LLMChain(llm=llm, prompt=first_input_prompt, output_key='person', memory=person_memory)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, output_key='dob', memory=dob_memory)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, output_key='description', memory=descr_memory)

parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'description']
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'No name provided'}), 400

    result = parent_chain({'name': name})
    
    return jsonify({
        'person': result['person'],
        'dob': result['dob'],
        'description': result['description']
    })

if __name__ == '__main__':
    app.run(debug=True)
