# API conventions
Wout's counter page reads these responses. Do not deviate.

- URLs: plural, lowercase, no trailing slash: `/customers`, `/repairs`.
- Repairs are looked up by slip number, not by an internal id.
- Success: 200 for reading or changing, 201 for creating. The body is the object itself as JSON.
- Errors: always JSON `{"error": "message"}`. 400 for bad input, 404 when something does not exist.
- Flask returns an HTML page for unknown routes by default. `create_app()` in app/__init__.py must register JSON error handlers for 400 and 404.
- Dates: `YYYY-MM-DD`, nothing else.
- Money: whole number of cents. 34,50 euro = `3450`. Never floats.
- The app runs on port 5000.
