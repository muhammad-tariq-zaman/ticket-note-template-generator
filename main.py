"""Render a standard helpdesk ticket note from a JSON ticket.

Usage: python3 main.py ticket.json
JSON fields: ticket, category, summary, agent.
Each known category gets its own next-step line; an unknown
category falls back to a generic follow-up line. The note is
plain text, ready to paste into the ticket.
"""
import argparse, json, sys

NEXT_STEPS = {
    "password-reset": "Next step: confirm the user can sign in, then close the ticket.",
    "network": "Next step: re-test connectivity after the fix and record the result.",
    "printer": "Next step: print a test page and confirm output quality with the user.",
    "software": "Next step: verify the application opens and the reported error is gone.",
    "access": "Next step: confirm the access works for the user, then close the ticket.",
}
GENERIC_STEP = "Next step: follow up with the requester to confirm the fix."

def render_note(ticket):
    category = str(ticket.get("category", "general")).strip().lower()
    step = NEXT_STEPS.get(category, GENERIC_STEP)
    lines = [
        f"Ticket {ticket['ticket']} [{category}]",
        f"Summary: {ticket['summary']}",
        f"Handled by: {ticket['agent']}",
        step,
    ]
    return "\n".join(lines)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, encoding="utf-8") as f:
        print(render_note(json.load(f)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
