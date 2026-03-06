import json
from extract_llm import extract_account_data

file = open("dataset/demo_calls/demo1.txt").read()

data = extract_account_data(file, "demo1")

print(json.dumps(data, indent=2))