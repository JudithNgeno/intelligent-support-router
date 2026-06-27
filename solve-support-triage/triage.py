import json

class SolveSupportTriage:
    def __init__(self):
        self.routes = ["AI_ENGINEERING", "LEGAL_ATTORNEY", "GTM_SUCCESS", "TIER_1_SELF_SERVE"]

    def analyze_ticket(self, ticket_text):
        ticket_lower = ticket_text.lower()
        
        # Heuristic/Rule-based triage logic
        if "stack trace" in ticket_lower or "console error" in ticket_lower or "api latency" in ticket_lower:
            route = "AI_ENGINEERING"
            urgency = "HIGH"
            context_summary = "User experiencing frontend/backend decoupling issue or execution failure. Stack trace attached."
        elif "uspto" in ticket_lower or "patent application" in ticket_lower or "claims drafting" in ticket_lower:
            route = "LEGAL_ATTORNEY"
            urgency = "MEDIUM"
            context_summary = "Complex domain question regarding IP harvesting or litigation module formatting."
        elif "billing" in ticket_lower or "add user" in ticket_lower or "login" in ticket_lower:
            route = "TIER_1_SELF_SERVE"
            urgency = "LOW"
            context_summary = "Routine account configuration. Resolve immediately using internal Playbook Doc #4."
        else:
            route = "GTM_SUCCESS"
            urgency = "MEDIUM"
            context_summary = "General platform walk-through request from a senior partner."

        return {
            "Assigned_Team": route,
            "Urgency_Level": urgency,
            "Context_For_Team": context_summary
        }

# --- Quick Test Case ---
mock_ticket = """
Hi Support, I am a senior partner at DLA Piper. While running the patent generation module 
for our latest quantum computing claim, the UI froze, and the browser console printed a 
504 Gateway Timeout stack trace. I am short on time, please look into this.
"""

triage_system = SolveSupportTriage()
result = triage_system.analyze_ticket(mock_ticket)
print(json.dumps(result, indent=4))