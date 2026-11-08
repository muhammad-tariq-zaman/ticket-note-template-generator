# ticket-note-template-generator

Render a standard helpdesk ticket note from a JSON ticket (ticket, category, summary, agent): each known category gets its own next-step line, unknown categories fall back to a generic follow-up.

## How to run

```sh
python3 main.py ticket.json
```

## Example output

```
Ticket T-101 [network]
Summary: Wi-Fi drops every hour
Handled by: ali
Next step: re-test connectivity after the fix and record the result.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
