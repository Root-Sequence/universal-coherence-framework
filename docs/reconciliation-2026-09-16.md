# UCF and the Root Sequence living paper

**Date:** 2026-09-16. **Status:** AI-assisted revision candidate; author review pending.  
**UCF source baseline:** `78277d3f3e54f4150e71fcdf7aab589a4fcb9f38`.  
**Paper baseline:** `cc90276d2b165c070f77401772b480ae2ba1fe84`, [draft PR #6](https://github.com/Root-Sequence/root-sequence/pull/6).

## Why reconcile them

The first paper draft used Root Sequence's general coherence model but omitted the dedicated UCF specification and glossary from its source map. UCF itself contained several overlapping definitions and a careful README alongside stronger older claims. The response is to compare them explicitly, not make a new synthesis silently replace the earlier model.

## Definition map

| Existing formulation | Retained contribution | Clarification in the candidate |
|---|---|---|
| UCF model v1: internal states, external behavior, temporal trajectories | Internal, inter-agent, systemic, and temporal layers | Separate scales and observations; no assumed common metric. |
| Earlier UCF glossary: stable, integrated, functional whole | Relationships and coordination | Stability and integration need not be goals in every context; protective separation and ending a pattern can matter. |
| Root Sequence overview and general coherence model: assumptions/model versus reality | Checking actual operating conditions | A matching local model does not establish wider benefit or legitimacy. |
| Living paper C-003: functional fit versus normative legitimacy | Explicitly contestable purposes and authority | A working definition still needs operationalization; definitions alone are not measurements. |

The [v1.1 draft](../models/ucf-model-v1.1-draft.md) is a proposed UCF home for the reconciliation. The paper can summarize and challenge it. UCF's four-layer model and four state labels are different structures; the booking example examines both without forcing a stage sequence.

## Roles and placement

UCF owns its particular model, glossary, UC-series claims, and [constructed example](../models/examples/booking-service/README.md). The paper owns the broader argument and C-series claims. Its source stays at `Root-Sequence/root-sequence/research/papers/coherent-systems/`; it links to the detailed UCF example rather than hosting a second implementation.

Root Sequence's general systems documents remain valid independent inquiry. Coherent World and No One Noticed are design and narrative contexts, not evidence or automatically updated canon. No other project's source, domain, permission, or deployment is changed by this reconciliation.

## Issue #1: current disposition

The contribution filename and optional-framework README framing had already been corrected on main before this pass. Other original tasks were still incomplete. This candidate corrects navigation, adds project-level citation metadata, establishes a claims convention, qualifies the glossary and time essay, and preserves earlier wording in [exact snapshots](archive/README.md).

The tracker must remain open: a claim-by-claim foundations audit, domain bibliographies, publication review, and comparative validation have not been completed. The duplicate predictive-processing/distributed-cognition blobs require source recovery, not invented replacement prose. Current indices no longer certify those files as a finished empirical foundation.

## What was actually exercised

The booking script computes a specified finite example and 24 sensitivity fixtures. Eight implementation tests passed. Four contrasting cases were examined editorially; no independent reviewers or participants were involved. No test establishes the framework's universality, a preferred social rule, or improved performance over a competent baseline.

## What remains to decide

The author should review the fit/legitimacy distinction, the scope of each layer, and whether state labels deserve further development. The current comparison allows labels to be retained with local criteria, renamed, or omitted; it does not decide that for every application.

The remaining evidence audit is a defined task, not a claim that all existing work is wrong. Preserve hypotheses and philosophical work under explicit labels while checking factual assertions against their sources.

[Changelog](../CHANGELOG.md) · [Existing issue #1](https://github.com/Root-Sequence/universal-coherence-framework/issues/1)
