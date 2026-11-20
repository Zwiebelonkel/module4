# Business rules

## Repair statuses (exactly, in Dutch)
`ontvangen`, `in herstelling`, `wacht op onderdelen`, `klaar`, `opgehaald`

## Allowed status changes
- ontvangen → in herstelling
- in herstelling → wacht op onderdelen
- wacht op onderdelen → in herstelling (when the part arrives)
- in herstelling → klaar
- klaar → opgehaald
Any other change: 400. A slip does not go back otherwise. If a finished bike has a problem again, create a new slip.

## Prices
- A repair without a price can never be `klaar`. Reject with 400.
- Only Jan may change a price (see Open).

## Customers
- A customer needs a name and a phone number. Without a phone number, nothing is saved (400).
- Both `0471 23 45 67` and `+32 471 23 45 67` are fine.
- A customer can have several bikes.

## Open
- How the API recognises Jan (no login exists).
- Whether price 0 counts as "has a price".
- Which other status changes are allowed.
- Phone number validation and storage format.
- Whether addresses are required, and whether payments are tracked.
