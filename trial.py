from __future__ import annotations
from langgraph.graph import StateGraph, END
from pydantic import BaseModel
from agents.witness import *
from config.prompts import *

# === LangGraph Schema ===
class TrialState(BaseModel):
    case: str
    phase: str = "opening"


# === Graph Building ===
def build_trial_graph(case_background: str):
    defense = CourtroomAgent("Defense", DEFENSE_SYSTEM)
    prosecution = CourtroomAgent("Prosecution", PROSECUTION_SYSTEM)
    judge = CourtroomAgent("Judge", JUDGE_SYSTEM)
    plaintiff = CourtroomAgent("Plaintiff", PLAINTIFF_SYSTEM)
    defendant = CourtroomAgent("Defendant", DEFENDANT_SYSTEM)

    agents = [defense, prosecution, judge, defendant] 

    def opening(state: TrialState) -> TrialState:
        print("\n==== Opening Statements ====")
        print("PROSECUTION:", prosecution.respond(f"Opening statement to the Court. Background: {state.case}"))
        print("DEFENSE:", defense.respond("Opening statement to the Court responding to the prosecution."))
        return state.copy(update={"phase": "argument"})

    def argument(state: TrialState) -> TrialState:
        print("\n==== Argumentation Phase ====")
        print("PLAINTIFF:", plaintiff.respond("Explain your experience and view of the incident."))

        num_witnesses = random.randint(1, 3)
        last_speaker_idx = -1

        for i in range(num_witnesses):
            introducer_idx = (last_speaker_idx + 1) % len(agents)
            introducer = agents[introducer_idx]
            name, intro = run_witness_agent(state.case, i)

            print(f"{introducer.name.upper()} (introducing witness):", introducer.respond(f"I would now like to call {name} to the stand."))
            run_dynamic_witness_qa(name, state.case, agents, intro, num_questions=random.randint(1,3) )

            last_speaker_idx = introducer_idx

        print("DEFENDANT:", defendant.respond("Respond to the plaintiff's and witness statements and defend your position."))
        print("PROSECUTION:", prosecution.respond("Present further arguments and address the defense's points."))
        print("DEFENSE:", defense.respond("Present your defense and counter the prosecution's claims."))
        return state.copy(update={"phase": "closing"})

    def closing(state: TrialState) -> TrialState:
        print("\n==== Closing Statements ====")
        print("PROSECUTION:", prosecution.respond("Give your closing argument summarizing the State's position."))
        print("DEFENSE:", defense.respond("Give your closing statement defending your client."))
        return state.copy(update={"phase": "verdict"})

    def verdict(state: TrialState) -> TrialState:
        print("\n==== Judge's Verdict ====")
        print("JUDGE:", judge.respond("Summarize the case, evaluate both sides and deliver a final verdict."))
        return state

    graph = StateGraph(state_schema=TrialState)
    graph.add_node("opening", opening)
    graph.add_node("argument", argument)
    graph.add_node("closing", closing)
    graph.add_node("verdict", verdict)

    graph.set_entry_point("opening")
    graph.add_edge("opening", "argument")
    graph.add_edge("argument", "closing")
    graph.add_edge("closing", "verdict")
    graph.add_edge("verdict", END)

    return graph.compile()

