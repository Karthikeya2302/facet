# Demo Data Corpus

All 25 documents for the fictional Series B fintech. Internally consistent.
Drop each into `backend/data/{role}/{filename}.md`.

**Cross-doc facts to keep consistent if you regenerate or extend:**
- ARR: ~$24M, growing ~30% MoM (Q3)
- Headcount: 187, target 250 EOY 2025
- Last raise: Series B, $40M, 14 months ago, led by Ascendant Ventures
- Cash runway: 22 months
- Project Nightingale: acquisition of "Stride Payments" for $12M (CEO-only)
- Regulatory inquiry: central bank notice on KYC procedures (CEO-only)
- Salary bands (HR-only): L3 ₹18-28L, L4 ₹28-45L, L5 ₹45-70L, L6 ₹70-1.1Cr
- Engineering teams: Payments, Platform, Risk, Data

---

## ceo/board_minutes_q3.md

```markdown
# Board Minutes — Q3 Review

**Date:** September 18, 2025
**Attendees:** CEO, CFO, CTO, two independent board members, two investor reps (Ascendant Ventures, Helios Capital)

## Financial review
Q3 ARR closed at $24.1M, up 28% from Q2. Gross margin holding at 71%. Net burn $1.8M/month, runway 22 months at current spend. CFO presented revised FY26 plan targeting $48M ARR.

## Project Nightingale — approved
The board unanimously approved proceeding with Project Nightingale, the acquisition of Stride Payments Pvt Ltd, at an offer of $12M (60% cash, 40% equity). Stride's payment-rails team (14 engineers) will be absorbed into the Platform team. Their merchant book (~3,400 SMB customers) will migrate to our infrastructure over Q1 2026. The CEO and CFO are authorized to finalize terms by November 30, 2025. Public announcement deferred to post-close.

## Regulatory inquiry — discussed
The central bank's notice dated August 22 regarding KYC procedures was reviewed. Outside counsel (Trilegal) is leading the response. Initial assessment: procedural, not enforcement. The board approved a $400K legal reserve. The CEO will update the board monthly until resolution.

## Hiring plan
Approved expansion to 250 by end of year. Heaviest weighting toward Platform (acquisition integration) and Risk (regulatory posture). HR has been briefed.

## Next meeting
December 11, 2025. Standing agenda items: Nightingale integration status, regulatory update, FY26 plan finalization.
```

---

## ceo/project_nightingale_brief.md

```markdown
# Project Nightingale — Internal Brief

**Status:** Board-approved, pre-close. STRICTLY CONFIDENTIAL.

## Target
Stride Payments Pvt Ltd. Bangalore-based, founded 2021. ~3,400 SMB merchants, mostly in Tier-2 cities. ARR ~$3.1M, growing 12% MoM. Team of 22 (14 engineers, 4 sales, 4 ops).

## Rationale
Three reasons:
1. **Geographic gap.** Stride owns Tier-2 SMB market share we've been unable to crack with our enterprise-led GTM.
2. **Talent.** Their payment-rails team has deep expertise in UPI reconciliation — work we'd otherwise hire 6-9 months to build.
3. **Defensive.** Stride was approaching a Series A; if they raised, they'd become a real competitor in 18 months.

## Deal structure
- Total: $12M
- 60% cash ($7.2M), 40% equity ($4.8M at our last 409A)
- Founder retention: 24-month earnout, 30% of equity portion tied to Q4 2026 ARR target of $5M from acquired book
- Key-person clauses: founding CTO of Stride must stay 18 months
- No-shop clause expires November 30

## Integration plan
- Engineering: Stride's payment-rails team folds into Platform under [redacted, manager name TBD]
- Product: Stride's merchant dashboard sunset by Q2 2026, migrated to our UI
- Brand: Stride brand retained for 12 months to avoid migration friction

## Risks
- Regulatory: central bank's KYC inquiry could complicate close if not resolved
- Cultural: Stride is heavily engineering-led, fewer process gates than we have
- Customer concentration: top 5 Stride merchants are 18% of their revenue

## Sign-off
CEO, CFO (approved). Board: approved Q3. Legal: Trilegal handling.
```

---

## ceo/exec_compensation.md

```markdown
# Executive Compensation Structure 2025

This document covers compensation for the CEO, CFO, CTO, and VP-level leadership. Confidential — CEO-only access.

## CEO
- Base: ₹1.8 Cr
- Target bonus: 50% of base, tied to ARR and runway targets
- Equity: 6.2% fully diluted, vested over 4 years, 25% cliff already passed
- Refresh grant: 0.5% post-Series B, vesting 4 years from grant

## CFO
- Base: ₹1.4 Cr
- Target bonus: 40% of base
- Equity: 0.9% fully diluted, 4-year vest, 14 months in

## CTO
- Base: ₹1.5 Cr
- Target bonus: 40% of base
- Equity: 1.1% fully diluted, 4-year vest, fully employed since founding (cliff passed)

## VP Engineering, VP Sales, VP Product
- Base: ₹85-95L range
- Target bonus: 25% of base
- Equity: 0.3-0.5% each

## Notes on philosophy
Exec compensation is benchmarked against Pave data for Series B fintechs in India. Base is at 50th percentile, equity weighted higher (75th percentile) to align with company outcome. Annual review in March; next adjustment April 1, 2026.

## Board notification
All exec comp changes >5% require board notification. Changes >10% require board approval.
```

---

## ceo/regulatory_inquiry_response.md

```markdown
# Central Bank KYC Inquiry — Response Status

**Inquiry received:** August 22, 2025
**Counsel:** Trilegal (lead: partner Priya Menon)
**Response filed:** September 15, 2025
**Status:** Awaiting follow-up

## Background
The central bank issued a notice under Section 35A regarding our KYC verification procedures, specifically for merchant onboarding between January-June 2025. Concern: roughly 340 merchants were onboarded with secondary verification gaps (PAN matched, but address verification skipped via a deprecated automation path).

## Our position
- The gap was identified internally on July 18, before the notice
- A remediation plan was already underway: all affected merchants re-verified by August 30
- We notified the central bank's compliance desk on July 21 (i.e., before the formal notice)
- No customer funds were lost; no fraud attributable to the gap

## Response filed
- Acknowledged the procedural gap
- Submitted remediation evidence (re-verification logs, code audit, process changes)
- Requested closure without further action

## Risk assessment
Trilegal's read: 70% likely closed without penalty, 25% likely closed with a warning letter, 5% likely small financial penalty (₹50L-1Cr range). No reasonable scenario where license is at risk.

## Reserve
$400K legal/penalty reserve booked Q3, per board approval.

## Communication
- Internal: only exec team and audit committee aware
- External: no disclosure required at this stage; would be required only if penalty imposed
- Investors: notified Ascendant and Helios via secure data room, no broader disclosure
```

---

## ceo/fundraise_plans_2026.md

```markdown
# Series C Planning — Internal

**Timing target:** Q3 2026
**Quantum target:** $80-120M
**Valuation target:** $600M-$800M (3-4x last)

## Rationale for timing
Current runway is 22 months. Series C at Q3 2026 leaves ~9 months of buffer after close — comfortable, not desperate. Key proof points needed before raise:

1. ARR > $40M (FY26 plan targets $48M)
2. Project Nightingale fully integrated, contributing $5M+ ARR from acquired book
3. Regulatory inquiry resolved with no enforcement
4. Path-to-profitability narrative tightened (target: positive EBITDA by Q4 2027)

## Lead candidates
Tier 1 (preferred):
- Sequoia India (Surge alumni network)
- Lightspeed India
- Accel
Tier 2:
- Tiger Global (back from hiatus)
- Premji Invest
Strategic:
- Visa Ventures (signaled interest)
- Mastercard (cold)

## Process timeline (draft)
- April 2026: Banker selection (likely Avendus or Modern Treasury Capital)
- May-June: Materials prep, customer reference setup
- July: Soft-circle conversations
- August-September: Formal process
- October-November: Close

## Risks
- Macro: if rates stay high, growth multiples compress
- Nightingale: if integration slips, ARR proof point weakens
- Regulatory: any escalation kills the timeline
```

---

## ceo/quarterly_financials.md

```markdown
# Q3 2025 Financial Summary

## P&L
| Metric | Q3 actual | Q3 plan | vs plan |
|---|---|---|---|
| Revenue | $7.4M | $7.1M | +4% |
| Gross margin | 71% | 70% | +1pp |
| OpEx | $9.1M | $8.8M | +3% |
| Net burn | $1.8M/mo | $1.7M/mo | -6% |

## Balance sheet (Sep 30)
- Cash: $39.4M
- AR: $4.2M (DSO 51 days)
- Total assets: $46.1M
- Debt: $0
- Runway: 22 months at current burn

## ARR detail
- Starting ARR (Q2 end): $18.8M
- New: $7.2M
- Churn: $1.9M
- Expansion: $0
- Ending ARR: $24.1M
- Net new ARR: $5.3M

## Top 10 customers
Concentration at 31% of ARR (vs 38% Q2) — diversification trending right direction.

## Notes for board
- Burn slightly over plan, driven by Risk team hiring acceleration in anticipation of regulatory work and Nightingale integration prep
- Gross margin improvement from infra cost optimization (-12% on AWS spend after Q2 reserved-instance audit)
- DSO creep watch: 51 vs 44 last quarter; AR team flagged 6 late-paying accounts, escalation underway
```

---

## hr/salary_bands_2025.md

```markdown
# Salary Bands 2025 — Engineering, Product, Design

Confidential. HR-only access. Bands are total cash compensation (base + target bonus). Equity granted separately per level.

## Engineering levels

| Level | Title | Total cash (₹) | Equity (% / refresh) |
|---|---|---|---|
| L2 | SDE I | 12-18 L | 0.005% / annual refresh |
| L3 | SDE II | 18-28 L | 0.01-0.02% / annual refresh |
| L4 | Senior SDE | 28-45 L | 0.03-0.06% / annual refresh |
| L5 | Staff Engineer | 45-70 L | 0.08-0.15% / annual refresh |
| L6 | Principal Engineer | 70 L - 1.1 Cr | 0.20-0.40% / biannual refresh |
| L7 | Distinguished Engineer | 1.1 - 1.6 Cr | 0.40-0.70% / biannual refresh |

## Engineering Manager track

| Level | Title | Total cash (₹) |
|---|---|---|
| M4 | Engineering Manager (1 team) | 38-55 L |
| M5 | Senior EM (2-3 teams) | 55-85 L |
| M6 | Director Eng | 85 L - 1.3 Cr |

## Product

| Level | Title | Total cash (₹) |
|---|---|---|
| P3 | PM | 22-35 L |
| P4 | Senior PM | 35-55 L |
| P5 | Staff PM | 55-80 L |
| P6 | Principal / Group PM | 80 L - 1.2 Cr |

## Design

| Level | Title | Total cash (₹) |
|---|---|---|
| D3 | Product Designer | 20-32 L |
| D4 | Senior Designer | 32-50 L |
| D5 | Staff Designer | 50-75 L |

## Notes
- Bands are 50th-75th percentile against Pave India fintech benchmark, refreshed July 2025
- Mid-band is the target for typical performers; top of band requires "exceeds" rating two cycles running
- Geo adjustment: -10% for fully remote, -15% for non-metro
- All offers above mid-band require VP approval; above top-of-band requires CFO sign-off
```

---

## hr/q4_hiring_pipeline.md

```markdown
# Q4 2025 Hiring Pipeline

**Target:** Close 63 hires by December 31 to land at 250 headcount.
**Current pipeline:** 47 in-process candidates, 11 offers out, 4 accepted/awaiting start.

## By function

| Function | Q4 target | Pipeline | Offers out | Risk |
|---|---|---|---|---|
| Engineering | 38 | 29 | 7 | Medium — top funnel weak |
| Risk & Compliance | 8 | 6 | 1 | High — small candidate pool |
| Sales | 7 | 6 | 2 | Low |
| Product | 4 | 3 | 1 | Low |
| Operations | 4 | 2 | 0 | Medium |
| G&A | 2 | 1 | 0 | Low |

## Engineering breakdown
- Platform team: 14 open (Nightingale integration prep) — 11 in pipe
- Payments: 9 open — 7 in pipe
- Risk eng: 7 open — 5 in pipe
- Data: 5 open — 4 in pipe
- Other: 3 open — 2 in pipe

## Top open roles
1. Staff Engineer, Platform (L5) — 6 weeks open, 2 final-round
2. Director of Risk Engineering (M6) — 4 weeks open, 1 final-round
3. Senior PM, Payments (P4) — 3 weeks open, 3 in process

## Sourcing channels (last 30 days)
- Inbound applications: 1,840 (12% response rate)
- Recruiter outreach: 410 (28% response rate)
- Employee referrals: 67 (51% response rate) — highest conversion
- Agencies: 28 (low volume, high cost)

## Risks
- Risk Eng director search dragging — consider raising offer band by 10%
- Platform velocity needed for Nightingale integration (Q1 2026); if 6+ hires don't close by Dec, integration timeline slips
```

---

## hr/performance_review_framework.md

```markdown
# Performance Review Framework

Twice-yearly cycle: April and October. Snapshot-based, not continuous.

## Ratings
Five-point scale, distribution-constrained at the company level:

| Rating | Meaning | Distribution target |
|---|---|---|
| Exceeds++ | Top performer, multi-cycle | 5% |
| Exceeds | Consistently above expectations | 20% |
| Meets+ | Solid, above-bar | 40% |
| Meets | At expectations | 25% |
| Below | Performance plan triggered | 10% |

## Inputs
1. **Self-review** — written by employee
2. **Manager review** — written by direct manager
3. **Peer feedback** — 3-5 peers selected by employee, validated by manager
4. **Skip-level review** — manager's manager weighs in on calibration

## Calibration
Department-level calibration before ratings finalize. VP and HR partner moderate. Goal: prevent rating inflation, ensure cross-team fairness.

## Compensation linkage
- Exceeds++: top of band, accelerated equity refresh, promotion consideration
- Exceeds: above mid-band, standard refresh, promotion consideration after two cycles
- Meets+: mid-band, standard refresh
- Meets: mid-band, reduced refresh
- Below: performance plan, no increase, no refresh

## Performance plans
30-60-90 day plans for Below-rated employees. Manager + HR partner co-own. Outcome: improvement (return to Meets), exit with severance, or extension. Roughly 40% of plans result in exit.

## Notes
- First review for new hires: deferred to cycle after 6 months tenure
- Internal transfers: rating carries from prior role for 1 cycle
- Manager change mid-cycle: prior manager input required
```

---

## hr/headcount_plan_2026.md

```markdown
# Headcount Plan 2026

Confidential. HR-only. Board-approved at September meeting.

## Year-end targets

| Function | Dec 2025 | Dec 2026 | Net add | Mostly driven by |
|---|---|---|---|---|
| Engineering | 142 | 195 | +53 | Nightingale integration, platform scale |
| Risk & Compliance | 18 | 32 | +14 | Regulatory posture, new product lines |
| Sales | 32 | 48 | +16 | Series C-readiness, enterprise motion |
| Product | 14 | 20 | +6 | New product lines |
| Operations | 22 | 28 | +6 | Merchant ops scale |
| G&A | 12 | 17 | +5 | Finance, legal, IT |
| **Total** | **240*** | **340** | **+100** | |

*Includes Nightingale acquisition headcount (22) closing Q1 2026.

## Cost implications
- Average fully-loaded cost per hire: ₹62L
- 2026 incremental payroll: ~₹62 Cr (~$7.4M)
- Embedded in FY26 plan

## Hiring cadence
- Q1: 35 (heavy front-load for Nightingale integration)
- Q2: 28
- Q3: 22
- Q4: 15

## Constraints
- Bangalore office capacity caps at 280; need real-estate decision by Q2
- Recruiting team needs to grow from 6 to 10 to support volume
- Compensation budget assumes mid-band; significant above-band hiring will trigger replan
```

---

## hr/benefits_summary.md

```markdown
# Employee Benefits Summary 2025

Applies to all full-time employees.

## Health insurance
- Coverage: employee + spouse + 2 children + 2 parents
- Sum insured: ₹10L base, top-up available at employee cost
- Provider: ICICI Lombard
- Pre-existing conditions: covered from day 1 (no waiting period)
- Maternity: ₹1L sub-limit, no waiting period
- OPD: ₹15K annual reimbursement

## Life & disability
- Group term life: 5x annual base salary, max ₹2 Cr
- Personal accident: 5x base salary
- Disability cover: 60% income replacement, up to 24 months

## Time off
- Annual leave: 24 days
- Sick leave: 12 days
- Casual leave: 6 days
- Parental leave: 26 weeks (primary), 4 weeks (secondary)
- Bereavement: 5 days
- Sabbatical: 4 weeks unpaid available after 4 years tenure

## Financial
- Employee Provident Fund: standard 12% employee + 12% employer
- Group gratuity: as per Indian gratuity act
- ESOP: per offer letter
- Annual learning budget: ₹40K
- WFH setup allowance: ₹50K one-time

## Other
- Wellness: ₹3K monthly gym/wellness reimbursement
- Mental health: 8 free sessions/year via YourDOST
- Internet allowance (remote): ₹2K/month
- Annual offsite: company-funded, location varies
- Meal allowance (in-office days): ₹250/day

## Tax-optimized salary structuring
Available on request via HR — LTA, meal vouchers, telephone reimbursement, etc.
```

---

## hr/attrition_report.md

```markdown
# Attrition Report — Q3 2025

## Headline
- Annualized regretted attrition: 13.4%
- Industry benchmark (Indian fintech, our stage): 18-22%
- Q3 trend: stable vs Q2 (13.1%), down from Q4 2024 (17.8%)

## By function (Q3 annualized)

| Function | Regretted attrition | YoY |
|---|---|---|
| Engineering | 11.2% | -4.1pp |
| Risk | 8.0% | -2.0pp |
| Sales | 21.4% | +1.2pp |
| Product | 9.1% | -3.0pp |
| Operations | 18.6% | -2.4pp |
| G&A | 12.5% | +0.5pp |

## Exit interview themes (Q3, n=14 regretted exits)
1. Compensation (43%) — gap to competing offers, mostly at L4-L5
2. Growth opportunity (29%) — lack of clear path to next level
3. Manager (21%) — concentrated in two specific managers, escalated
4. Burnout / WLB (14%)
5. Relocation / personal (14%)

## Hot spots
- Sales attrition (21.4%) concerning — investigating commission plan and territory fairness
- Two managers driving disproportionate exits — performance conversations underway with VPs
- L4 engineering: 6 exits in Q3, all citing comp. Salary band review escalated, possible mid-cycle adjustment for L4

## Retention actions Q4
- L4 engineering comp benchmark refresh (target Nov 15)
- Manager skip-level surveys (Oct 20)
- Career-laddering doc rollout for engineering (Nov 30)
- Sales commission plan audit (December)
```

---

## manager/payments_team_roadmap_h1.md

```markdown
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
```

---

## manager/platform_team_budget.md

```markdown
# Platform Team — 2025 Budget & 2026 Plan

Team: 22 engineers + 1 senior EM + 2 EMs + 1 PM. Owns: core infrastructure, internal developer platform, observability, security infra, data pipelines.

## 2025 budget (full year)
| Category | Approved | Spent YTD | Forecast EOY |
|---|---|---|---|
| Headcount (loaded) | ₹14.2 Cr | ₹10.1 Cr | ₹13.8 Cr |
| AWS | ₹3.8 Cr | ₹2.4 Cr | ₹3.4 Cr |
| Third-party tools (DataDog, PagerDuty, etc) | ₹95L | ₹68L | ₹92L |
| Contractors | ₹40L | ₹28L | ₹38L |
| Conferences / training | ₹18L | ₹9L | ₹16L |
| **Total** | **₹19.0 Cr** | **₹13.4 Cr** | **₹18.6 Cr** |

## 2025 wins vs budget
- AWS spend coming in 11% under budget after Q2 reserved-instance audit
- Headcount slightly under plan (4 open reqs) — net positive for budget, net negative for velocity

## 2026 plan asks
- Headcount: +10 engineers (Nightingale integration, recurring payments infra, multi-region prep)
- AWS: +35% (capacity for 4x TPS, multi-region)
- Tooling: +₹20L (security tooling for SOC 2 Type II prep)
- **Total ask: ₹26.4 Cr** (+39% vs 2025)

## Headcount detail (2026)
- 4 Platform Engineers (L4-L5) — Q1
- 2 SREs (L4) — Q1 (Nightingale integration support)
- 2 Security Engineers (L4-L5) — Q2 (SOC 2)
- 2 Data Platform Engineers (L4) — Q2

## Approval status
Approved by CFO at September budget review with 5% contingency reduction (now ₹25.1 Cr). Final sign-off pending December plan close.
```

---

## manager/oncall_rotation.md

```markdown
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
```

---

## manager/team_lead_handbook.md

```markdown
# Team Lead Handbook

For engineering managers and tech leads. Covers expectations, cadences, and resources.

## Weekly cadence
- **Monday:** team standup (15 min), priority review with PM
- **Tuesday-Thursday:** 1:1s (30 min each, every other week per direct report)
- **Friday:** team retro every 2 weeks (30 min), weekly tech-debt grooming (45 min)

## 1:1 expected agenda
- Career growth (5 min)
- Current work / blockers (10 min)
- Feedback both directions (5 min)
- Personal / wellbeing (5 min)
- Anything else (5 min)

Take notes. Send a 2-line summary to your direct report after each 1:1.

## Skip-level cadence
- VP skip-level with each L4+ engineer twice per year
- EM skip-level with each L3 every quarter

## Hiring expectations
- EMs own headcount allocation within their team
- Final say on offers within budget; above-band requires VP sign-off
- Each EM expected to do 4-6 interviews/month average

## Performance management
- Use the rating framework (see performance_review_framework.md)
- Calibration meetings: prep 1 week in advance, bring written justifications
- Performance plans: HR partner is your co-pilot, don't go it alone

## On-call
- EMs are on the manager rotation for their team (see oncall_rotation.md)
- EMs do not typically take primary unless team is too small to staff

## Promotion guidelines
- L3 → L4: typically 18-24 months at L3, 2 strong cycles, clear scope expansion
- L4 → L5: typically 2-3 years at L4, evidence of cross-team impact
- L5 → L6: requires written case to VP + engineering leadership review
- All promotions require calibration approval

## Difficult conversations
- Compensation gaps: redirect to HR for benchmarking, never freelance an answer
- Underperformance: document, document, document; don't surprise people at review time
- Departures: be supportive, manage knowledge transfer, conduct exit conversation
```

---

## manager/engineering_okrs_q1.md

```markdown
# Engineering OKRs — Q1 2026

## Objective 1: Hit Nightingale integration milestones
- KR1: Stride payment-rails code merged to main, all tests passing — Mar 1
- KR2: 100% of Stride merchants migrated to our auth system — Mar 31
- KR3: Zero P0 incidents attributable to integration — ongoing
- Owner: Platform EM, Payments EM (co-owned)

## Objective 2: Reliability bar
- KR1: Payment success rate ≥ 99.97% (Q1 average)
- KR2: P0 incidents ≤ 2 in Q1
- KR3: MTTR for P0 ≤ 25 minutes
- Owner: Platform Director

## Objective 3: Risk posture matches regulatory expectations
- KR1: KYC remediation 100% complete (all 340 affected merchants closed) — Jan 15
- KR2: SOC 2 Type II audit kickoff — Feb 1
- KR3: Internal compliance dashboard live, weekly review with CFO — Mar 1
- Owner: Risk Eng Director

## Objective 4: Hire to plan
- KR1: 35 engineering hires closed in Q1 (vs plan of 35)
- KR2: 100% of new hires through structured onboarding within first 2 weeks
- KR3: Time-to-productivity median ≤ 6 weeks (first commit to main)
- Owner: VP Eng

## Cross-cutting
- All EMs commit to 6 interviews/month average
- Tech debt budget: 20% of sprint capacity, non-negotiable
- All P0/P1 incidents must have public-ish (engineering-wide) postmortems within 5 business days

## Watch items (not OKRs but tracked)
- L4 engineering attrition rate (target < 12% annualized)
- Code review turnaround time (target < 8 working hours median)
- Build pipeline reliability (target > 95% green)
```

---

## employee/company_handbook.md

```markdown
# Company Handbook

Welcome. This is the short version of how things work.

## Working hours
We don't track hours. We do track outcomes. Most teams have a "core hours" overlap of 11am-4pm IST when meetings happen and people are reachable. Outside that, work when works for you.

## Communication
- **Slack:** primary, but not 24/7. No response expected outside working hours.
- **Email:** external partners, formal HR matters
- **Video calls:** scheduled in advance, cameras optional
- **Docs:** decisions live in writing. If it's not written down, it didn't happen.

## Meetings
- 25 or 50 min, not 30 or 60 — buffer between meetings matters
- Agenda required, or it gets declined
- Notes shared after, async-first
- "No meeting Wednesdays" is sacred. Hold the line.

## Decision-making
Use the DACI framework where it matters:
- D: Driver (one person who runs the decision process)
- A: Approver (one person who has final say)
- C: Contributors (give input)
- I: Informed (told after)

If you can't name the A, the decision isn't ready to be made.

## Documents and naming
- Notion is the home for company docs
- Google Docs for drafts
- Use clear titles: "[Team] [Topic] [Date]"

## Conflict
We disagree, commit, and move on. If you can't, escalate openly — your manager or HR is your partner, not your problem.

## Time off
- 24 days annual leave; take them. Block them on the calendar 2 weeks in advance.
- Sick leave: use it without guilt. Mental health counts.
- Bereavement, parental, etc: see benefits summary.

## Equipment
- Laptop, monitor, peripherals provided
- WFH allowance covers chair / desk / internet setup; see IT setup guide
- Replacement cycle: 3 years standard

## Money basics
- Salary credited 28th of each month (or last working day before)
- Reimbursements: process within 30 days via Zaggle
- Payroll questions: hr-payroll@ Slack channel

## Last word
This handbook is short on purpose. We hire adults; we treat you like one. The rest is judgment.
```

---

## employee/holiday_policy.md

```markdown
# Holiday Policy

## Annual leave
- 24 days per calendar year
- Accrued monthly (2 days/month), available immediately on accrual
- Maximum carryover: 8 days into next year; rest lapses
- Notice: 2 weeks for leave > 5 days; 3 days for leave ≤ 5 days
- Manager approval required (rarely refused, but plan for coverage)

## Public holidays
9 fixed public holidays + 3 floating (your choice). 2026 list:

**Fixed:**
- January 1 — New Year
- January 26 — Republic Day
- March 14 — Holi (varies)
- April 14 — Ambedkar Jayanti
- August 15 — Independence Day
- October 2 — Gandhi Jayanti
- November 1 — Diwali (varies)
- December 25 — Christmas
- + 1 region-specific per office

**Floating (pick 3):**
- Eid, Pongal, Onam, Christmas Eve, Ganesh Chaturthi, Karwa Chauth, Good Friday, Buddha Purnima, etc.

## Sick leave
- 12 days per year
- No doctor's note needed for ≤ 2 consecutive days
- Doctor's note required for ≥ 3 consecutive days
- Does not roll over

## Casual leave
- 6 days per year
- For personal matters, short-notice (e.g., bank work, family event)
- 1 day notice typically sufficient

## Parental leave
- Primary caregiver: 26 weeks paid
- Secondary caregiver: 4 weeks paid
- Adoption: same as biological
- Phased return option: 50% schedule for first 4 weeks back

## Bereavement
- 5 days for immediate family
- 2 days for extended family
- No documentation needed

## Marriage leave
- 5 days, once per tenure

## Sabbatical
- 4 weeks unpaid, available after 4 years of continuous service
- Requires 60 days notice

## Edge cases
- Holiday falls on weekend → no compensatory day off (we already have generous PTO)
- On-call during holiday → comp day per on-call policy
- Travel time around long leave → discuss with manager, usually flexible
```

---

## employee/it_setup_guide.md

```markdown
# IT Setup Guide — New Hire Day 1

Welcome. This walks you through your first day's IT setup.

## Hardware (delivered to you before start date)
- MacBook Pro 14" M3 (16GB / 512GB standard; 32GB available on request for ML/data roles)
- External 27" monitor
- Apple Magic Keyboard + Magic Mouse OR Logitech MX equivalents
- USB-C hub
- Webcam (Logitech C920)

If anything's missing or damaged: open a ticket at help.[redacted].com or message #it-support.

## First boot
1. Power on, complete macOS setup wizard. Use your work email (firstname.lastname@[redacted].com).
2. When prompted for an admin account, use the credentials in your welcome email.
3. The MDM (Jamf) profile installs automatically. Approve all prompts.

## Required installs (auto-pushed via Jamf, takes ~30 min)
- Slack
- Zoom
- 1Password (your vault is invited; check your email)
- Okta Verify
- Notion
- Linear
- AnyConnect VPN
- Google Chrome (with managed profile)

## Account setup (do in this order)
1. **Okta:** complete MFA setup with Okta Verify on your phone
2. **Email/calendar:** sign in to Google Workspace via Okta SSO
3. **Slack:** sign in via SSO. Join #general, #announcements, your team channel, #social
4. **1Password:** accept vault invite, transfer over from personal manager if any
5. **Notion:** SSO sign-in, browse the "New Hire" home page
6. **Linear:** SSO sign-in, your team's project will appear

## Engineering-specific
If you're in engineering, you'll get additional accesses:
- GitHub: invitation will land within 24h of start date
- AWS: provisioned via Okta SSO, role-based access
- Internal dev environment: see the engineering onboarding doc in Notion
- VPN: required for staging/prod access

## Common issues
- **Okta MFA stuck:** restart Okta Verify, request reset in #it-support
- **VPN won't connect:** check that you're on Okta-protected SSID at office; for remote, try the AnyConnect "lite" profile
- **Can't find a tool:** check the Software Catalog in Notion

## Phone / Mobile
- Slack on phone: install, sign in via SSO
- 1Password on phone: install, complete the QR-code setup with your laptop
- Okta Verify on phone: required (it's your MFA)

## What if I want a different setup?
- Linux on the laptop: not supported, sorry. We standardize on macOS for MDM/security.
- Mechanical keyboard / different mouse: bring your own, BYOD-friendly
- Standing desk / better chair: claim against your WFH setup allowance

## Help
- Real-time: #it-support on Slack
- Tickets: help.[redacted].com
- In-office: IT desk on the 4th floor, weekday 10-7
```

---

## employee/expense_policy.md

```markdown
# Expense Policy

## Tool of record
All expenses processed through Zaggle. Submit within 30 days of incurring; submissions after 60 days are not reimbursed.

## What's reimbursable
- **Work travel:** flights (economy domestic, premium economy for international > 6 hours), hotels (up to ₹6,000/night metro, ₹4,000 non-metro), local transport, meals up to ₹2,000/day per diem
- **Client meals:** up to ₹3,000/person, must list attendees and purpose
- **Office supplies:** under ₹2,000 with manager approval
- **Subscriptions:** any work-related SaaS / books / courses under ₹5,000 with manager approval; above that, separate IT-purchasing process
- **Conference fees:** with manager approval, no cap on industry conferences
- **WFH setup:** one-time ₹50,000 allowance covers chair, desk, monitor add-ons
- **Internet (remote):** ₹2,000/month

## What's not reimbursable
- Personal phone bills (unless on a designated company line)
- Alcohol for solo client dinners
- Flights upgraded beyond policy
- Gifts to vendors / clients without prior approval
- Penalties (parking tickets, late fees on personal cards)
- Personal entertainment

## Approval flow
- Under ₹5,000: auto-approved if within policy categories
- ₹5,000 – ₹50,000: manager approval required
- Above ₹50,000: VP + Finance approval required
- Above ₹2,00,000: CFO approval required (typically large travel or events)

## Submission steps in Zaggle
1. Snap photo of receipt at time of expense (Zaggle mobile app)
2. Tag with category, project (if applicable), business purpose (1 sentence)
3. Manager auto-notified for approval
4. Reimbursement credited to salary account in 7-10 business days post-approval

## Currency
- Foreign expenses: enter in original currency, Zaggle applies the appropriate FX rate
- Keep the original receipt as Finance may request

## Disputes
If a reimbursement is denied and you disagree, escalate to finance@ — first to your manager, then to Finance. Most disputes resolve in favor of the employee when the business purpose is clearly stated.

## Audit
Random audits 2x per year. Receipts must be retained for 3 years; Zaggle stores them automatically.
```

---

## employee/code_of_conduct.md

```markdown
# Code of Conduct

This applies to everyone: employees, contractors, interns, board members, and visitors at any company-sponsored event.

## Core expectations
- Treat everyone with respect and dignity
- Communicate honestly, even when it's uncomfortable
- Acknowledge mistakes and learn from them
- Protect company and customer data
- Don't compete with the company while employed

## Behaviors that are not okay
- Harassment of any kind, including based on gender, caste, religion, sexual orientation, race, national origin, disability, or age
- Bullying, intimidation, or retaliation
- Discrimination in hiring, promotion, or assignments
- Sexual misconduct of any kind, including unwelcome advances or comments
- Substance abuse during work or company-sponsored events
- Physical violence or threats
- Theft, fraud, falsification of records

## Conflicts of interest
- Disclose any board seat or advisory role at another company
- Disclose any equity holding ≥ 1% in a competitor, customer, or vendor
- Family employment at competitors/vendors: disclose; ongoing roles will be reviewed
- Side gigs: allowed if (a) doesn't conflict with our business (b) doesn't impact your performance here (c) disclosed to your manager

## Confidentiality
- Customer data is protected by law and policy. Access only what you need for your job.
- Internal data (financials, strategy, customer lists) is confidential. No sharing externally without explicit approval.
- Trade secrets remain protected even after you leave the company.
- Use of confidential information for personal benefit (e.g., trading on non-public info) is grounds for termination and legal action.

## Reporting
Three ways to report concerns:
1. Your manager
2. HR (people@[redacted].com)
3. Anonymous: ethics-hotline.[redacted].com (third-party operated)

No retaliation for good-faith reports. Retaliation is itself a violation.

## Investigation
- All reports taken seriously and investigated
- Investigations are confidential to the extent possible
- Outcomes range from coaching to termination depending on severity
- Anyone interviewed in an investigation is protected from retaliation

## Why this matters
Our business depends on trust — customer trust, regulator trust, employee trust. This code isn't paperwork; it's how we keep that trust.
```

---

## employee/remote_work_policy.md

```markdown
# Remote Work Policy

## Modes
The company supports three working modes. Mode is set per-role at offer, reviewable annually.

### Office-based
- 4 days/week in office expected
- Located in primary office city (Bangalore HQ or Mumbai)
- Available for most roles

### Hybrid
- 2 days/week in office expected
- Located within commute of an office
- Default for most engineering, product, design

### Remote
- Fully remote
- Located anywhere in India
- Available for individual contributor roles after manager approval
- Quarterly in-office trip expected (company-funded)

## Switching modes
- Within first 6 months: discuss with manager + HR
- Annual review: opportunity to switch with manager approval
- Mid-cycle change: requires business justification (relocation, family, health)

## Compensation impact
- Office-based and hybrid: full band
- Remote: -10% if within India, -15% if non-metro

## Equipment for remote
- Same baseline as office (laptop, monitor, peripherals)
- WFH setup allowance: ₹50,000 one-time
- Internet allowance: ₹2,000/month
- Quarterly in-office travel: company-booked, economy class, 2 nights

## Working internationally
- Up to 30 days/year working from outside India for personal reasons (with manager approval)
- Visa/tax implications are your responsibility
- Longer-term international working: not currently supported, will require role change

## Time zone expectations
- Core hours (IST 11am-4pm) overlap required for hybrid and remote
- Async-first communication outside core hours
- Managers must accommodate occasional time-shifting (family, doctor's appointments)

## Performance
- Remote performance evaluated same as in-office, no penalty for mode
- Productivity tracked via outcomes (OKRs, project delivery), not hours or activity
- Career progression independent of mode

## Edge cases
- Caregiver responsibilities: flexible scheduling supported, talk to your manager
- Disability/accessibility: full remote available outside of policy with HR support
- Pregnant employees: WFH option without mode change for last trimester
```

---

## employee/security_basics.md

```markdown
# Security Basics for Everyone

You are the first line of defense for keeping customer data and company information safe. Here's what's required of every employee, regardless of role.

## Passwords
- Use 1Password for everything (vault provisioned at onboarding)
- Never reuse passwords across services
- Never share passwords, even with teammates — share access via the proper system (Okta, GitHub teams, etc.)

## MFA
- Required on every work account
- Use Okta Verify (don't use SMS-based MFA where avoidable)
- Lost your phone? Open a ticket in #it-support immediately, do not delay

## Laptops
- Always lock when stepping away (⌃⌘Q on Mac)
- Disk encryption is enforced via MDM — don't disable
- Don't install software outside the Software Catalog without IT approval
- Lost or stolen: report within 1 hour to #it-support; we can remote-wipe

## Email and Slack
- Phishing is the #1 attack vector. If a message asks for credentials, payment changes, or "urgent action," verify out-of-band before acting.
- Use "Report Phishing" button in Gmail for anything suspicious
- Slack DMs from people you don't recognize: verify identity before sharing anything

## Customer data
- Access only what you need for your job
- Don't export customer data to personal devices or accounts
- Never paste customer data into external tools (ChatGPT, online JSON formatters, etc.) — use approved internal tools
- All customer-data access is logged and audited

## Physical security
- Badge required to enter office; don't tailgate or let strangers in
- Visitors must be signed in at reception and escorted
- Don't take photos of work surfaces with sensitive info visible
- Confidential documents: shred, don't trash

## When traveling
- Don't use public Wi-Fi without VPN
- Don't leave laptop unattended in cafes or hotel rooms (use a cable lock for hotel)
- Cross-border travel: be aware of customs laws on devices in your destination

## Reporting incidents
Anything that feels off — suspicious email, weird laptop behavior, accidental data exposure, lost device — report to security@[redacted].com or in #security-incidents. Speed matters more than certainty; we'd rather investigate a false alarm than miss a real one.

## Annual training
You'll complete a 30-minute security training annually, plus a phishing simulation quarterly. It's mandatory and tracked.
```

---

## employee/health_benefits_overview.md

```markdown
# Health Benefits Overview

This is the employee-facing summary. For the full benefits document, see the benefits summary on Notion.

## Health insurance
- Provider: ICICI Lombard
- Covers: you, spouse, up to 2 children, up to 2 parents (or in-laws, your choice)
- Sum insured: ₹10 lakh base
- Top-up: available at employee cost, up to ₹50 lakh additional sum
- Cashless network: ICICI's hospital list (~6,500 hospitals across India)
- Pre-existing conditions: covered day 1, no waiting period
- Maternity: ₹1 lakh sub-limit, no waiting period

## OPD (outpatient)
- ₹15,000/year reimbursement for OPD, diagnostics, dental, vision
- Submit bills through Zaggle, processed in 10 days
- Family members covered

## Mental health
- 8 free sessions/year via YourDOST (therapy / counseling)
- Sessions are confidential — employer never sees details
- Topics: stress, anxiety, family, career, anything you want to talk about

## Wellness
- ₹3,000/month reimbursement for gym, yoga, sports clubs
- Bills via Zaggle
- One subscription at a time (can switch mid-year)

## Maternity
- 26 weeks paid for primary caregiver
- Pregnancy-related expenses covered fully under insurance
- Lactation rooms available in both offices
- Returning mothers: phased return option (50% schedule for first 4 weeks)

## Paternity / secondary caregiver
- 4 weeks paid leave
- Can be taken any time within 6 months of child's birth/adoption
- Same for adoption (both primary and secondary)

## Vaccinations & preventive care
- Annual health checkup paid for you and spouse (Apollo or Practo Plus partner)
- Flu shots offered in office every October
- Children's vaccinations: covered under insurance

## Emergency
- 24/7 ambulance reimbursement
- Emergency room visit: cashless at network hospitals
- Critical illness rider: ₹10 lakh additional cover, included in standard plan

## How to use your benefits
- Cashless hospital visit: show your e-card (in the ICICI Lombard app) at registration
- Reimbursement: submit through Zaggle with original bills
- Mental health: book on YourDOST.com using your work email
- Questions: hr-benefits Slack channel

## Changes during the year
- Adding a dependent (marriage, child birth): notify HR within 30 days
- Switching parents → in-laws (or vice versa): annual window, January
```

---

# How to use this corpus

1. Copy each section above into the corresponding file under `backend/data/{role}/`
2. Strip the surrounding code-fences (the ` ```markdown ` and closing ` ``` `)
3. Save with the filename indicated in the section header
4. Run `python -m app.indexing.ingest` once you have Qdrant and the embedding model set up
5. The corpus is internally consistent — facts referenced across documents (ARR, headcount, salary bands, Project Nightingale, regulatory inquiry) match
6. Demo "gotcha" content for the recruiter moment lives in CEO-only docs (Project Nightingale brief, regulatory response, exec comp) — these are what get blocked for the employee
