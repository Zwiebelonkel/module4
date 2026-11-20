# Fietsatelier De Spaak API

## Project
Flask JSON API for the bike repair shop De Spaak (owner: Els). Data lives in memory (app/store.py). Wout's counter page reads the responses, so the response format must not change unless asked.

## Commands
- Install: `pip install flask`
- Run: `flask --app app run` (port must stay 5000)

## Structure
- app/__init__.py: create_app(), registers blueprints and JSON error handlers
- app/store.py: holds the data in memory
- app/routes/: one blueprint file per resource

## Read only what the task needs
- Start of every session → notes/decisions.md
- New or changed endpoint → docs/api-conventions.md
- Repairs, statuses, prices or phone numbers → docs/business-rules.md
- New kind of thing to track → skill add-resource

## Memory
When the user decides how the project works, append one line to notes/decisions.md: `YYYY-MM-DD – decision – reason`. Never put customer data in that file.

## Never
- Never log, print or write customer data (names, phone numbers) anywhere, including notes.
- Never guess an unclear rule: see "Open" in docs/business-rules.md and ask.
