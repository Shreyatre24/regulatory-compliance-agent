# Architecture

The pipeline is deliberately small and inspectable. Each stage has one job and a stable
input/output shape, so any stage can be swapped or upgraded without touching the others.

```
        ┌─────────────────────────────────────────────────────────────────┐
        │                          run(regulation, product)                 │
        └─────────────────────────────────────────────────────────────────┘
                                        │
        regulation_text, product_text   ▼
        ┌───────────┐   requirements   ┌────────────┐   clauses   ┌──────────┐
        │  Planner  │ ───────────────▶ │  Retriever │ ──────────▶ │  Writer  │
        │ (LLM)     │  [{id, req, …}]  │  (RAG)     │  [clause…]  │  (LLM)   │
        └───────────┘                  └────────────┘             └────┬─────┘
                                                                       │ assessment
                                                                       ▼
                                                                 ┌───────────┐
                                                                 │ Validator │  schema check
                                                                 │ (critic)  │
                                                                 └────┬──────┘
                                                                      ▼
                                                                 ┌───────────┐
                                                                 │ Run store │  runs/<ts>-<hash>/
                                                                 │(versioned)│  inputs.json + report.json
                                                                 └───────────┘
```

## Stages

- **Planner** — decomposes the regulation (+ product context) into discrete, checkable
  requirements. This is the agentic "brain": the reasoning about *how* to break a regulation
  into an actionable checklist. Mirrors the Planner in a Planner/Executor split.
- **Retriever (RAG)** — for each requirement, returns the most relevant regulation clauses as
  grounding evidence. v0.1 can be naive (keyword / simple similarity); a vector store is v0.2.
- **Writer** — drafts one assessment per requirement `{id, status, rationale, evidence}`,
  conforming to the schema. Schema-oriented generation keeps output structured and parseable.
- **Validator (critic)** — cheap, deterministic check that every assessment matches the schema
  and uses a valid status. Makes the output trustworthy and traceable.
- **Run store** — persists every run with its inputs and output under a timestamped, hashed id,
  so any result is reproducible and diffable across runs.

## Design principles

- **Stable shapes between stages** — components are swappable in isolation.
- **Green from minute one** — stubs return valid mock data so the pipeline always runs; you
  replace stubs incrementally without ever having a broken repo.
- **Traceability over cleverness** — every conclusion carries its evidence and passes a schema check.

## Roadmap (not built yet — and that's fine to show)

- v0.2 — real vector retrieval (chunk + embed + top-k) over full regulation PDFs.
- v0.3 — evaluation harness: gold requirements + precision/recall on gap detection.
- v0.4 — DOCX report generation from the validated JSON (python-docx).
- v0.5 — multi-regulation support and a simple CLI report viewer.
