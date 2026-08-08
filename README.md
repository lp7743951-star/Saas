# AI SaaS Architecture Forge

> **Stop shipping demo-shaped production systems.**

[![License: MIT](https://img.shields.io/badge/License-MIT-0b7285.svg)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-7c3aed.svg)](skills/ai-saas-architecture-forge/SKILL.md)
[![Cloud Neutral](https://img.shields.io/badge/Cloud-Neutral-111827.svg)](#what-it-forges)

Turn a product idea - or a living codebase - into an AI SaaS architecture that can survive real users, real money, real outages, and real audits.

**AI SaaS Architecture Forge** is a Codex Skill for the dangerous moment when "we have a frontend, an API, and an LLM call" starts getting mistaken for "we are ready for production."

It does not generate cloud-logo collages. It does not use microservice count as a proxy for intelligence. It does not disguise unknowns as confident architecture. It delivers boundaries, state machines, data ownership, failure behavior, production gates, and a roadmap a team can actually execute.

## Why this hits differently

Most architecture describes what happens when everything works. The Forge starts where reality breaks the happy path:

- Money moved, but entitlement did not. Who repairs it?
- A payment provider delivered the same event three times. What changes exactly once?
- The model timed out halfway through a stream. Can fallback produce a second answer or a second charge?
- A prompt, model, tool, or policy change went bad. Can operators roll back immediately?
- A cache, index, or vector store vanished. Which source rebuilds it?
- Why can a customer surface reach operator capability? Why can a browser touch provider secrets?
- Does a dashboard zero mean zero - or does it mean the data never arrived?
- Is this system production-ready, or has it merely survived one successful demo?

The Forge refuses to let "we will harden it later" close those questions.

## What it forges

- Product and trust boundaries across customer, operator, API, worker, and integration surfaces
- Capability maps that resist premature microservices
- End-to-end identity, commerce, entitlement, AI runtime, publishing, and ingestion flows
- Explicit state machines, invariants, idempotency keys, audit events, and recovery actions
- System-of-record and rebuildable-derivative decisions
- AI provider routing, bounded fallback, streaming, usage, safety, and cost controls
- Deployment topology, migration discipline, observability, backup, and rollback gates
- A `now / next / later` roadmap tied to evidence instead of architectural fashion

## Learn from private systems without leaking their DNA

The bundled architecture probe emits category-level evidence while suppressing source paths, matched values, domains, payloads, and internal names. The sanitization playbook strips organization fingerprints, customer information, commercial thresholds, and provider-account details while preserving reusable engineering decisions.

This repository is an independent abstraction. It contains no copied proprietary source code, credentials, customer data, private endpoints, or production identifiers.

## Install in 30 seconds

Copy the Skill into your Codex skills directory:

```bash
cp -R skills/ai-saas-architecture-forge ~/.codex/skills/
```

Then invoke it:

```text
Use $ai-saas-architecture-forge to turn this repository into a production-ready architecture blueprint.
```

Or pressure-test a narrower surface:

```text
Use $ai-saas-architecture-forge to review our payment, entitlement, and AI fallback design before launch.
```

## Three forge modes

| Mode | Input | Output |
|---|---|---|
| Greenfield | Idea, brief, or PRD | Smallest honest architecture, assumptions, non-goals, evolution triggers |
| Repository | Existing codebase | Evidence report, actual boundaries, risk gaps, production blueprint |
| Review | Existing architecture | Contradictions, failure analysis, maturity verdict, ADR queue |

## A full forge produces

1. A blunt architecture verdict
2. Observed / Inferred / Assumed / Unknown evidence
3. Product and trust boundaries
4. Capability map and split rules
5. Critical flows and failure paths
6. State machines, invariants, and idempotency
7. Data ownership and rebuild strategy
8. Runtime and deployment topology
9. Security, cost, observability, and recovery controls
10. Production gates and an honest maturity verdict
11. A `now / next / later` roadmap
12. The three decisions worth making next

## Repository layout

```text
skills/ai-saas-architecture-forge/
|-- SKILL.md
|-- agents/openai.yaml
|-- references/
|   |-- architecture-canvas.md
|   |-- production-gates.md
|   +-- sanitization-playbook.md
+-- scripts/architecture_probe.py
```

## The Forge doctrine

1. **Evidence before opinion.**
2. **Boundaries before services.**
3. **Invariants before endpoints.**
4. **Recovery before scale theater.**
5. **Measured triggers before decomposition.**
6. **Explicit unknowns before fabricated precision.**

## What it will not pretend to replace

This Skill supports architecture discovery, design, and review. It does not replace formal threat modeling, legal advice, compliance certification, capacity testing, professional secret scanning, or an accountable production owner.

It makes architecture more honest and harder for reality to break. It does not sell the fairy tale that one prompt magically certifies a production system.

## Contributing

Pressure-test the Forge with real architecture decisions, then open an issue or pull request with a minimal, sanitized reproduction. Never submit employer code, customer data, private URLs, credentials, production identifiers, or undisclosed vulnerabilities.

## License

MIT. Use it, fork it, sharpen it, and prevent the next "the demo worked, so ship it" incident.
