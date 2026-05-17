# Payments Team Roadmap — H1 2026

Team: 18 engineers + 1 EM + 2 PMs. Owns: core payments processing, settlement, reconciliation, merchant payouts.

## H1 themes
1. **Reliability** — get to four nines on payment success rate (currently 99.94%)
2. **Throughput** — 5x peak TPS for big-merchant onboarding wins
3. **Nightingale integration** — absorb Stride's payment-rails infra
4. **New product** — recurring payments / subscriptions GA

## Q1 milestones
- Settlement engine v3 (deterministic retries, idempotency hardening) — Feb 15
- Nightingale infra audit complete — Jan 31
- UPI reconciliation cutover (Stride code adopted) — Mar 15
- Payouts SLA: 99.5% within 24h, currently 98.1% — ongoing

## Q2 milestones
- Recurring payments GA — May 30
- TPS ceiling 4x baseline (load tested) — Apr 30
- Stride merchant migration to our infra (3,400 merchants) — Jun 30
- Refunds API v2 (async, webhook-driven) — Jun 15

## Dependencies
- Platform team: infra capacity planning (load test environment by Feb 1)
- Risk team: fraud rules engine integration for recurring payments
- Data team: settlement reconciliation dashboards

## Risks
- Nightingale integration slipping if hiring lags (need 6 senior engineers by Feb)
- TPS targets require database sharding work; if Platform team scope slips, ours slips
- Recurring payments cuts across Risk + Platform + Payments; integration testing window tight

## OKRs aligned
- Eng OKR 1: 99.99% payment success — owned
- Eng OKR 2: zero P0 incidents > 30 min MTTR — co-owned with Platform
- Product OKR: recurring payments revenue > $400K ARR by EOY — owned
