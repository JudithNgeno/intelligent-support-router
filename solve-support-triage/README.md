# Solve Intelligence - Automated Support Triage Engine (Heuristic Prototype)

This repository contains a local, rule-based heuristic prototype designed to automate inbound support ticket classification for Solve Intelligence. 

### The Problem This Solves

As Solve scales across 600+ global IP teams, complex technical tickets from demanding patent attorneys can bleed onto the desks of core AI engineers and attorneys, disrupting product focus. This system intercepts, parses, and formats incoming tickets to route them with complete operational context automatically.

### Architecture Overview

- **Language:** Python
- **Format:** Structured JSON outputs for seamless backend integration.
- **Routing Profiles:** Matches domain keywords (e.g., *stack traces* vs *USPTO compliance*) to partition engineering issues from high-touch legal and account queries instantly.

### Next Steps and Scaling

If I were running this in production at Solve, the next phase would be replacing the basic hardcoded string matching with a lightweight LLM classification call (like using the `openai` Python SDK with `gpt-4o-mini`). 

To make it production-ready, I would:

1. Wrap this script into a fast API endpoint using FastAPI.
2. Force the LLM to output a strict JSON structure using structural formatting flags so it doesn't break our routing pipeline.
3. Hook it directly into a Slack Webhook so that tickets matching "AI_ENGINEERING" instantly ping the engineering triage channel with the auto-generated context summary.