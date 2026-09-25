# Dynamic coherence migration audit — 2026-09-24

**Status:** Repository migration inventory / AI-assisted / author review pending  
**Related:** [Dynamic coherence evidence reconciliation](dynamic-coherence-evidence-audit-2026-09-24.md) · [UCF model v1.1](../models/ucf-model-v1.1-draft.md)  
**Purpose:** Identify what should be preserved, extended, re-audited, superseded, or archived after the September 24 adaptive-continuity synthesis.

This is not a claim that every file named below is wrong. It is a **migration queue** based on current model status, targeted reading, and code-search signals that warrant review.

## Decision

Do **not** rewrite UCF wholesale.

Use five dispositions:

1. **PRESERVE** — compatible with the stronger framework and useful as written.
2. **EXTEND** — basically sound but missing the state/transition/history/future-possibility distinction.
3. **RE-AUDIT** — contains domain claims or cross-domain transfers that need source-level verification.
4. **SUPERSEDE ACTIVE CLAIM** — preserve historical text, but current navigation/model must explicitly reject or replace the claim.
5. **ARCHIVE / RETIRE IF NO ADDED VALUE** — after comparison, move out of active analytical use if the concept adds no discriminating value.

---

## A. Preserve / extend rather than rewrite

### Current UCF framing

- `README.md`
- `models/ucf-model-v1.1-draft.md`
- `docs/claims.md`
- `docs/evidence.md`
- `docs/reconciliation-2026-09-16.md`
- `models/examples/booking-service/`

Why:

- already treats UCF as exploratory;
- separates functional fit, relational consequences, and normative judgment;
- keeps four layers separate from optional state labels;
- requires boundaries and timescales;
- rejects a universal score;
- explicitly allows labels to be omitted;
- contains failure/retirement conditions;
- already says structural similarity is not shared mechanism.

Needed migration:

- extend the temporal layer with current-state vs. transition-dynamics change;
- add retained history, future possibility, lock-in, and revision power;
- compare agency language against capabilities, viability/reachability, and empowerment rather than claiming new metrics.

This work is in the current draft PR.

---

## B. High-priority foundation re-audit

### `docs/foundations/coherence-and-systems-theory.md`

Signals:

- presents one cross-domain definition as "coherence in systems theory";
- calls four UCF states generalized attractor categories;
- claims multi-level coherence is necessary across domains;
- describes itself as a core scientific foundation.

Current disposition:

**SUPERSEDE ACTIVE CLAIM / REWRITE AFTER SOURCE AUDIT.**

Preserve the historical page with an audit notice until a sourced replacement exists.

### `docs/foundations/ecological-stability-and-resilience.md`

Search signal:

- contains Chaos → Tension → Flow → Unity language.

Needed check:

- separate Holling-style resilience from stability;
- distinguish resilience, adaptability, and transformability;
- remove any state ranking that is not sourced within ecology.

Current disposition:

**RE-AUDIT.**

### `docs/foundations/resilience-engineering-and-organizational-coherence.md`

Search signals:

- "scientific foundation";
- broad biological/artificial/ecological/organizational transfer language.

Needed check:

- review resilience-engineering definitions within their own domain;
- distinguish graceful degradation, recovery, robustness, adaptation, and transformation;
- test whether "organizational coherence" is the source's term or UCF interpretation.

Current disposition:

**RE-AUDIT.**

### `docs/foundations/noise-entropy-and-complexity-science.md`

Search signal:

- generalized-attractor language.

Existing issue:

- UCF already corrected some entropy/compression overreach.

Needed check:

- identify exact technical measures;
- separate information, thermodynamic, and dynamical uses;
- remove automatic mapping to UCF states.

Current disposition:

**RE-AUDIT.**

### `docs/foundations/multi-agent-communication-theory.md`

Search signals:

- Chaos → Tension → Flow → Unity;
- "scientific foundation."

Needed check:

- distinguish communication/coordination results from UCF state extrapolation;
- identify whether synchronization is actually desirable or necessary in each cited model.

Current disposition:

**RE-AUDIT.**

### `docs/foundations/predictive-processing-and-coherence.md` and `distributed-cognition.md`

Existing known problem:

- identical blobs at the audited base despite different filenames.

Additional search signals:

- Chaos → Tension → Flow → Unity;
- "scientific foundation."

Current disposition:

**BLOCKED / SOURCE RECOVERY FIRST.**

Do not invent missing content or treat either page as a verified distinct foundation.

---

## C. High-priority speculation correction

### Already bannered in the current PR

- `coherence-attractors-and-basins.md`
- `coherence-resilience-and-adaptation.md`
- `coherence-developmental-trajectories.md`
- `cross-scale-coherence.md`

Reasons:

- universalized attractor language;
- UCF state maturity/development sequence;
- unsourced resilience ranking;
- technical metastability generalized as a broad principle;
- universal cross-scale requirements.

Disposition:

**PRESERVE AS HISTORICAL SPECULATION + SUPERSEDE ACTIVE CLAIMS.**

### Next speculation pages to audit

Search results indicate likely follow-up review for:

- `coherence-emergence-pathways.md`
- `emergent-coherence-diagnostics.md`
- `coherence-phase-transitions.md`
- `coherence-resource-dynamics.md`
- `coherence-agency-and-autonomy.md`
- `coherence-constraints-and-limits.md`
- `coherence-incentives-and-game-dynamics.md`
- `coherence-information-dynamics.md`
- `coherence-networks-and-topologies.md`
- `coherence-coordination-and-synchronization.md`
- `coherence-ethics-and-cross-intelligence-safeguards.md`
- `coherence-tradeoffs-and-tensions.md`
- `coherence-infrastructure.md`
- `coherence-memory-and-temporality.md`

These files are not pre-judged false. They are flagged because search found phrases such as:

- `coherence requires`;
- broad "across biological, artificial, ecological..." transfer;
- Flow/Unity state claims;
- technical terms used outside their checked domains.

Disposition:

**RE-AUDIT IN BATCHES, NOT MASS REWRITE.**

---

## D. Interpretation layer

Search found many pages containing formulations such as "Unity is..." across:

- embodiment;
- creativity;
- connection;
- meaning;
- systems;
- society;
- liberation;
- communication;
- intelligence;
- consciousness;
- subjectivity;
- ethics;
- culture;
- emotion;
- attention.

This is not automatically a problem.

The Interpretation layer is allowed to explore meanings, metaphors, and philosophical proposals.

Migration rule:

> **Do not rewrite an interpretation merely because it is non-empirical. Rewrite or relabel only when it is presented as a domain result, universal mechanism, or necessary developmental fact.**

Disposition:

**PRESERVE BY DEFAULT; AUDIT boundary language where empirical claims appear.**

---

## E. Publications

Search identified `publications/UCF-Scientific-Overview.md` as using "scientific foundation" language.

A publication can be more consequential than an internal note because readers may reasonably infer stronger review.

Disposition:

**HIGH-PRIORITY PUBLICATION AUDIT.**

Questions:

- Does it predate the v1.1 corrections?
- Does it still present the state taxonomy as established?
- Are citations primary and scoped?
- Does the title/status imply peer review or validation that did not occur?
- Should it be marked historical, revised, or withdrawn from active publication navigation?

---

## F. Quantitative search signals from the 2026-09-24 scan

These are **triage signals**, not evidence that every occurrence is wrong.

| Query | Matching files |
| --- | ---: |
| exact `Chaos → Tension → Flow → Unity` | 7 |
| `generalized attractor` | 2 |
| exact `These requirements are universal` | 1 |
| exact `Flow has optimal` | 1 |
| `metastab` | 2 |
| `allostasis` | 2 |
| phrase `coherence requires` | 10 |
| phrase `scientific foundation` | 12 |
| phrase `across biological, artificial, ecological` | 11 |
| phrase `Unity is` | 24 |

A search match is only a reason to inspect context.

---

## G. Migration order

### Pass 1 — active model and navigation

Already underway:

- v1.1 temporal extension;
- evidence reconciliation;
- speculation/foundation warnings;
- current navigation status.

### Pass 2 — foundation claim audit

Prioritize:

1. systems theory;
2. ecological resilience;
3. resilience engineering;
4. information/entropy;
5. multi-agent communication;
6. predictive processing / distributed cognition source recovery.

For each consequential claim:

- exact claim;
- claim type;
- source;
- inspected portion;
- domain boundary;
- what UCF adds;
- transfer step;
- alternative explanation;
- revision trigger.

### Pass 3 — speculation batches

Review by concept family rather than file order:

- dynamical systems: attractors, phase transitions, criticality;
- adaptation: resilience, development, evolution;
- agency: autonomy, incentives, constraints;
- information: signal integrity, information dynamics;
- multi-scale: networks, synchronization, cross-scale claims;
- future intelligence: hybrid / mesh / distributed-self material.

### Pass 4 — interpretation and publications

- interpretation: boundary-language audit only;
- publications: stronger source/status review because of public-facing authority.

### Pass 5 — retirement decisions

After comparative testing, ask:

- Do the four labels add discriminating information?
- Does "dynamic coherence" add findings beyond existing methods?
- Which terms should remain poetic/interpretive?
- Which should become optional local descriptors?
- Which should leave active analytical use entirely?

---

## H. Rewrite rule

Rewrite when at least one is true:

1. the active text states something the checked evidence contradicts or does not support;
2. a technical term is used as though its meaning transfers universally;
3. the text implies a required developmental sequence without evidence;
4. the text collapses function, agency, legitimacy, consciousness, or welfare;
5. a newer model has explicitly superseded the claim;
6. leaving the page unchanged would likely mislead a reasonable reader about current UCF status.

Do **not** rewrite merely because:

- the language is old;
- the page is philosophical;
- a metaphor is imperfect but clearly labeled;
- a new framework says the same thing more elegantly;
- historical provenance would be lost.

---

## I. Working answer to "does this change everything?"

**Architecturally: yes, potentially.**

The new synthesis changes what UCF should ask about **time, adaptation, history, future possibility, and power over revision**.

**Epistemically: no, not by itself.**

An exciting synthesis does not retroactively validate itself or invalidate all prior work.

The responsible response is:

> **keep what survives the stronger model, correct what the stronger evidence rules expose, compare against existing methods, and allow the framework to shrink if the comparison shows it should.**

That is a more important kind of coherence than making every document say the same thing.
