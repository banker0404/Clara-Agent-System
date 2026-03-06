import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT = """
Extract ONLY configuration updates from this onboarding transcript.

Return JSON with ONLY the fields that changed.

Example format:

{
"business_hours":{"start":"","end":"","timezone":""},
"emergency_definition":[],
"call_transfer_rules":"",
"integration_constraints":""
}

Transcript:
"""

def extract_updates(transcript):

    payload = {
        "model": "llama3",
        "prompt": PROMPT + transcript,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    text = response.json()["response"]

    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        return {}

    return json.loads(match.group())