from config.env import * 
from base_agent import CourtroomAgent
import random
from typing import List, Tuple


# === Witness Logic ===

def run_witness_agent(context: str, index: int) -> Tuple[str, str]:
    client = Groq(api_key=key)
    prompt = f"""You are a fictional courtroom witness.

Based on the case below, invent a realistic identity and write a testimony.

### Case:
{context}

### Instructions:
- Introduce yourself clearly. Start your testimony with your full name and your job.
- Give your testimony in first person.
- Be truthful, personal, and avoid legal jargon (unless fitting).
- No speculation—stick to what you directly know.
"""

    result = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=512
    ).choices[0].message.content.strip()

    name = "WITNESS"

    for line in result.splitlines():
        if "My name is" in line:
            try:
                # Extract portion after "My name is " and before the comma
                name = line.split("My name is")[1].split(",")[0].strip()
                break
            except IndexError:
                continue

    return name, result


def run_dynamic_witness_qa(witness_name: str, case: str, agents: list[CourtroomAgent], witness_intro: str, num_questions):
     print(f"\n--- Witness {witness_name} takes the stand ---\n")
     print(witness_name.upper(), ":\n", witness_intro)
     asked_agents = []
     available_agents = [agent for agent in agents]

     for i in range(num_questions):
        if not available_agents:
            available_agents = [agent for agent in agents]

        asker = random.choice(available_agents)
        available_agents.remove(asker)
        asked_agents.append(asker.name)

        question = f"\nAsk witness {witness_name} one relevantly related to its profession, respectful question based on the case context: {case}"
        print(f"{asker.name.upper()} (Q{i+1}):", asker.respond(question))

        response_prompt = f"\nYou are {witness_name}. Answer the following question truthfully and respectfully and you are not allowed to counter question: {question}"
        print(f"{witness_name} (A{i+1}):", asker.respond(response_prompt))

       
     print(f"\n\n[Q&A Session Completed – {witness_name} was questioned by: {', '.join(set(asked_agents))}]")



def run_witness_reply(witness_name: str, case_context: str, question: str) -> str:
    client = Groq(api_key=key)
    prompt = f"""
You are a courtroom witness named {witness_name}. Answer the following question based on your personal knowledge and the case context.
And you are not allowed to counter question the agents.
### Case:
{case_context}

### Question:
{question}

### Instructions:
- Answer in first person.
- Be consistent with what you have previously said. Do not contradict your earlier testimony.
- If your memory is unclear, say so instead of guessing.
- Be realistic and stay within the facts you know.
- No speculation or legal talk.
"""

    result = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=126
    ).choices[0].message.content.strip()
    return result
