import sys
import os
sys.path.append(os.path.dirname(__file__))

import json

from extract_onboarding import extract_updates
from patch_engine import apply_patch
from agent_generator import generate_agent
from diff_engine import generate_diff, write_changelog

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

ONBOARD_PATH = os.path.join(BASE_PATH,"dataset","onboarding_calls")
OUTPUT_PATH = os.path.join(BASE_PATH,"outputs","accounts")


def run_onboarding():

    for file in os.listdir(ONBOARD_PATH):

        if not file.endswith(".txt"):
            continue

        account_id = file.split(".")[0]

        transcript = open(os.path.join(ONBOARD_PATH,file)).read()

        updates = extract_updates(transcript)

        v1_memo_path = os.path.join(
            OUTPUT_PATH,account_id,"v1","memo.json"
        )

        if not os.path.exists(v1_memo_path):

            print(f"Skipping {account_id} (no v1 found)")
            continue

        old_memo = json.load(open(v1_memo_path))

        new_memo = apply_patch(old_memo,updates)

        agent = generate_agent(new_memo,"v2")

        v2_path = os.path.join(OUTPUT_PATH,account_id,"v2")

        os.makedirs(v2_path,exist_ok=True)

        json.dump(new_memo,
                  open(os.path.join(v2_path,"memo.json"),"w"),
                  indent=2)

        json.dump(agent,
                  open(os.path.join(v2_path,"agent_spec.json"),"w"),
                  indent=2)

        changes = generate_diff(old_memo,new_memo)

        changelog_path = os.path.join(
            OUTPUT_PATH,account_id,"changelog.md"
        )

        write_changelog(changelog_path,changes)

        print(f"Updated {account_id} → v2")


if __name__ == "__main__":

    run_onboarding()