# Milestones

The rule: **every milestone is finishable in one sitting and ends with a commit.**
Bad-state days still produce a green commit. You never face a blank page or a broken repo.

## The 20-minute first win (do this before anything else)

- [ ] `python -m src.main` — watch the stubbed pipeline run and write a folder under `runs/`.
- [ ] `git init && git add . && git commit -m "v0.1: end-to-end pipeline (stubbed)"`.
- [ ] Create the GitHub repo and `git push`. **You now have a public, running project.** Done today.

Everything below just makes the stubs real, one at a time. The repo is already "out there."

## Fill the stubs (one per sitting)

- [ ] **Run store** — already works. Confirm you understand it; it's your "versioned runs" proof.
- [ ] **Schema** — read `src/schema.py`, adjust the statuses/fields to how you think about compliance.
- [ ] **Planner** (`src/planner.py`) — replace the stub with one LLM call that returns a JSON list of
      requirements from the regulation. This is the highest-signal file; it's your agentic reasoning.
- [ ] **Writer** (`src/writer.py`) — replace the stub with an LLM call that drafts an assessment per
      requirement, grounded in the retrieved clauses. Keep the return shape schema-aligned.
- [ ] **Retriever** (`src/retriever.py`) — start naive (keyword overlap is fine), return top-k clauses.
- [ ] **Real data** — drop one real public regulation into `data/` (see `data/README.md`) and run on it.
- [ ] **README polish** — 2–3 real screenshots of a run, your voice in the intro, your links.

## Explicitly NOT in v0.1 (kill scope creep on sight)

- ❌ No fine-tuning. Use a base model via API. Fine-tuning is not what makes this legible.
- ❌ No web UI. A CLI that prints a run id and writes JSON is enough.
- ❌ No vector database. Naive retrieval first; embeddings are v0.2.
- ❌ No Docker / deployment / CI. Later, if ever.
- ❌ No multi-regulation support. One regulation, one product description, end to end.

If you find yourself building something on the ❌ list, stop — that's the perfectionism that
turns "this week" into "never." Ship v0.1 first. It's allowed to be small.
