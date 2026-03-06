import os
import json

from extract_llm import extract_account_data
from agent_generator import generate_agent

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

DEMO_PATH = os.path.join(BASE_PATH, "dataset", "demo_calls")
OUTPUT_PATH = os.path.join(BASE_PATH, "outputs", "accounts")


def run_demo_pipeline():

    for file in os.listdir(DEMO_PATH):

        if not file.endswith(".txt"):
            continue

        transcript_path = os.path.join(DEMO_PATH, file)

        transcript = open(transcript_path).read()

        account_id = file.split(".")[0]

        print(f"Processing {account_id}")

        memo = extract_account_data(transcript, account_id)

        agent = generate_agent(memo, "v1")

        account_path = os.path.join(OUTPUT_PATH, account_id, "v1")

        os.makedirs(account_path, exist_ok=True)

        memo_file = os.path.join(account_path, "memo.json")
        agent_file = os.path.join(account_path, "agent_spec.json")

        with open(memo_file, "w") as f:
            json.dump(memo, f, indent=2)

        with open(agent_file, "w") as f:
            json.dump(agent, f, indent=2)

        print(f"Saved outputs for {account_id}")


if __name__ == "__main__":
    run_demo_pipeline()