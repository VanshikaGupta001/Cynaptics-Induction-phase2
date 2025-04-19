from trial import build_trial_graph

# === Run Example ===

if __name__ == "__main__":
    sample_case = (
        "Jamie Smith is suing Alex Doe for damages resulting from a car accident that occurred on May 15th, 2023. "
        "Jamie claims Alex was driving under the influence and caused the crash. Alex denies the claim and states the accident was due to poor weather."
    )
    graph = build_trial_graph(sample_case)
    initial_state = {"case": sample_case}
    final_state = graph.invoke(initial_state)
