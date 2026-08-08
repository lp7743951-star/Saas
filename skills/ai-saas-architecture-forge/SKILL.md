---
name: ai-saas-architecture-forge
description: Turn an AI SaaS idea, product brief, or existing repository into an evidence-backed, production-ready architecture blueprint. Use when Codex must design or review product boundaries, customer and operator surfaces, modular services, data ownership, state machines, AI model routing, subscriptions or payments, safety and audit controls, deployment topology, migration strategy, operational feedback loops, or phased delivery while removing proprietary names, credentials, URLs, customer data, and organization-specific fingerprints.
---

# AI SaaS Architecture Forge

Forge a product idea or codebase into a defensible architecture. Separate observed evidence, design decisions, assumptions, and unresolved risks; never present repository guesses as facts.

## Choose the operating mode

- Use **greenfield mode** when the input is a brief or idea. Mark unknowns explicitly and offer a minimal decision set.
- Use **repository mode** when source files exist. Inspect the repository before proposing changes.
- Use **review mode** when an architecture already exists. Preserve sound decisions, expose contradictions, and rank gaps by production risk.
- Modify code only when the user asks for implementation. Otherwise deliver a blueprint or review without mutating the source repository.

## Run the forge

1. Establish the product contract.
   - State users, buyer, core job, revenue event, regulated or high-risk actions, service-level expectation, and explicit non-goals.
   - Ask only for decisions that materially change architecture. Otherwise make a labeled assumption and continue.

2. Collect evidence.
   - In repository mode, run `python scripts/architecture_probe.py <repo-root> --output <report.md>` from this skill directory.
   - Read the generated report, manifests, existing architecture docs, deployment files, schema or migrations, and the smallest set of representative modules needed to verify boundaries.
   - Treat folder names and frameworks as clues, not proof of runtime behavior.

3. Sanitize before synthesis.
   - Read [references/sanitization-playbook.md](references/sanitization-playbook.md).
   - Replace brands, people, tenants, domains, provider account details, proprietary taxonomies, exact commercial thresholds, internal codenames, and source-specific field names with neutral roles or ranges.
   - Never copy secrets, tokens, private endpoints, customer content, raw webhook bodies, or production identifiers into outputs.
   - Preserve reusable decisions and invariants, not proprietary implementation fingerprints.

4. Draw product and trust boundaries.
   - Separate the customer experience, operator control plane, core application API, asynchronous workers, and external integrations.
   - Assign identity, authorization, data ownership, and failure responsibility at every boundary.
   - Keep management capability out of customer surfaces and prevent browsers from directly owning privileged provider credentials.

5. Trace critical journeys end to end.
   - Trace identity and session lifecycle.
   - Trace purchase, payment notification, entitlement, renewal, expiration, refund, and reconciliation when monetization exists.
   - Trace AI request admission, safety checks, context assembly, provider routing, streaming, usage accounting, and failure fallback.
   - Trace configuration draft, versioning, publishing, rollback, and audit when operators manage runtime behavior.
   - Trace ingestion, normalization, idempotency, evidence, data quality, alerting, and review when external operational data exists.

6. Derive the architecture.
   - Use [references/architecture-canvas.md](references/architecture-canvas.md) for the required views and decision records.
   - Define capability boundaries before selecting services.
   - Define state machines and invariants before endpoints.
   - Assign one system of record for each durable fact; use caches, search indexes, and vectors only as rebuildable derivatives.
   - Keep irreversible financial, entitlement, security, and audit events append-oriented and idempotent.
   - Prefer a modular monolith until scale, isolation, ownership, or independent release evidence justifies a split.

7. Pressure-test production readiness.
   - Read [references/production-gates.md](references/production-gates.md).
   - Test the design against duplicate events, partial failure, provider outage, timeout, retry storms, stale authorization, bad migrations, secret leakage, tenant crossover, cost runaway, missing evidence, and rollback.
   - Do not call a system production-ready while any applicable critical gate is unresolved.

8. Deliver the blueprint.
   - Lead with a one-paragraph architecture verdict.
   - Include evidence and assumptions, product boundaries, capability map, critical flows, state machines and invariants, data ownership, runtime topology, security/cost/observability controls, failure modes, phased roadmap, and an ADR queue.
   - Distinguish **now**, **next**, and **later**. Tie every later split or technology addition to a measurable trigger.
   - End with the top three decisions the team must make next.

## Apply the quality bar

- Reject decorative diagrams that do not show ownership, trust, state, or failure behavior.
- Reject technology shopping lists without decision drivers.
- Reject direct coupling between payment callbacks and non-idempotent entitlement mutation.
- Reject AI fallback that can silently duplicate billing or stream two answers.
- Reject mutable prompts or policies without versions and rollback.
- Reject dashboards that hide missing data by inventing zeroes or estimates.
- Reject production migrations that depend on development-only schema push behavior.
- Prefer explicit unknowns over fabricated precision.

## Use concise deliverables

For a small request, return the verdict, one boundary view, one critical flow, top risks, and the next decisions. For a full architecture request, follow every section in [references/architecture-canvas.md](references/architecture-canvas.md). Use Mermaid only when it makes a boundary, state transition, or failure path easier to verify.
