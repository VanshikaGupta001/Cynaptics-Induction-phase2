import gradio as gr
from config.utils import load_case
from trial import *
import io
import sys

def simulate_case(case_no):
    case = load_case(case_no)
    if not case:
        return "Case not found..."

    buffer = io.StringIO()
    sys.stdout = buffer
    graph = build_trial_graph(case)
    initial_state = {"case": case}
    final_state = graph.invoke(initial_state)
    
    sys.stdout = sys.__stdout__

    return buffer.getvalue()

iface = gr.Interface(
    fn=simulate_case,
    inputs=gr.Textbox(label="Enter Case Number"),
    outputs=gr.Textbox(label="Simulation Result", lines=20),
    title="AGENTS OF JUSTICE",
    description="Enter a case number to simulate a courtroom trial."
)

if __name__ == "__main__":
    iface.launch(share=True)