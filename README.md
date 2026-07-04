# Regulatory Compliance Agent

An agentic pipeline that reads a **public regulation** and a **product/process description**,
then produces a structured, reviewable **compliance report** — flagging what's compliant, what's
a gap, and what needs a human. Built around a Planner → Retrieve → Write → Validate loop with
versioned, reproducible runs.

> Inspired by my MSc thesis on NLP-driven regulatory document automation (graded 1,0).
> This is the public, from-scratch sibling of that work, built on openly available regulations
> (e.g. UN/ECE vehicle-homologation regulations, the EU AI Act, GDPR) so anyone can run it.
>
> _TODO(you): replace this quote with one honest sentence in your own voice + a link to your LinkedIn._

## Why

Regulated, documentation-heavy processes are everywhere in industry, and checking a product or
process against a regulation by hand is slow and error-prone. This agent does a first pass: it
decomposes the regulation into checkable requirements, retrieves the relevant clauses, drafts an
assessment per requirement, and validates the output against a fixed schema — so results are
**traceable**, not a black box.

## Architecture (at a glance)

```
regulation.txt ─┐
                ├─▶ Planner ─▶ [requirements] ─▶ Retriever(RAG) ─▶ Writer ─▶ Validator ─▶ Run store
product.txt   ─┘                                                                          (versioned)
```

Full design in [ARCHITECTURE.md](ARCHITECTURE.md).

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # add your model API key when you wire up the LLM steps
python -m src.main            # runs end-to-end on the bundled sample files
```

Out of the box it runs with **stubbed components** and writes a versioned run to `runs/`.
That's intentional: you always have a green pipeline. Replace one stub at a time
(see [MILESTONES.md](MILESTONES.md)).

## Status

v0.1 — end-to-end pipeline with a working run store; agent components stubbed, being filled in.
Roadmap (evaluation harness, vector retrieval, DOCX report generation) is in ARCHITECTURE.md.
Honest status is a feature: it shows how the system is designed, not just what's finished.

## License

MIT — _TODO(you): keep or change._
