# 30-Day AI Engineer Playbook

A hands-on, day-by-day GitHub repository for becoming productive with **modern AI engineering**.

This playbook is built around practical engineering skills:

- Python for AI
- Data handling
- Classical machine learning
- Neural-network fundamentals
- LLM application development
- Prompting
- Structured outputs
- Embeddings
- Vector search
- Retrieval-Augmented Generation (RAG)
- Tool calling
- AI agents
- Evaluation
- Observability
- Security
- FastAPI
- Streamlit
- Production architecture

> Learn AI engineering by building working systems every day.

## 30-Day Learning Path

### Week 1 — AI Engineering Foundations
1. AI Engineer Role and Modern Stack
2. Python for AI Applications
3. Data with NumPy and Pandas
4. Machine Learning Workflow
5. Classification Project
6. Regression Project
7. Model Evaluation and Experimentation

### Week 2 — Deep Learning and LLM Applications
8. Neural Network Fundamentals
9. Text Processing and NLP Basics
10. LLM Application Architecture
11. Prompt Engineering
12. Structured Outputs with Pydantic
13. Model Abstraction and Local LLMs
14. Build an AI Application

### Week 3 — Embeddings, RAG, and Agents
15. Embeddings
16. Semantic Search
17. Vector Stores
18. Retrieval-Augmented Generation
19. RAG Evaluation
20. Tool Calling
21. Build Your First AI Agent

### Week 4 — Production AI Engineering
22. Agentic Workflows
23. AI Security and Guardrails
24. Evaluation Frameworks
25. Observability
26. Reliability and Failure Handling
27. FastAPI for AI Services
28. Streamlit AI Frontends
29. Production AI Architecture
30. Capstone: Enterprise AI Assistant

## Final Capstone

```text
User
  |
  v
Streamlit UI
  |
  v
FastAPI
  |
  v
AI Orchestrator
  |
  +--> RAG
  +--> Tools
  +--> Structured Output
  +--> Evaluation
  +--> Guardrails
  |
  v
Knowledge + Enterprise Data
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/prepare_data.py
pytest -q
```

Run an example:

```bash
python examples/05_agent.py
```

Run the API:

```bash
uvicorn apps.api.main:app --reload
```

Run the UI:

```bash
streamlit run apps/ui/app.py
```

Optional Ollama:

```bash
ollama serve
ollama pull llama3.2
export USE_OLLAMA=true
```

## Repository Structure

```text
30-day-ai-engineer-playbook/
├── days/
├── ai_engineer/
│   ├── ml/
│   ├── llm/
│   ├── rag/
│   ├── agents/
│   ├── evaluation/
│   ├── security/
│   └── observability/
├── apps/
│   ├── api/
│   └── ui/
├── data/
├── knowledge/
├── examples/
├── scripts/
├── tests/
└── docs/
```

## Design Principles

- Build before optimizing.
- Measure model quality.
- Keep deterministic logic deterministic.
- Use the smallest model that works.
- Ground answers when facts matter.
- Validate structured outputs.
- Design failure paths.
- Treat user and retrieved content as untrusted.
- Separate model logic from business logic.
- Think about cost, latency, and observability from the beginning.

## License
MIT
