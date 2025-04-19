# AGENTS OF JUSTICE
This project is an AI-driven courtroom simulation system using Groq API, LLaMA, and Gradio. This project simulates a courtroom trial with autonomous legal agents representing the Judge, Defense Lawyer and Prosecution Lawyer. Built with fast reasoning, real-time interaction, and modularity for scalability.

    # OVERVIEW
This project simulates a courtroom environment where multiple autonomous agents play roles such as the Judge, Lawyers, Defendent , Plaintiff and witness. These agents communicate and make decisions based on their individual prompts, using the Groq API to interface with the LLaMA model( llama3-8b-8192) for real-time reasoning.

    # FEATURES
1> Multi-Agent System: Independent agents for Judge, Defense Lawyer, DEfendant, Plaintiff and Prosecution Lawyer.

2> Gradio Interface: User-friendly web UI for trial initiation and interaction.

3> Groq + LLaMA Integration: Fast and efficient LLM-driven decision-making.

4> Context Retention: Agents remember prior conversations and actions that is they retain memory.

5> Customizable Prompts: Easily change agent behavior and trial flow using prompt templates.

6> Interactive Simulation: Users can observe or influence courtroom discussions.

  #  Architecture
Folder Structure
bash
Copy
Edit
courtroom-sim/
│
├── agents/                      # Contains agent logic
│   ├── base_agent.py             
│   ├── witness.py           

│
├── config/                     # Stores prompt templates for agents
│   └── prompts.py
│   └── env.py
│   └──utils.py

│
├── trial.py                       # LangGraph flow logic
├── file.py                        # To preprocess the cses.csv file into cases_meaningful_sentences.csv

│
├── app.py                      # Main entry point with Gradio UI
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation

│
├── processed_data.csv            
├── cases.csv

  Key Components:
1. Agents: Each agent is a Python module with specific behavior and prompts that simulate legal roles.
   
2.Prompts: Templates stored in prompts/ that define how each agent interacts and responds. These can be customized to suit different case scenarios.

3. API Client: Manages communication with the Groq API for inference and decision-making, based on the case data provided by agents.

   
4. Main.py: The entry point of the application. It integrates the agents, prompts, and the Gradio UI to manage real-time simulation.
   
5. LangGraph: The structured flow of the trial is managed using LangGraph, which ensures that the sequence of actions, such as presenting evidence or making arguments, follows a logical 
   order and also supports conditional flow.


  # IMPLEMENTATION
1. Clone the Repository

"git clone https://github.com/VanshikaGupta001/Cynaptics-Induction-phase2.git"


2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt


5. Add Your Groq API Key
Create a .env file and add the following:

GROQ_API_KEY=your_groq_api_key

5. Run the Application
python app.py


# Scope for Improvement
1. Witness Agent Integration:
Add functionality to introduce a witness during the trial for cross-examination, making the simulation more dynamic.

2. TTS Integration:
    Integrate speech synthesis with gradio with different for for different agents (based on gender) and emotions and tone of the speech based on the roles of the agents.

3. Extended Agent Interactions:
Implement more complex interactions, including objections, evidence presentation, and more nuanced legal dialogue.

Introduce roles for jury members, clerks, and other courtroom personnel.

4. Memory Retention & Context:
Use vector-based memory storage (like FAISS or other vector databases) to store and retrieve long-term conversation context for agents.

5. Better Case Upload/Parsing:
Allow users to upload case files (PDF, DOCX) and parse them into structured data to drive the trial simulation.

