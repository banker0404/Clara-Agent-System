def build_prompt(memo):

    company = memo.get("company_name","the company")

    return f"""
You are the AI phone assistant for {company}.

BUSINESS HOURS FLOW
1 greet caller politely
2 ask the purpose of the call
3 collect caller name and phone number
4 route or transfer call
5 if transfer fails apologize and promise follow up
6 ask if caller needs anything else
7 close call politely

AFTER HOURS FLOW
1 greet caller
2 determine if the call is an emergency
3 if emergency collect name phone and address immediately
4 attempt transfer to on call technician
5 if transfer fails reassure caller and promise urgent follow up
6 if non emergency collect details
7 confirm follow up during business hours
"""


def generate_agent(memo, version):

    return {
        "agent_name": f"{memo.get('company_name','Company')} Assistant",
        "version": version,
        "voice_style": "professional",
        "system_prompt": build_prompt(memo),
        "variables": {
            "business_hours": memo.get("business_hours"),
            "timezone": memo.get("business_hours",{}).get("timezone",""),
            "office_address": memo.get("office_address","")
        },
        "call_transfer_protocol": memo.get("call_transfer_rules",""),
        "fallback_protocol":
        "If transfer fails notify dispatch and reassure caller"
    }