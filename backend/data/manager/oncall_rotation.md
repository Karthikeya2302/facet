# On-Call Rotation Policy

Applies to: Payments, Platform, Risk, Data engineering teams.

## Structure
- Primary on-call: 1 week shifts, Monday 10am IST to Monday 10am IST
- Secondary on-call: same shift, paged only if primary doesn't ack in 15 min
- Manager on-call: same shift, paged for P0 or for escalation by primary

## Compensation
- ₹15,000/week primary
- ₹5,000/week secondary
- ₹10,000/week manager
- 1 comp day per week of primary, taken within 30 days
- P0 incident with >2 hours active response: additional comp day

## Coverage requirements
- L3+ engineers eligible for primary
- L4+ engineers eligible for secondary mentoring of primary
- Managers handle their own team's manager rotation

## Page response SLAs
- P0 (customer-impacting outage): 5 minutes ack, 15 minutes engaged
- P1 (degraded, customer-noticed): 15 minutes ack, 30 minutes engaged
- P2 (degraded, not customer-noticed): 30 minutes ack, 2 hours engaged
- P3 (informational): next business day

## Tooling
- PagerDuty for paging
- Slack #incident-{number} channel auto-created on P0/P1
- Status page (status.[redacted].com) updated within 10 min of P0 declaration
- Postmortem required within 5 business days of P1+, blameless format

## Burnout safeguards
- No engineer on primary more than 1 week per 6 weeks
- If on-call week had > 8 hours active response, mandatory skip of next rotation
- Manager reviews on-call load monthly
