// Simple checks. Click Run to execute them. You can add your own checks at the bottom.
import { NotWrittenYet, SAMPLE_TICKETS } from './tickets';
import { countOpen, oldestOpenTicket } from './ticketStats';
import { findOverdueTickets, formatReport } from './overdue';

const results: { name: string; ok: boolean; detail: string }[] = [];

function check(name: string, fn: () => void) {
  try {
    fn();
    results.push({ name, ok: true, detail: '' });
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    results.push({ name, ok: false, detail: error instanceof NotWrittenYet ? `not written yet (${message})` : message });
  }
}

function expectEqual(actual: unknown, expected: unknown) {
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e) throw new Error(`expected ${e}, got ${a}`);
}

// ---- Part 1 ----
check('Part 1: open tickets for P1, P2 and P3', () =>
  expectEqual([countOpen(SAMPLE_TICKETS, 'P1'), countOpen(SAMPLE_TICKETS, 'P2'), countOpen(SAMPLE_TICKETS, 'P3')], [4, 3, 1]));
check('Part 1: open tickets, empty list', () =>
  expectEqual(countOpen([], 'P1'), 0));
check('Part 1: oldest open ticket', () =>
  expectEqual(oldestOpenTicket(SAMPLE_TICKETS)?.id ?? null, 5));
check('Part 1: oldest open ticket, empty list', () =>
  expectEqual(oldestOpenTicket([]), null));

// ---- Part 2 ----
check('Part 2: first line of the report', () =>
  expectEqual(formatReport(findOverdueTickets(SAMPLE_TICKETS))[0], 'P1 #9 Payment page error - 3h overdue (sam)'));
check('Part 2: report with no overdue tickets', () =>
  expectEqual(formatReport([]), ['No overdue tickets.']));

// ---- Add your own checks here ----


export function printResults() {
  const passed = results.filter((r) => r.ok).length;
  for (const r of results) {
    console.log(`${r.ok ? '✓' : '✗'} ${r.name}${r.ok ? '' : `\n    ${r.detail}`}`);
  }
  console.log(`\n${passed} passed, ${results.length - passed} failed`);
}
