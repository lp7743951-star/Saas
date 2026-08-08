# Production Gates

Classify each applicable gate as `pass`, `conditional`, `fail`, or `unknown`. A critical `fail` or `unknown` prevents an unqualified production-ready verdict.

## Product and ownership

- Every surface has a named user, owner, permission model, and non-goal.
- Every critical workflow has a success definition and a recovery owner.
- Operator-only controls are isolated from customer surfaces.

## Identity and tenant isolation

- Server-side authorization is enforced for every protected resource.
- Tenant identity comes from trusted authentication context, not client-supplied ownership fields.
- Privileged actions require stronger controls and durable audit records.
- Session revocation, expiry, credential rotation, and account deletion are defined.

## Commerce and entitlement

- Money uses an exact decimal or integer minor-unit representation.
- Payment notifications are authenticated, persisted, deduplicated, and replay-safe.
- Order, payment, refund, and entitlement have explicit state machines.
- Entitlement changes are exactly-once from the business perspective.
- Reconciliation can repair missed or out-of-order external events.

## AI runtime

- Provider credentials remain server-side and encrypted or secret-managed.
- Requests carry one correlation ID through admission, policy, provider, usage, and audit.
- Timeout, cancellation, retry, and fallback have bounded budgets.
- Fallback cannot commit duplicate output or duplicate charge.
- Prompt, model, tool, and policy configurations are versioned and reversible.
- Input and output safety handling is explicit for the product risk class.
- Per-request, per-user, per-tenant, and global cost controls exist where applicable.

## Data and integration

- Every durable fact has one system of record and one write owner.
- External events have stable source identity or a deterministic idempotency key.
- Missing data is represented explicitly and never silently converted into zero.
- Derived stores have a documented rebuild source and process.
- Retention, deletion, export, and evidence requirements match data sensitivity.

## Operations and resilience

- Logs are structured, secrets and personal data are redacted, and correlation is end to end.
- Metrics cover latency, traffic, errors, saturation, business conversion, provider health, and cost.
- Alerts have thresholds, owners, runbooks, and noise controls.
- Backups are automated; restore has been tested against recovery objectives.
- Dependency outages have deliberate degraded behavior.
- Queues have retry limits, dead-letter handling, poison-message isolation, and replay controls.

## Change and release

- CI verifies types or compilation, tests, artifacts, migrations, and secret scanning.
- Production uses reviewed migrations, not development schema synchronization.
- Destructive schema changes use expand, migrate, contract or an equivalent compatible sequence.
- Release supports health checks, progressive rollout, rollback, and post-deploy verification.
- Configuration and feature changes can be rolled back independently when practical.

## Verdict language

- Use **prototype-ready** when the happy path works but durable recovery and controls are incomplete.
- Use **pilot-ready** when limited real users are safe under active observation and manual recovery.
- Use **production-candidate** when critical gates pass but restore, scale, or operational evidence is incomplete.
- Use **production-ready** only when all applicable critical gates pass with tested evidence.
