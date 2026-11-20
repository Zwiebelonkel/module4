# Client Report Part A: Statements from the interview and the email

| Statement | Source | Group | Goes into |
|---|---|---|---|
| Today a repair is a paper slip with the customer's name and phone number, plus what is wrong | Interview | Rule | docs/business-rules.md (customers) |
| The slip gets a number, SP plus four digits (SP-0001, SP-0002, …); customers call and say the number, so the number is the search key | Interview | Rule | docs/api-conventions.md (repairs are looked up by slip number) |
| Slip statuses, exactly in Dutch: ontvangen, in herstelling, klaar, opgehaald | Interview | Rule | docs/business-rules.md (repair statuses) |
| A slip only goes forward: ontvangen → in herstelling → klaar → opgehaald | Interview | Rule | docs/business-rules.md (allowed status changes) |
| A finished bike can come back the next day because of squeaking brakes, but then a new slip is made: a slip does not go back otherwise | Interview | Rule | docs/business-rules.md (allowed status changes) |
| A repair without a price can never be klaar; reject with 400 | Interview | Rule | docs/business-rules.md (prices) |
| Prices are written in euros like 34,50, never stored as a decimal number: use cents, 34,50 euro = 3450 | Interview + Wout's note (email) | Rule | docs/api-conventions.md (money), notes/decisions.md (why: Wout's advice about rounding) |
| Only Jan may change a price; customers argue with Els, never with Jan | Interview + Wout's note (email) | Decision | notes/decisions.md (opens: how the API recognises Jan) |
| Customer data (names, phone numbers) must not go to the internet; run the AI on their own machine | Interview + Wout's note (email) | Decision | AGENTS.md (Never: no customer data logged) |
| Errors must come back as JSON with one field `error`, otherwise Wout's counter page shows nothing | Email | Rule | docs/api-conventions.md (errors) |
| Success: 200 for reading or changing, 201 for creating; return the object itself as JSON | Email | Rule | docs/api-conventions.md (success) |
| Dates are YYYY-MM-DD, nothing else; the counter page can't handle other formats | Email | Rule | docs/api-conventions.md (dates) |
| URLs are plural and lowercase: /customers, /repairs; no trailing slash | Email | Rule | docs/api-conventions.md (URLs) |
| Money in cents, as whole numbers: 34,50 euro = 3450. Never floats | Email | Rule | docs/api-conventions.md (money) |
| The app runs on http://localhost:5000, keep Flask on its default port | Email | Decision | AGENTS.md (Commands: port must stay 5000) |
| Data is stored in memory (app/store.py); Wout said start simple, a real database later; it only runs on the laptop at the counter | Interview + Wout's note (email) | Decision | notes/decisions.md |
| No login: just Els and Jan in the shop; no login endpoint in the brief | Interview + Wout's note (email) | Decision | notes/decisions.md; opens: how the API recognises Jan |
| Customers: a customer needs a name and a phone number; without a phone number nothing is saved (400) | Email + Interview ("a customer needs a name and a phone number") | Rule | docs/business-rules.md (customers) |
| Both 0471 23 45 67 and +32 471 23 45 67 are fine, as long as there is one | Email | Rule | docs/business-rules.md (customers: both formats fine) |
| A customer can have several bikes | Interview | Rule | docs/business-rules.md (customers) |
| Systems to build: customers, their bikes, the parts used on repairs, later e-bikes; for each: list, look one up, add one, change one | Interview | Repeating job | skill add-resource |
| Ask someone to check the work (tests); Wout wants tests so the page does not break on every change | Email | Repeating job | (left out in this task) |
| Errors for 400 bad input, 404 when something does not exist | Email | Rule | docs/api-conventions.md (errors) |
| Flipping an email change: the slip number now includes the year, SP-2026-0001, starting again on 1 January each year (from SP-2027-0001) | Email | Decision | not in decisions.md by instruction; goes into docs/business-rules.md? no — opens: slip number format |
| The email adds the stage wacht op onderdelen for when Jan waits for a part to be delivered; when the part arrives it goes back to in herstelling | Email | Rule | docs/business-rules.md (repair statuses); the back-change wacht op onderdelen → in herstelling is added by the email |

## Open questions for Els

1. Slip numbers: is the year taken from the creation date, what happens beyond 9999 per year, and must old paper slips (SP-0001 and so on, without a year) be migrated?
2. Phone numbers: only check that one exists, or also validate the format, and store them as typed or normalised?
3. A repair only goes forward, but the email says wacht op onderdelen can go back to in herstelling: is that the only exception, and which statuses may lead to wacht op onderdelen?
4. Only Jan may change a price, but there is no login: how should the API recognise Jan?
5. Does a price of 0 euro count as "has a price", and when is the price first entered?
6. Data is only in memory, so it is lost when the laptop restarts: is that acceptable?
7. Are addresses required, and are there deliveries?
8. Should the API record payment ("opgehaald" means picked up and paid) or only the status?
