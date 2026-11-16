// Ticket data used by every part of the exercise. You shouldn't need to change this file.
//
// Priority: "P1" (most urgent), "P2" or "P3"
// Status: "open", "waiting_on_customer" or "closed"
// Assignee: null means nobody is assigned
// HoursOpen: whole hours since the ticket was created
// Responded: true once someone from support has replied
public record Ticket(
    int Id,
    string Title,
    string Priority,
    string Status,
    string? Assignee,
    int HoursOpen,
    bool Responded);
