# Architecture Canvas

Use this structure for a full architecture blueprint. Omit empty sections only when they are genuinely inapplicable.

## 1. Verdict

Summarize the recommended architecture, dominant tradeoff, maturity level, and largest unresolved risk in one paragraph.

## 2. Evidence and assumptions

Create four short lists:

- Observed: verified from inputs or repository evidence.
- Inferred: likely but not proven.
- Assumed: selected to keep work moving.
- Unknown: requires owner decision or measurement.

Never merge these categories.

## 3. Product contract

Define:

- Primary user and economic buyer.
- Core job and success event.
- Revenue or entitlement event.
- Sensitive and regulated actions.
- Availability and latency expectations.
- Explicit first-release non-goals.

## 4. Boundary view

Map these logical surfaces even when they deploy together:

- Customer experience: discovery, purchase, use, account controls.
- Operator control plane: catalog, configuration, publishing, support, safety, audit, cost.
- Core API: identity, entitlement, business workflows, durable state.
- Workers: ingestion, indexing, reconciliation, notifications, long-running tasks.
- Integrations: payments, communications, storage, AI providers, analytics, external systems.

For each boundary, record identity, allowed data, write authority, failure owner, and audit requirement.

## 5. Capability map

Group capabilities around business invariants, not framework folders. A common AI SaaS starting map is:

1. Identity and access
2. Catalog and configuration
3. Commerce and entitlement
4. AI runtime and provider gateway
5. Conversation or job execution
6. Knowledge and retrieval
7. Safety and policy
8. Usage, cost, and quota
9. Operations and audit
10. External data ingestion and review

Recommend a modular monolith by default. Split a capability only when at least one driver is measured: incompatible scaling, strict fault isolation, different security boundary, independent ownership and release cadence, or technology requirements that cannot coexist cleanly.

## 6. Critical flows

For every critical flow, write:

`actor -> admission -> authorization -> durable write -> external effect -> confirmation -> derived updates -> audit -> recovery`

Include timeout, retry, duplicate, cancellation, and partial-success behavior.

### AI execution invariant

Authorize entitlement and reserve quota before provider execution. Assign one request ID across safety checks, provider attempts, streaming, usage, and audit. A fallback attempt must never result in two committed answers or ambiguous billing.

### Payment invariant

Verify notification authenticity, persist the raw event securely, deduplicate by provider transaction and event identity, transition order state transactionally, grant entitlement exactly once, and reconcile independently.

### Publishing invariant

Run traffic only on immutable published versions. Draft edits create a new version; rollback selects a prior version and records the actor and reason.

### Ingestion invariant

Normalize external records into a canonical contract, deduplicate by source identity, preserve evidence, score completeness, and represent missing data as unknown rather than zero.

## 7. State machines and invariants

Model at least the states and legal transitions for:

- Order and payment
- Subscription or entitlement
- Publishable configuration
- Long-running ingestion or indexing job
- AI request or conversation turn
- Alert or manual review

For each transition, identify command, guard, idempotency key, durable event, side effects, and compensating or recovery action.

## 8. Data ownership

Create a table with: data domain, system of record, write owner, retention, sensitivity, derivatives, recovery source.

Use a relational database for durable transactional facts unless evidence demands otherwise. Treat cache, search, analytics, and vector stores as derivatives with explicit rebuild paths. Keep financial, usage, security, and audit trails append-oriented.

## 9. Runtime topology

Show deployment units, ingress, private network boundaries, databases, cache, object storage, queue or event transport, external providers, secret storage, logs, metrics, traces, and backup path. Logical separation does not require immediate service separation.

## 10. Cross-cutting controls

Cover:

- Authentication, authorization, tenant isolation, and privileged access.
- Encryption, secret rotation, data minimization, retention, deletion, and audit.
- Rate limits, quotas, budgets, per-tenant cost attribution, and abuse controls.
- Structured logs, correlation IDs, golden signals, business signals, and alert ownership.
- Backups, restore objectives, degraded modes, reconciliation, and rollback.

## 11. Failure register

Rank failures by impact and likelihood. Include trigger, blast radius, detection, containment, recovery, and preventive test. Cover provider outage, duplicate external events, database pressure, stale authorization, poison messages, bad configuration, migration failure, and runaway cost.

## 12. Delivery roadmap

- Now: smallest architecture that closes the commercial and safety loop.
- Next: reliability and operational controls justified by observed usage.
- Later: decomposition or specialized infrastructure tied to explicit thresholds.

For every phase, list acceptance evidence, not only tasks.

## 13. ADR queue

Capture each consequential decision as: context, options, decision, consequences, reversal cost, owner, and review trigger.

## 14. Next decisions

End with the three decisions that most reduce uncertainty or production risk.
