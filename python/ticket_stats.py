"""
PART 1: no AI for this part. Documentation and search engines are fine.

Write the body of each function below. Click Run to check your work.
"""
from typing import Optional
from tickets import Ticket


def count_open(tickets: list[Ticket], priority: str) -> int:
    """
    Return how many tickets have this priority and are NOT closed.
    For example, count_open(SAMPLE_TICKETS, "P1") should return 4.
    """
    raise NotImplementedError("Part 1: write count_open")


def oldest_open_ticket(tickets: list[Ticket]) -> Optional[Ticket]:
    """
    Return the ticket that is NOT closed and has the highest hours_open.
    Return None if there are no tickets that aren't closed.
    """
    raise NotImplementedError("Part 1: write oldest_open_ticket")
