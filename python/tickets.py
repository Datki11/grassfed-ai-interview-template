"""Ticket data used by every part of the exercise. You shouldn't need to change this file."""
from dataclasses import dataclass
from typing import Optional

# priority: "P1" (most urgent), "P2" or "P3"
# status: "open", "waiting_on_customer" or "closed"


@dataclass(frozen=True)
class Ticket:
    id: int
    title: str
    priority: str
    status: str
    assignee: Optional[str]  # None means nobody is assigned
    hours_open: int          # whole hours since the ticket was created
    responded: bool          # True once someone from support has replied


SAMPLE_TICKETS = [
    Ticket(1, "Login page down", "P1", "open", None, 6, False),
    Ticket(2, "Slow dashboard", "P1", "open", "maya", 2, False),
    Ticket(3, "Invoice missing", "P2", "waiting_on_customer", "sam", 30, False),
    Ticket(4, "Export to CSV fails", "P2", "open", "lee", 28, True),
    Ticket(5, "Typo on pricing page", "P3", "open", None, 96, False),
    Ticket(6, "Old feature request", "P3", "closed", "maya", 240, False),
    Ticket(7, "Password reset email delayed", "P1", "open", "lee", 4, False),
    Ticket(8, "Report totals look wrong", "P2", "open", None, 26, False),
    Ticket(9, "Payment page error", "P1", "open", "sam", 7, False),
]
