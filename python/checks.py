"""Simple checks. Click Run to execute them. You can add your own checks at the bottom."""
import traceback
from tickets import SAMPLE_TICKETS
from ticket_stats import count_open, oldest_open_ticket
from overdue import find_overdue_tickets, format_report

results: list[tuple[str, bool, str]] = []


def check(name, fn):
    try:
        fn()
        results.append((name, True, ""))
    except NotImplementedError as error:
        results.append((name, False, f"not written yet ({error})"))
    except AssertionError as error:
        results.append((name, False, str(error) or "assertion failed"))
    except Exception:
        results.append((name, False, traceback.format_exc(limit=1).strip().splitlines()[-1]))


def expect_equal(actual, expected):
    assert actual == expected, f"expected {expected!r}, got {actual!r}"


# ---- Part 1 ----
def part1_counts():
    counts = [count_open(SAMPLE_TICKETS, p) for p in ("P1", "P2", "P3")]
    expect_equal(counts, [4, 3, 1])

def part1_counts_empty():
    expect_equal(count_open([], "P1"), 0)

def part1_oldest():
    oldest = oldest_open_ticket(SAMPLE_TICKETS)
    expect_equal(oldest.id if oldest else None, 5)

def part1_oldest_empty():
    expect_equal(oldest_open_ticket([]), None)

check("Part 1: open tickets for P1, P2 and P3", part1_counts)
check("Part 1: open tickets, empty list", part1_counts_empty)
check("Part 1: oldest open ticket", part1_oldest)
check("Part 1: oldest open ticket, empty list", part1_oldest_empty)


# ---- Part 2 ----
def part2_first_line():
    expect_equal(format_report(find_overdue_tickets(SAMPLE_TICKETS))[0], "P1 #9 Payment page error - 3h overdue (sam)")

def part2_empty_report():
    expect_equal(format_report([]), ["No overdue tickets."])

check("Part 2: first line of the report", part2_first_line)
check("Part 2: report with no overdue tickets", part2_empty_report)


# ---- Add your own checks here ----


def print_results():
    passed = sum(1 for _, ok, _ in results if ok)
    for name, ok, detail in results:
        print(f"{'✓' if ok else '✗'} {name}" + ("" if ok else f"\n    {detail}"))
    print(f"\n{passed} passed, {len(results) - passed} failed")
