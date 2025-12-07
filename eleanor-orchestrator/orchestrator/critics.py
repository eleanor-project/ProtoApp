import subprocess

def call_critic(model_name: str, prompt: str) -> dict:
    """Calls an Ollama model and returns parsed critic output."""
    result = subprocess.run(
        ["ollama", "run", model_name],
        input=prompt.encode(),
        capture_output=True,
        text=True,
    )
    
    output = result.stdout.strip()
    return parse_critic_output(output)

def parse_critic_output(text: str) -> dict:
    """Parses Eleanor critic structured output into a Python dict."""
    fields = {
        "Claim": "",
        "Evidence": "",
        "Constitutional Principle": "",
        "Confidence": 0.0,
        "Mitigation": "",
        "raw": text
    }
    
    for line in text.splitlines():
        if "Claim:" in line:
            fields["Claim"] = line.split(":", 1)[1].strip()
        elif "Evidence:" in line:
            fields["Evidence"] = line.split(":", 1)[1].strip()
        elif "Constitutional Principle:" in line:
            fields["Constitutional Principle"] = line.split(":", 1)[1].strip()
        elif "Confidence:" in line:
            try:
                fields["Confidence"] = float(line.split(":", 1)[1].strip())
            except:
                fields["Confidence"] = 0.0
        elif "Mitigation:" in line:
            fields["Mitigation"] = line.split(":", 1)[1].strip()
    
    return fields
