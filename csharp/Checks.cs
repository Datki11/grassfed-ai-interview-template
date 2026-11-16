using System.Collections;
using System.Text;

// Simple checks. Click Run to execute them. You can add your own checks in Run().
public static class Checks
{
    private record Result(string Name, bool Ok, string Detail);

    private static readonly List<Result> Results = new();

    private static void Check(string name, Action body)
    {
        try
        {
            body();
            Results.Add(new Result(name, true, ""));
        }
        catch (NotImplementedException e)
        {
            Results.Add(new Result(name, false, $"not written yet ({e.Message})"));
        }
        catch (Exception e)
        {
            Results.Add(new Result(name, false, e is CheckFailed ? e.Message : $"{e.GetType().Name}: {e.Message}"));
        }
    }

    private class CheckFailed : Exception
    {
        public CheckFailed(string message) : base(message) { }
    }

    private static string Describe(object? value) => value switch
    {
        null => "null",
        string s => $"\"{s}\"",
        IDictionary d => "{" + string.Join(", ", d.Keys.Cast<object>().OrderBy(k => k.ToString())
            .Select(k => $"{k}: {Describe(d[k])}")) + "}",
        IEnumerable e => "[" + string.Join(", ", e.Cast<object?>().Select(Describe)) + "]",
        _ => value.ToString() ?? "",
    };

    private static void ExpectEqual(object? actual, object? expected)
    {
        if (Describe(actual) != Describe(expected))
            throw new CheckFailed($"expected {Describe(expected)}, got {Describe(actual)}");
    }

    public static void Run()
    {
        Console.OutputEncoding = Encoding.UTF8;
        var tickets = SampleTickets.All;

        // ---- Part 1 ----
        Check("Part 1: open tickets for P1, P2 and P3", () =>
            ExpectEqual(new[] { TicketStats.CountOpen(tickets, "P1"), TicketStats.CountOpen(tickets, "P2"),
                TicketStats.CountOpen(tickets, "P3") }, new[] { 4, 3, 1 }));
        Check("Part 1: open tickets, empty list", () =>
            ExpectEqual(TicketStats.CountOpen(new List<Ticket>(), "P1"), 0));
        Check("Part 1: oldest open ticket", () =>
            ExpectEqual(TicketStats.OldestOpenTicket(tickets)?.Id, 5));
        Check("Part 1: oldest open ticket, empty list", () =>
            ExpectEqual(TicketStats.OldestOpenTicket(new List<Ticket>()), null));

        // ---- Part 2 ----
        Check("Part 2: first line of the report", () =>
            ExpectEqual(Overdue.FormatReport(Overdue.FindOverdueTickets(tickets))[0],
                "P1 #9 Payment page error - 3h overdue (sam)"));
        Check("Part 2: report with no overdue tickets", () =>
            ExpectEqual(Overdue.FormatReport(new List<Ticket>()), new[] { "No overdue tickets." }));

        // ---- Add your own checks here ----

        PrintResults();
    }

    private static void PrintResults()
    {
        var passed = Results.Count(r => r.Ok);
        foreach (var r in Results)
            Console.WriteLine((r.Ok ? "✓ " : "✗ ") + r.Name + (r.Ok ? "" : $"\n    {r.Detail}"));
        Console.WriteLine($"\n{passed} passed, {Results.Count - passed} failed");
    }
}
