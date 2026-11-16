import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

// Simple checks. Click Run to execute them. You can add your own checks in run().
public final class Checks {
    private record Result(String name, boolean ok, String detail) {}

    private static final List<Result> results = new ArrayList<>();

    private static void check(String name, Runnable body) {
        try {
            body.run();
            results.add(new Result(name, true, ""));
        } catch (UnsupportedOperationException e) {
            results.add(new Result(name, false, "not written yet (" + e.getMessage() + ")"));
        } catch (AssertionError e) {
            results.add(new Result(name, false, e.getMessage()));
        } catch (RuntimeException e) {
            results.add(new Result(name, false, e.getClass().getSimpleName() + ": " + e.getMessage()));
        }
    }

    private static void expectEqual(Object actual, Object expected) {
        if (!Objects.equals(actual, expected)) {
            throw new AssertionError("expected " + expected + ", got " + actual);
        }
    }

    public static void run() {
        var tickets = SampleTickets.ALL;

        // ---- Part 1 ----
        check("Part 1: open tickets for P1, P2 and P3", () ->
            expectEqual(List.of(TicketStats.countOpen(tickets, "P1"), TicketStats.countOpen(tickets, "P2"),
                TicketStats.countOpen(tickets, "P3")), List.of(4, 3, 1)));
        check("Part 1: open tickets, empty list", () ->
            expectEqual(TicketStats.countOpen(List.of(), "P1"), 0));
        check("Part 1: oldest open ticket", () -> {
            Ticket oldest = TicketStats.oldestOpenTicket(tickets);
            expectEqual(oldest == null ? null : oldest.id(), 5);
        });
        check("Part 1: oldest open ticket, empty list", () ->
            expectEqual(TicketStats.oldestOpenTicket(List.of()), null));

        // ---- Part 2 ----
        check("Part 2: first line of the report", () ->
            expectEqual(Overdue.formatReport(Overdue.findOverdueTickets(tickets)).get(0),
                "P1 #9 Payment page error - 3h overdue (sam)"));
        check("Part 2: report with no overdue tickets", () ->
            expectEqual(Overdue.formatReport(List.of()), List.of("No overdue tickets.")));

        // ---- Add your own checks here ----

        printResults();
    }

    private static void printResults() {
        long passed = results.stream().filter(Result::ok).count();
        for (Result r : results) {
            System.out.println((r.ok() ? "✓ " : "✗ ") + r.name() + (r.ok() ? "" : "\n    " + r.detail()));
        }
        System.out.println("\n" + passed + " passed, " + (results.size() - passed) + " failed");
    }

    private Checks() {}
}
