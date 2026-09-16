# Booking-service example

**Status:** constructed example and executable arithmetic, 2026-09-16. AI-assisted; author review pending. No real service data, participants, or field experiment. This does not validate UCF or recommend a real allocation rule.

## Assumptions

One service has 120 minutes in a single period. There are eight requests taking 15 minutes each and two taking 45 minutes each: 210 minutes of demand. Appointments cannot be divided. Every selected request completes; durations are known exactly. No urgency, outcomes, travel, eligibility, cancellations, skill differences, or preferences are modeled. “Unmet service minutes” is unfinished requested work, not measured waiting time, experienced harm, or another provider's actual workload.

Compare three precisely specified rules using the same information:

- **Arrival order:** two long requests followed by eight short requests; stop when the next request cannot fit. This is an arbitrary fixed queue, not a fairness baseline.
- **Maximum completions:** enumerate feasible combinations and maximize the number served. Break ties by serving more long requests, then more short requests.
- **At least one of each:** impose that coverage constraint, then use the same objective and tie rule. Report infeasible when it cannot be met; do not silently relax it.

## Computed results

| Rule | Short served | Long served | Completions | Used minutes | Unmet requests | Unmet service minutes |
|---|---:|---:|---:|---:|---:|---:|
| Arrival order | 2 | 2 | 4 | 120 | 6 | 90 |
| Maximum completions | 8 | 0 | 8 | 120 | 2 | 90 |
| At least one of each | 5 | 1 | 6 | 120 | 4 | 90 |

The local target can exclude the longer requests. The coverage constraint changes that distribution but does not eliminate the shortage or dominate every outcome. All three use the full capacity and leave 90 minutes unfinished. Normative evaluation needs information and authorization not supplied by the model.

The script also enumerates 24 capacity/duration combinations (six capacities and four long-request durations), evaluating three rules in each. At 210 minutes in the base-duration case, every request fits and the exclusion disappears. At capacity 30 with the base durations, serving at least one of each is infeasible. These are explicit limits to the example, not inconvenient cases omitted from it.

## What UCF's layers reveal

**Internal:** The completion-maximizer works correctly for its target. There is no need to invent a software bug to explain the exclusion.

**Inter-agent:** Requests are not interchangeable in resource requirements. Any referral requires another service's agreement, capacity, and compatibility; none is simulated here.

**Systemic:** Moving an unmet request outside the reporting boundary does not establish that it was served. The table cannot establish total societal benefit, and a larger boundary needs actual data.

**Temporal:** This is a one-period model. Recurring exclusion, backlog, learning, changing demand, and maintenance remain questions for a later model, not results from this run.

A competent resource-and-impact review can identify these same facts. This pass has not demonstrated that UCF discovers additional omissions or reduces review effort.

## State-label stress test

Calling the optimizer internally “Flow” while calling its capacity mismatch “Tension” changes no prediction or arithmetic. Calling the constrained rule “Unity” would conceal remaining exclusions unless the term had independent criteria. The first editorial application therefore uses the four layers without assigning an overall state.

This is an AI-assisted analysis, not a blinded comparison or inter-rater reliability study. Whether the state vocabulary adds value remains UC-004, not a settled rejection of all state labels.

## Four definition counterexamples

1. **Effective but coercive, fictional:** The service meets its completion target by compelling attendance. Functional performance does not answer the authority objection.
2. **Protective but unreliable, fictional:** Refusal and appeal exist, but the software repeatedly loses bookings. Procedural commitments do not establish service reliability.
3. **Mixed outcome, computed fixture:** A coverage constraint serves one long request but reduces total completions; unmet work remains. Do not compress this into one improvement score.
4. **Bounded repair, fictional variant:** A booking-loss defect is corrected without changing access rules. The repair can support a limited reliability claim, not a conclusion that all system purposes are legitimate.

The two counterexamples and repair variant are editorial constructions, not tested deployments. They examine whether definitions preserve distinctions; there has been no human-reviewer study.

## Reproduce

From this directory, using Python 3.10 or later:

```sh
python -m unittest -v
python booking_model.py --output /tmp/ucf-booking-results.json
```

The output path must not already exist. The standard-library script does not contact a network or collect data. Source: [booking_model.py](booking_model.py); checks: [test_booking_model.py](test_booking_model.py).

Eight implementation tests passed locally on 2026-09-16. They check expected allocations, capacity and demand accounting, maximality of the local objective, infeasible constraints, the sufficient-capacity counterexample, and input validation. These checks concern code and arithmetic, not scientific validity.

## Next test, not yet run

Compare the layer review against a competent existing assessment on the same bounded case, with comparable information and effort. Record omissions, false alarms, disagreement, burden, and unnecessary data requests. Independent evaluation, richer service modeling, and cross-domain transfer remain open.

[Model](../../ucf-model-v1.1-draft.md) · [Claims](../../../docs/claims.md) · [Evidence](../../../docs/evidence.md)
