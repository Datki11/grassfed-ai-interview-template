// Ticket data used by every part of the exercise. You shouldn't need to change this file.

export type Priority = 'P1' | 'P2' | 'P3'; // P1 is the most urgent
export type Status = 'open' | 'waiting_on_customer' | 'closed';

export interface Ticket {
  id: number;
  title: string;
  priority: Priority;
  status: Status;
  assignee: string | null; // null means nobody is assigned
  hoursOpen: number;       // whole hours since the ticket was created
  responded: boolean;      // true once someone from support has replied
}

export const SAMPLE_TICKETS: Ticket[] = [
  { id: 1, title: 'Login page down', priority: 'P1', status: 'open', assignee: null, hoursOpen: 6, responded: false },
  { id: 2, title: 'Slow dashboard', priority: 'P1', status: 'open', assignee: 'maya', hoursOpen: 2, responded: false },
  { id: 3, title: 'Invoice missing', priority: 'P2', status: 'waiting_on_customer', assignee: 'sam', hoursOpen: 30, responded: false },
  { id: 4, title: 'Export to CSV fails', priority: 'P2', status: 'open', assignee: 'lee', hoursOpen: 28, responded: true },
  { id: 5, title: 'Typo on pricing page', priority: 'P3', status: 'open', assignee: null, hoursOpen: 96, responded: false },
  { id: 6, title: 'Old feature request', priority: 'P3', status: 'closed', assignee: 'maya', hoursOpen: 240, responded: false },
  { id: 7, title: 'Password reset email delayed', priority: 'P1', status: 'open', assignee: 'lee', hoursOpen: 4, responded: false },
  { id: 8, title: 'Report totals look wrong', priority: 'P2', status: 'open', assignee: null, hoursOpen: 26, responded: false },
  { id: 9, title: 'Payment page error', priority: 'P1', status: 'open', assignee: 'sam', hoursOpen: 7, responded: false },
];

// Thrown by the empty functions until you write them.
export class NotWrittenYet extends Error {}
