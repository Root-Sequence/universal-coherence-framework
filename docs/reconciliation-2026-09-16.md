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

## Recovery verification, 2026-09-16

The UCF draft survived at `c4d7b236828a59139c0d5204b1faaed13154682a`. The companion paper had only partly staged changes and no branch update. Its reconciliation was recovered and completed at [paper commit 20740c7](https://github.com/Root-Sequence/root-sequence/commit/20740c794a5a01b2d616abc6f74bad9dcf83054d), on the existing draft PR rather than a new paper repository.

Checks actually repeated in a fresh local runtime using Python 3.13.5:

- Fetched both Python files from the saved UCF revision and matched their exact Git blob hashes: `booking_model.py` = `a2153cd05550224a6fe358d9176bde9b40f823fc`; `test_booking_model.py` = `b3ff9557715d732dbd8ed56035b747c84b942264`.
- Reran the eight unittest tests, all passing. Reran the report: 24 distinct capacity/duration fixtures, three allocation rules per fixture, plus the base case. Base allocations remain `(2, 2)`, `(8, 0)`, and `(5, 1)` short/long requests; all leave 90 service minutes unmet.
- Six additional sanity checks passed: fixture count, fixture uniqueness, zero capacity, zero demand, refusal to overwrite an existing output, and clean failure for a missing output directory. These are implementation checks, not a comparison of research methods.
- Matched all nine companion-paper changed file hashes to their locally inspected contents. Checked 40 relative Markdown links in those files against prepared files or previously connector-verified repository paths. Checked twelve claim IDs, ten question IDs, three research-task IDs, five footnote definitions, five bibliography entries, and the 197-word abstract.
- Rechecked the six archived snapshot blob IDs against their originals. Parsed the saved CFF as YAML and checked required root fields and its source hash; no official CFF-schema validation or GitHub citation-render test was performed.
- Reopened the primary sources in the evidence log at its stated coverage: Shannon's introductory, entropy, and coding pages; the BABAR, Zurek, and Goodhart metadata/abstracts. This is not a complete literature review or reproduction of those studies.

The interrupted progress text mentioned a 700-case comparison with 561 completion-count matches. Its protocol and outputs were not recovered in the verified code, which implements the 24-fixture report above. The larger count is not adopted as a result. Neither a completion-count match nor the current toy example would establish that UCF improves a review method.

This recovery does not claim a full-repository link audit, rendered BibTeX validation, independent review, empirical findings, framework universality, author approval, or website deployment. Both repository branches and their pull requests are public drafts, not local-only or private workspaces.

## What remains to decide

The author should review the fit/legitimacy distinction, the scope of each layer, and whether state labels deserve further development. The current comparison allows labels to be retained with local criteria, renamed, or omitted; it does not decide that for every application.

The remaining evidence audit is a defined task, not a claim that all existing work is wrong. Preserve hypotheses and philosophical work under explicit labels while checking factual assertions against their sources.

[Changelog](../CHANGELOG.md) · [Existing issue #1](https://github.com/Root-Sequence/universal-coherence-framework/issues/1)
