import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT = """
Extract structured information from this service company call transcript.

Return ONLY JSON using this schema:

{
"account_id":"",
"company_name":"",
"business_hours":{"days":[],"start":"","end":"","timezone":""},
"office_address":"",
"services_supported":[],
"emergency_definition":[],
"emergency_routing_rules":"",
"non_emergency_routing_rules":"",
"call_transfer_rules":"",
"integration_constraints":"",
"after_hours_flow_summary":"",
"office_hours_flow_summary":"",
"questions_or_unknowns":[],
"notes":""
}

Transcript:
"""

def extract_account_data(transcript, account_id):

    payload = {
        "model": "llama3",
        "prompt": PROMPT + transcript,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    text = response.json()["response"]

    # remove markdown code blocks if present
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    # extract JSON portion
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        json_text = match.group()
    else:
        raise ValueError("No JSON found in model output")

    data = json.loads(json_text)

    data["account_id"] = account_id

    return data