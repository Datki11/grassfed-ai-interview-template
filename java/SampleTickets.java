import java.util.List;

// You shouldn't need to change this file.
public final class SampleTickets {
    public static final List<Ticket> ALL = List.of(
        new Ticket(1, "Login page down", "P1", "open", null, 6, false),
        new Ticket(2, "Slow dashboard", "P1", "open", "maya", 2, false),
        new Ticket(3, "Invoice missing", "P2", "waiting_on_customer", "sam", 30, false),
        new Ticket(4, "Export to CSV fails", "P2", "open", "lee", 28, true),
        new Ticket(5, "Typo on pricing page", "P3", "open", null, 96, false),
        new Ticket(6, "Old feature request", "P3", "closed", "maya", 240, false),
        new Ticket(7, "Password reset email delayed", "P1", "open", "lee", 4, false),
        new Ticket(8, "Report totals look wrong", "P2", "open", null, 26, false),
        new Ticket(9, "Payment page error", "P1", "open", "sam", 7, false)
    );

    private SampleTickets() {}
}
