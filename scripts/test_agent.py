import sys
sys.path.append("scripts")

import json
from extract_llm import extract_account_data
from agent_generator import generate_agent

transcript = open("dataset/demo_calls/demo1.txt").read()

memo = extract_account_data(transcript,"demo1")

agent = generate_agent(memo,"v1")

print(json.dumps(agent,indent=2))