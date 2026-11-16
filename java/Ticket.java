// Ticket data used by every part of the exercise. You shouldn't need to change this file.
//
// priority: "P1" (most urgent), "P2" or "P3"
// status: "open", "waiting_on_customer" or "closed"
// assignee: null means nobody is assigned
// hoursOpen: whole hours since the ticket was created
// responded: true once someone from support has replied
public record Ticket(
    int id,
    String title,
    String priority,
    String status,
    String assignee,
    int hoursOpen,
    boolean responded
) {}
