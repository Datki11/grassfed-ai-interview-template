# Support Ticket Overview

You're joining a small team that builds an internal support tool. Customers raise **tickets**. Each ticket has a priority (P1 is the most urgent), a status, an optional assignee, how many hours it has been open, and whether support has replied yet. See `Ticket.cs` and `SampleTickets.cs`.

The interview has three parts. Your interviewer will tell you when to move on. **It's fine not to finish everything.** We're interested in how you think and how you check your work.

Click **Run** at any time to see which checks pass.

---

## Part 1: Write two small functions (no AI, about 10 minutes)

Open `TicketStats.cs` and write the body of each function. The comment above each one explains what it should return.

Please **don't use the AI assistant** for this part. Documentation and search engines are fine. Afterwards we'll ask you to walk us through your code.

---

## Part 2: Build a feature (AI assistant allowed, about 20 minutes)

Support leads want a report of tickets that are **overdue for a first reply**.

Write both functions in `Overdue.cs`.

### `FindOverdueTickets(tickets)`
Returns every ticket that:
- is **not closed**,
- has **not been responded to**, and
- has been open **longer than** its priority allows:

| Priority | Hours allowed before the first reply |
| --- | --- |
| P1 | 4 |
| P2 | 24 |
| P3 | 72 |

Order the results by priority (P1, then P2, then P3). Within the same priority, the ticket that has been open **longest comes first**.

### `FormatReport(overdue)`
Returns one line per overdue ticket, in the same order:

```
P1 #9 Payment page error - 3h overdue (sam)
```

- "Hours overdue" is the hours open minus the hours allowed.
- Show `(unassigned)` when the ticket has no assignee.
- If there are no overdue tickets, return a single line: `No overdue tickets.`

### How you'll be assessed in this part
- How you **plan** the work and **direct** the AI assistant.
- How you **check** what it produces. Only two checks are provided, so adding your own in `Checks.cs` is encouraged.
- Whether you can **explain** the final code.

Before you start, take a minute to ask any questions and outline your approach.

---

## Part 3: A change (about 10 minutes)

Your interviewer will give you a follow-up requirement.
