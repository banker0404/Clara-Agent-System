# Clara Agent Automation Pipeline
## Overview

This project builds an automated pipeline that converts service-business call transcripts into structured AI voice-agent configurations.

The system processes demo call transcripts to generate a preliminary Retell agent configuration (v1). After onboarding transcripts are received, the system updates the agent configuration to version v2 and produces a changelog describing the changes.

The goal is to automate the transformation of messy conversational data into structured operational rules and AI agent prompts.

## System Architecture

Demo Transcript
      ↓
LLM Extraction (Ollama + Llama3)
      ↓
Structured Account Memo JSON
      ↓
Retell Agent Draft Spec (v1)
      ↓
Stored in outputs/accounts/

Onboarding Transcript
      ↓
Extract Updates
      ↓
Patch Existing Memo
      ↓
Generate Updated Agent Spec (v2)
      ↓
Generate Changelog

## Project Structure

clara-agent-system/

dataset/
   demo_calls/
   onboarding_calls/

scripts/
   extract_llm.py
   extract_onboarding.py
   agent_generator.py
   patch_engine.py
   diff_engine.py
   run_demo_pipeline.py
   run_onboarding_pipeline.py

outputs/
   accounts/

dashboard/

workflows/

README.md


## Setup Instructions

1. Install Python

2. Install dependencies

    pip install requests streamlit

3. Install Ollama

    Download from:
    https://ollama.com

4. Pull the LLM model

    ollama pull llama3

5. Start the Ollama server

    ollama serve


## Running the Pipelines

Run the demo pipeline:

    python scripts/run_demo_pipeline.py

This generates:

outputs/accounts/<account_id>/v1/memo.json  
outputs/accounts/<account_id>/v1/agent_spec.json


Run the onboarding update pipeline:

    python scripts/run_onboarding_pipeline.py

This generates:

outputs/accounts/<account_id>/v2/memo.json  
outputs/accounts/<account_id>/v2/agent_spec.json  
outputs/accounts/<account_id>/changelog.md


## Output Structure

outputs/accounts/<account_id>/

v1/
   memo.json
   agent_spec.json

v2/
   memo.json
   agent_spec.json

changelog.md

## Limitations

- Extraction accuracy depends on transcript clarity.
- Some fields may remain empty when information is not present in the transcript.
- The system outputs a Retell agent specification rather than directly creating the agent through the Retell API.

## Future Improvements

- Integrate with the Retell API for automatic agent creation.
- Add a database for persistent account storage.
- Build a UI dashboard for managing accounts.
- Improve extraction prompts and validation logic.
