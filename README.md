# 🔍 Multi-Agent Research AI

## 🚀 Overview

An AI-powered research assistant that answers user queries by combining:

- **Retrieval-Augmented Generation (RAG)**
- **Vector database search** (pgvector)
- **Real-time web search** (Tavily API)
- **Multi-agent orchestration** using LangGraph

The system retrieves relevant information from both a local knowledge base and the web, then generates a structured response.

---

## 🧠 How It Works

### 🔄 Flow
```text
User Query
   ↓
Retrieval Agent (vector search)
   ↓
Router Agent
   ├──→ Synthesis Agent (if context is sufficient)
   └──→ Web Agent → Synthesis Agent
   ↓
Final Answer
```

### 🧩 Agents

#### Retrieval Agent
- Converts the query into embeddings
- Searches the vector database (pgvector)
- Returns relevant stored content

#### Router Agent
- Checks if retrieved context exists
- Routes execution to the next agent

#### Web Agent
- Calls Tavily API
- Retrieves relevant web content

#### Synthesis Agent
- Combines vector and web context
- Generates:
  - Explanation
  - Key insights
  - Final summary

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, LangGraph |
| Database | PostgreSQL + pgvector |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Web Search | Tavily API |
| Frontend | Streamlit |
| Infrastructure | Docker, Docker Compose |

---

## ⚙️ Setup
```bash
git clone <repo-url>
cd <project-folder>
docker-compose up -d --build
```

---

## 🔎 API

### `POST /research`

**Request:**
```json
{
  "query": "What is RAG?"
}
```

**Response:**
```json
{
  "final_answer": "..."
}
```

---

## 📂 Project Structure
```text
app/
 ├── main.py
 ├── graph.py
 ├── state.py
 ├── db.py
 ├── vector_store.py
 ├── tools/
 │    ├── embedder.py
 │    └── web_search.py
 └── agents/
      ├── retrieval_agent.py
      ├── web_agent.py
      ├── synthesis_agent.py
      └── router_agent.py

frontend/
 └── streamlit_app.py
```

---

## 🧠 Summary

The system processes a query by retrieving relevant context from a vector database, optionally augmenting it with live web results, and generating a structured answer through a multi-agent workflow.