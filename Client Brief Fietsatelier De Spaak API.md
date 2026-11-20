# Client Brief: Fietsatelier De Spaak API

## About this brief

Your client is Els Peeters, owner of Fietsatelier De Spaak, a small bicycle repair shop. She wants a Flask API so her repair jobs stop living on paper slips. The shop and the people in it are fictional.

This brief is the starting point for Module 4, Task 3. It contains two things: the transcript of a first interview, and an email Els sent the day after.

Read both carefully before you open OpenCode. Not everything Els says is a feature request:

- Some things are **rules** that every endpoint must follow.
- Some things are **decisions** that the agent must still know next week.
- Some things are **jobs that will repeat** many times.
- Some things are **worries** about quality that someone should check.

Sorting her words into these four groups is part of the task. Where Els contradicts herself or leaves something open, write it down as an open question. Do not let the agent guess.

## Interview transcript

Recorded in the workshop on a Monday morning. **You** are the developer, **Els** is the client.

**You:** Thanks for making time. Can you tell me how a repair works today?

**Els:** Someone walks in with a bike. I write their name and phone number on a paper slip, plus what's wrong. The slip gets a number, and I hang a label with that number on the handlebar. Then the bike goes in the queue for Jan, my mechanic.

**You:** What does that number look like?

**Els:** SP and then four digits. SP-0001, SP-0002 and so on. SP for Spaak. Customers call and say "I'm SP-0347", so the number has to be the thing you search on. Not some long code.

**You:** And what happens to the slip after that?

**Els:** It moves through the stages. *Ontvangen* when it comes in, *in herstelling* when Jan is working on it, *klaar* when it's done, and *opgehaald* when the customer has picked it up and paid. Those words, in Dutch. My customers are from here, and the screen at the counter shows them.

**You:** Can a repair go back a step?

**Els:** No. Well, once Jan put a bike on *klaar* and the customer came back the next day because the brakes still squeaked. But then I just make a new slip. A slip only goes forward.

**You:** What goes wrong with the paper system?

**Els:** Slips get lost. And prices. Jan sometimes forgets to write the final price, so a bike is *klaar* but nobody knows what to charge. That can never happen again. If there's no price, it's not *klaar*.

**You:** How do you write prices now?

**Els:** In euros, like 34,50. My nephew Wout looked at an earlier attempt last year and said you should never store money as a decimal number in software. Something about rounding. He said to use cents. I don't understand it, but he's studying IT, so I trust him.

**You:** Wout made an earlier version?

**Els:** He started one. It's a little web page for the counter, it still works. He says whatever you build, errors have to come back as JSON with one field called `error` in it, otherwise his page shows nothing. I'll ask him to send you the details.

**You:** Besides repairs, what else should the system know?

**Els:** The customers, obviously. And their bikes, because some people bring three bikes, one for each kid. And the parts we use on a repair: a tire, a chain, brake pads. Later, maybe in spring, I want to rent out e-bikes too. So there will be more things to add. Every time it's the same: I want to see a list, look one up, add one, change one.

**You:** Where should the data be stored?

**Els:** I don't care, as long as it works. It only runs on the laptop at the counter for now. Wout said start simple and you can add a real database later.

**You:** Does anyone need to log in?

**Els:** No, it's just us two in the shop. Oh, but only Jan is allowed to change a price. Customers argue with me about prices, never with Jan.

**You:** Is there anything you're worried about?

**Els:** Customer data. Phone numbers, names, addresses for deliveries. I read about these AI tools sending everything to some server in America. I don't want my customers' phone numbers on the internet. Can you build this without that?

**You:** We can run the AI model on our own machine for that.

**Els:** Good. And please make sure someone checks the work. The last time someone "just quickly built something" for me, it let you save a repair without a phone number. Then I had a bike for four months and no way to call the owner.

## Follow-up email from Els

**From:** Els Peeters **Subject:** Re: the repair system + Wout's notes

Hi,

Thanks for yesterday. Two things I forgot, and Wout's notes are at the bottom.

1. The slip numbers. I talked to my accountant, and she wants the year in the number. So SP-2026-0001, and on 1 January it starts again at SP-2027-0001. Sorry, I know I said four digits.
2. We need one more stage: *wacht op onderdelen*, for when Jan is waiting for a part to be delivered. When the part arrives, it goes back to *in herstelling*.

Also, phone numbers. Some customers give 0471 23 45 67, others +32 471 23 45 67. Both are fine, as long as there is one.

Greetings, Els

> **Forwarded notes from Wout**
>
> - Errors: always JSON like `{"error": "message"}`. Use 400 for bad input and 404 when something doesn't exist. My page only reads the `error` field.
> - Success: 200 for reading or changing, 201 for creating. Return the object itself as JSON.
> - Dates: `YYYY-MM-DD`, nothing else, my page can't handle other formats.
> - URLs in plural and lowercase: `/customers`, `/repairs`. No slash at the end.
> - Money in cents, as whole numbers. 34,50 euro = `3450`.
> - Please write tests, I don't want my page to break every time you change something.
> - My page runs on `http://localhost:5000`, so keep Flask on its default port.
