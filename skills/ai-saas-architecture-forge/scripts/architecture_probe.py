#!/usr/bin/env python3
"""Create a sanitized, evidence-oriented architecture inventory for a repository."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


SKIP_DIRS = {
    ".git", ".hg", ".svn", ".next", ".nuxt", ".turbo", ".venv", "venv",
    "node_modules", "dist", "build", "coverage", "target", "vendor",
}
TEXT_SUFFIXES = {
    ".cjs", ".css", ".env", ".go", ".graphql", ".html", ".java", ".js",
    ".json", ".jsx", ".kt", ".md", ".mjs", ".php", ".prisma", ".py",
    ".rb", ".rs", ".sh", ".sql", ".toml", ".ts", ".tsx", ".yaml", ".yml",
}
MAX_FILE_BYTES = 1_000_000

SIGNALS = {
    "identity-and-access": [r"\bauth(?:entication|orization)?\b", r"\bsession\b", r"\boauth\b", r"\brbac\b"],
    "commerce-and-entitlement": [r"\bpayment\b", r"\border\b", r"\bsubscription\b", r"\bentitlement\b", r"\brefund\b"],
    "ai-runtime": [r"\bmodel.?provider\b", r"\bprompt\b", r"\btoken.?count\b", r"\bstream(?:ing)?\b", r"\bembedding\b"],
    "knowledge-and-retrieval": [r"\bknowledge.?base\b", r"\bvector\b", r"\bretriev", r"\bchunk(?:ing)?\b"],
    "safety-and-audit": [r"\bsafety\b", r"\bmoderation\b", r"\baudit\b", r"\bpolicy\b"],
    "operations-and-observability": [r"\bmetric", r"\balert", r"\btelemetry\b", r"\btrace", r"\breconciliation\b"],
    "asynchronous-work": [r"\bqueue\b", r"\bworker\b", r"\bjob\b", r"\bwebhook\b", r"\bevent\b"],
}

TECHNOLOGIES = {
    "relational-database": [r"postgres", r"mysql", r"sqlite", r"sqlserver"],
    "cache-or-broker": [r"redis", r"memcached", r"rabbitmq", r"kafka"],
    "object-storage": [r"\bs3\b", r"object.?storage", r"\bcos\b", r"\bblob\b"],
    "container-runtime": [r"dockerfile", r"docker.?compose", r"kubernetes", r"\bk8s\b"],
    "infrastructure-as-code": [r"terraform", r"pulumi", r"cloudformation"],
    "schema-or-migrations": [r"prisma", r"typeorm", r"sequelize", r"alembic", r"flyway", r"liquibase"],
}

SECRET_PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "credential-assignment": re.compile(
        r"(?im)^\s*[A-Z][A-Z0-9_]*(?:SECRET|TOKEN|PASSWORD|PRIVATE_KEY|API_KEY)[A-Z0-9_]*\s*=\s*(?!\s*(?:$|<|\$\{|replace|example|changeme))\S+"
    ),
    "bearer-token": re.compile(r"(?i)authorization\s*[:=]\s*bearer\s+[a-z0-9._~+/=-]{16,}"),
    "credential-url": re.compile(r"(?i)\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s/@:]+:[^\s/@]+@"),
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            if path.stat().st_size > MAX_FILE_BYTES:
                continue
        except OSError:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {
            "Dockerfile", "Makefile", ".env", ".env.example", "package.json",
        }:
            yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def count_matches(text: str, patterns: list[str]) -> int:
    lowered = text.lower()
    return sum(len(re.findall(pattern, lowered, flags=re.IGNORECASE)) for pattern in patterns)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Repository root to inspect")
    parser.add_argument("--output", type=Path, help="Write Markdown report to this path")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    file_counts: Counter[str] = Counter()
    capability_counts: Counter[str] = Counter()
    technology_counts: Counter[str] = Counter()
    secret_counts: Counter[str] = Counter()
    manifest_counts: Counter[str] = Counter()
    total_files = 0

    manifest_names = {
        "package.json": "node-package",
        "pyproject.toml": "python-package",
        "requirements.txt": "python-requirements",
        "go.mod": "go-module",
        "Cargo.toml": "rust-package",
        "pom.xml": "jvm-package",
        "build.gradle": "jvm-package",
        "docker-compose.yml": "container-compose",
        "docker-compose.yaml": "container-compose",
        "Dockerfile": "container-image",
    }

    for path in iter_files(root):
        total_files += 1
        file_counts[path.suffix.lower() or "[no extension]"] += 1
        if path.name in manifest_names:
            manifest_counts[manifest_names[path.name]] += 1
        text = read_text(path)
        if not text:
            continue
        for name, patterns in SIGNALS.items():
            if count_matches(text, patterns):
                capability_counts[name] += 1
        evidence = f"{path.name}\n{text}"
        for name, patterns in TECHNOLOGIES.items():
            if count_matches(evidence, patterns):
                technology_counts[name] += 1
        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                secret_counts[name] += 1

    lines = [
        "# Sanitized Architecture Probe",
        "",
        "> This report contains category-level evidence only. It intentionally omits source paths, names, URLs, payloads, and matched secret values.",
        "",
        "## Repository shape",
        "",
        f"- Scanned text files: {total_files}",
        f"- File types observed: {len(file_counts)}",
        "- Largest text groups: " + (", ".join(f"`{k}` ({v})" for k, v in file_counts.most_common(8)) or "none"),
        "",
        "## Build and delivery evidence",
        "",
    ]
    lines.extend(f"- {name}: evidence in {count} file(s)" for name, count in sorted(manifest_counts.items()))
    if not manifest_counts:
        lines.append("- No common build manifest detected")

    lines.extend(["", "## Capability signals", ""])
    lines.extend(f"- {name}: evidence in {count} file(s)" for name, count in sorted(capability_counts.items()))
    if not capability_counts:
        lines.append("- No configured capability signal detected")

    lines.extend(["", "## Infrastructure signals", ""])
    lines.extend(f"- {name}: evidence in {count} file(s)" for name, count in sorted(technology_counts.items()))
    if not technology_counts:
        lines.append("- No configured infrastructure signal detected")

    lines.extend(["", "## Secret hygiene gate", ""])
    if secret_counts:
        lines.append("- FAIL: credential-like material was detected. Inspect the source locally before sharing any derivative artifact.")
        lines.extend(f"- {name}: detected in {count} file(s); values and locations suppressed" for name, count in sorted(secret_counts.items()))
    else:
        lines.append("- PASS: no configured credential pattern was detected. This is not a substitute for a dedicated secret scanner or manual review.")

    lines.extend([
        "",
        "## Interpretation rules",
        "",
        "- Counts show evidence presence, not implementation completeness.",
        "- Verify runtime behavior in representative modules before making an architecture claim.",
        "- Keep observed, inferred, assumed, and unknown facts separate.",
        "- Apply the sanitization playbook before publishing any blueprint.",
    ])

    report = "\n".join(lines) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 1 if secret_counts else 0


if __name__ == "__main__":
    raise SystemExit(main())
