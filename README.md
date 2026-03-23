# 🤖 GenAI Interview Preparation

A structured hands-on learning journey to become a **GenAI / LLM Engineer** — from Python fundamentals to building and deploying real AI products.

> **Goal:** Land my first job as a GenAI Engineer by building deep understanding, not just copying code.

---

## 📊 Progress Tracker

| Phase | Topics | Status |
|---|---|---|
| 🔵 Phase 1: Foundations | Python OOP, Math, Embeddings, Transformers | 🔄 In Progress |
| 🟡 Phase 2: LLM + RAG | LLMs, RAG from scratch, Vector DBs, LlamaIndex | ⏳ Upcoming |
| 🟢 Phase 3: Build + Ship | FastAPI, Resume Screener, Docker, Deployment | ⏳ Upcoming |

---

## 🗓️ Learning Plan

### 🔵 Phase 1: Foundations

**Python Deep Dive**
- OOP: classes, inheritance, dunder methods
- Decorators & context managers
- Async/await basics
- Write `BankAccount`, `Stack`, `ResumeParser` classes from scratch

**Math for ML**
- Vectors & matrices with NumPy
- Implement cosine similarity manually
- Gradient intuition through code
- Build `find_most_similar`, `normalize_vector`, `batch_similarity`

**Neural Networks Intuition**
- How a neuron works (weights, bias, activation)
- Forward pass coded from scratch in NumPy
- Backpropagation intuition
- Resource: Karpathy — "The spelled-out intro to neural networks"

**Embeddings & Vector Math**
- What IS an embedding? (words as coordinates)
- Load HuggingFace model, embed sentences
- Find most similar sentence — no libraries
- Build mini semantic search engine from scratch

**Transformers Conceptually**
- Attention mechanism — what problem it solves
- Tokens, context window, why it matters
- Resource: "The Illustrated Transformer" by Jay Alammar

---

### 🟡 Phase 2: LLM + RAG

**LLM Fundamentals**
- Temperature, top_p, top_k — experiment with all 3
- System prompt vs user prompt
- Why hallucination happens and how to reduce it
- Prompt engineering: chain of thought, few-shot

**RAG From Scratch**
- Build RAG with zero frameworks — raw Python
- Chunk a document manually, embed each chunk
- Store in a Python dict (not ChromaDB yet)
- Query: embed → find closest chunk → send to LLM

**Vector Databases Deep Dive**
- Why we need vector DBs (not regular SQL)
- ChromaDB: insert, query, delete, update
- HNSW index (conceptually)
- Compare cosine vs dot product vs euclidean

**LlamaIndex Internals**
- Read LlamaIndex source: how does it chunk?
- Chunking strategies: fixed, semantic, recursive
- Build full RAG pipeline — no copy-paste

**Advanced RAG Techniques**
- Hybrid search: dense + sparse (BM25)
- Re-ranking: what it is and why it helps
- Evaluate RAG: precision, recall, faithfulness
- LangChain vs LlamaIndex — know the difference

---

### 🟢 Phase 3: Build + Ship

**FastAPI + System Design**
- Build REST API with FastAPI from scratch
- Pydantic models for request/response validation
- Async endpoints for LLM calls
- Design resume screener architecture on paper

**Resume Screener Core**
- PDF parsing with PyMuPDF
- Resume parser agent with Groq LLM
- Match scoring agent
- Every line written from scratch

**Skill Gap + Rewriter Agents**
- Skill gap analysis agent
- Resume bullet rewriter agent
- Connect all agents in main.py
- Test with 3 different resumes + job descriptions

**Docker + Deployment**
- Dockerize the FastAPI app
- Write docker-compose.yml
- Deploy on Railway / Render
- Live URL to share with recruiters

**Interview Prep**
- Architecture diagrams
- Prepare answers for common GenAI questions
- Record a 2-min demo video
- Clean commit history on GitHub

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
