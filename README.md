# 🤖 GenAI Interview Preparation

A structured 15-day hands-on learning journey to become a **GenAI / LLM Engineer** — from Python fundamentals to building and deploying real AI products.

> **Goal:** Land my first job as a GenAI Engineer by building deep understanding, not just copying code.

---

## 📊 Progress Tracker

| Phase | Days | Topics | Status |
|---|---|---|---|
| 🔵 Phase 1: Foundations | Day 1–5 | Python OOP, Math, Embeddings, Transformers | 🔄 In Progress |
| 🟡 Phase 2: LLM + RAG | Day 6–10 | LLMs, RAG from scratch, Vector DBs, LlamaIndex | ⏳ Upcoming |
| 🟢 Phase 3: Build + Ship | Day 11–15 | FastAPI, Resume Screener, Docker, Deployment | ⏳ Upcoming |

---

## 🗓️ 15-Day Learning Plan

### 🔵 Phase 1: Foundations (Day 1–5)

#### Day 1 — Python Deep Dive
- OOP: classes, inheritance, dunder methods
- Decorators & context managers
- Async/await basics
- **Task:** Write `BankAccount`, `Stack`, `ResumeParser` classes from scratch

#### Day 2 — Math for ML
- Vectors & matrices with NumPy
- Implement cosine similarity manually
- Gradient intuition (no math — just code)
- **Task:** Build `find_most_similar`, `normalize_vector`, `batch_similarity`

#### Day 3 — Neural Networks Intuition
- How a neuron works (weights, bias, activation)
- Forward pass coded from scratch in NumPy
- Backpropagation intuition
- **Resource:** Karpathy — "The spelled-out intro to neural networks"

#### Day 4 — Embeddings & Vector Math
- What IS an embedding? (words as coordinates)
- Load HuggingFace model, embed 10 sentences
- Find most similar sentence — no libraries
- **Task:** Build mini semantic search engine

#### Day 5 — Transformers Conceptually
- Attention mechanism — what problem it solves
- Tokens, context window, why it matters
- **Resource:** "The Illustrated Transformer" by Jay Alammar

---

### 🟡 Phase 2: LLM + RAG (Day 6–10)

#### Day 6 — LLM Fundamentals
- Temperature, top_p, top_k — experiment with all 3
- System prompt vs user prompt
- Why hallucination happens and how to reduce it
- Prompt engineering: chain of thought, few-shot

#### Day 7 — RAG From Scratch
- Build RAG with zero frameworks — raw Python
- Chunk a document manually, embed each chunk
- Store in a Python dict (not ChromaDB yet)
- Query: embed → find closest chunk → send to LLM

#### Day 8 — Vector Databases Deep Dive
- Why we need vector DBs (not regular SQL)
- ChromaDB: insert, query, delete, update
- HNSW index (conceptually)
- Compare cosine vs dot product vs euclidean

#### Day 9 — LlamaIndex Internals
- Read LlamaIndex source: how does it chunk?
- Chunking strategies: fixed, semantic, recursive
- Re-read Repo Copilot code — explain every line
- **Task:** Build RAG pipeline — no copy-paste

#### Day 10 — Advanced RAG Techniques
- Hybrid search: dense + sparse (BM25)
- Re-ranking: what it is and why it helps
- Evaluate RAG: precision, recall, faithfulness
- LangChain vs LlamaIndex — know the difference

---

### 🟢 Phase 3: Build + Ship (Day 11–15)

#### Day 11 — FastAPI + System Design
- Build REST API with FastAPI from scratch
- Pydantic models for request/response validation
- Async endpoints for LLM calls
- Design resume screener architecture on paper

#### Day 12 — Resume Screener Core
- PDF parsing with PyMuPDF
- Resume parser agent with Groq LLM
- Match scoring agent
- **Rule:** Write every line yourself

#### Day 13 — Skill Gap + Rewriter Agents
- Skill gap analysis agent
- Resume bullet rewriter agent
- Connect all agents in main.py
- Test with 3 different resumes + job descriptions

#### Day 14 — Docker + Deployment
- Dockerize the FastAPI app
- Write docker-compose.yml
- Deploy on Railway / Render
- Get a live URL to share with recruiters

#### Day 15 — Interview Prep + README
- Write killer README with architecture diagram
- Prepare answers: why RAG not fine-tuning?
- Record a 2-min demo video
- Push to GitHub with clean commit history

---

## 🛠️ Projects Built

### 1. Repo Copilot
> Ask anything about any GitHub codebase using RAG

**Tech Stack:** LlamaIndex · ChromaDB · Groq LLM · HuggingFace Embeddings · Streamlit · GitPython

**Key Features:**
- Clone any public GitHub repo
- Index entire codebase using RAG pipeline
- Ask natural language questions about the code
- Semantic search across all files

🔗 [View Project](https://github.com/ayushRajak19/repos-copilot-cb)

---

### 2. AI Resume Screener *(In Progress)*
> Upload resume + paste job description → get match score, skill gap analysis, and AI-rewritten bullets

**Tech Stack:** Groq LLM · LlamaIndex · ChromaDB · FastAPI · React · PyMuPDF · PostgreSQL · Docker

**Key Features:**
- PDF resume parsing with LLM
- Semantic job match scoring (0–100%)
- Skill gap analysis with learning roadmap
- AI resume bullet rewriter
- REST API + React frontend

🔗 [View Project](#) *(coming soon)*

---

## 💡 Core Concepts I'm Mastering

```
Embeddings          → Converting text to vectors
Cosine Similarity   → Finding similar documents
RAG Pipeline        → Retrieval Augmented Generation
Chunking Strategies → Fixed, Semantic, Recursive
Vector Databases    → ChromaDB, pgvector, Pinecone
LLM Fundamentals    → Temperature, tokens, hallucination
Prompt Engineering  → Chain of thought, few-shot
Fine-tuning vs RAG  → When to use which
FastAPI             → Production ML APIs
Docker              → Containerizing AI apps
```

---

## 🎯 Interview Questions I Can Answer

- What is an embedding and why do we use them?
- Why cosine similarity over euclidean distance for text?
- What is RAG and when would you use it over fine-tuning?
- How do you handle hallucination in LLMs?
- What chunking strategy would you use for code files?
- Explain the difference between dense and sparse retrieval.
- How do you evaluate a RAG pipeline?

---

## 📚 Resources

| Resource | Link |
|---|---|
| Fast.ai Practical Deep Learning | https://course.fast.ai |
| Karpathy Neural Networks Zero to Hero | https://youtube.com/@AndrejKarpathy |
| DeepLearning.AI Short Courses | https://deeplearning.ai |
| The Illustrated Transformer | https://jalammar.github.io/illustrated-transformer |
| LlamaIndex Docs | https://docs.llamaindex.ai |

---

## 🚀 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-RAG-purple?style=flat)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-green?style=flat)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=flat)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal?style=flat&logo=fastapi)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow?style=flat)
![Docker](https://img.shields.io/badge/Docker-Deploy-blue?style=flat&logo=docker)

---

## 👨‍💻 About Me

**Ayush Rajak** — Aspiring GenAI Engineer

Building real AI products to land my first job in the GenAI space.
Every line of code in this repo is written by me — no copy-paste.

[![GitHub](https://img.shields.io/badge/GitHub-ayushRajak19-black?style=flat&logo=github)](https://github.com/ayushRajak19)

---

⭐ *If this repo helped you, give it a star!*
