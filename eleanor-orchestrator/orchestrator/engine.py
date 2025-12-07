from .critics import call_critic

CRITICS = {
    "rights": "eleanor-rights",
    "fairness": "eleanor-fairness",
    "risk": "eleanor-risk",
    "truth": "eleanor-truth",
    "pragmatics": "eleanor-pragmatics",
}

def run_all_critics(input_text: str) -> dict:
    outputs = {}
    for name, model in CRITICS.items():
        outputs[name] = call_critic(model, input_text)
    return outputs
