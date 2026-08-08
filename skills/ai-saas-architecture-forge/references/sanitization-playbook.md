# Sanitization Playbook

Use this playbook before architecture material leaves its source context.

## Sanitization objective

Retain transferable reasoning while removing facts that identify the source product, organization, customers, infrastructure account, or commercial playbook. Sanitization is a transformation, not a find-and-replace pass.

## Transform proprietary detail

| Source detail | Safe abstraction | Preserve |
|---|---|---|
| Product, company, or internal codename | `the platform`, `the service`, or a fictional neutral name | Role in the system |
| Named team or individual | `operator`, `administrator`, `analyst`, `support`, `customer` | Responsibility and permission |
| Customer, tenant, lead, or partner identity | Synthetic actor such as `tenant-a` | Multi-tenant relationship |
| Domain, IP, account ID, region-specific endpoint | `customer.example`, `admin.example`, `api.example`, or `<private-endpoint>` | Boundary and routing intent |
| Vendor-specific product | Capability class such as relational database, cache, object storage, queue, model provider | Required semantics; mention vendor only when essential |
| Exact internal metric name | Generic metric family such as conversion, retention, latency, quality, cost | Calculation and decision use |
| Exact commercial threshold | Qualitative trigger or rounded illustrative range | Direction and consequence |
| Proprietary department taxonomy | Capability group A/B or acquisition, conversion, delivery, support | Data contract and review cadence |
| Database or API name carrying business DNA | Neutral entity or endpoint pattern | Cardinality, lifecycle, idempotency |
| Real payload or content | Minimal synthetic example | Shape and validation rule |

## Remove completely

- Credentials, tokens, cookies, session material, private keys, certificates, hashes derived from secrets, and credential-like example values.
- Personal data, customer content, payment identifiers, phone numbers, email addresses, and support transcripts.
- Private repository URLs, internal ticket links, cloud account identifiers, production hostnames, and network coordinates.
- Raw webhook bodies, production logs, database dumps, analytics exports, and screenshots containing live data.
- Undisclosed vulnerabilities or operational shortcuts that would create a practical attack path.

## Preserve architecture truth

Keep these when they are expressed generically:

- Trust boundaries and who may cross them.
- State transitions, invariants, idempotency keys, append-only requirements, and recovery behavior.
- System-of-record decisions and which derivatives can be rebuilt.
- Reasons for separating customer, operator, API, worker, and integration surfaces.
- Failure containment, model fallback rules, cost attribution, audit requirements, and migration discipline.
- Delivery sequencing and measurable triggers for future decomposition.

## Check the final artifact

1. Search case-insensitively for source product names, repository names, organization names, people, domains, emails, phone-like strings, IP addresses, UUIDs, access keys, tokens, and cloud resource identifiers.
2. Search for environment assignments and URLs. Keep only unmistakably synthetic placeholders.
3. Search for exact internal thresholds, department names, aliases, and payload field names.
4. Inspect examples manually; synthetic data can still accidentally reproduce real data.
5. Confirm the artifact cannot be reverse-mapped to a specific customer, account, or private repository from its wording alone.
6. State that the output is an independent abstraction and contains no copied proprietary source code.

If a reusable principle cannot be explained without revealing a source-specific fact, omit it.
