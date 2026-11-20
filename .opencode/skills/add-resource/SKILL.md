---
name: add-resource
description: Adds a new resource (e.g. customers, bikes, parts, rentals) to the Flask API with list, get, create and update endpoints. Use when the user wants to track or manage a new kind of thing.
---
1. Read docs/api-conventions.md. If the resource involves repairs, statuses, prices or phone numbers, also read docs/business-rules.md.
2. Copy references/blueprint-template.py to app/routes/RESOURCES.py (plural, lowercase) and replace RESOURCE and RESOURCES everywhere.
3. Fill in the validation comments using the rules you read.
4. Add `RESOURCES = {}` for the new resource to app/store.py.
5. Register the blueprint in create_app() in app/__init__.py.
6. Run `flask --app app run` and check that it starts without errors.
7. Report back briefly: only the files you changed.
