# 🎓 AI University Customer Support Agent (Hybrid RAG + FastAPI + n8n)

An AI-powered University Customer Support Agent built with **Hybrid Retrieval-Augmented Generation (Hybrid RAG)**. The system retrieves relevant information from official university documents and generates accurate, context-aware answers using OpenAI's language model.

This project integrates **FastAPI**, **ChromaDB**, **Hybrid Retrieval**, and **n8n Automation** to provide a scalable REST API for university-related question answering.

---

## ✨ Features

- 📄 PDF-based Knowledge Base
- 🔍 Hybrid Search (Semantic + Keyword Retrieval)
- 🧠 OpenAI GPT Integration
- 🤗 HuggingFace Embeddings
- 🗂️ ChromaDB Vector Store
- ⚡ FastAPI REST API
- 🔄 n8n Workflow Automation
- 📚 Context-Aware Responses
- 🚫 Reduced Hallucinations
- 📡 Easy API Integration

---

# 🏗️ Tech Stack

- Python
- FastAPI
- LangChain
- OpenAI GPT
- HuggingFace Embeddings
- ChromaDB
- Hybrid Retrieval
- Document Re-ranking
- n8n
- Postman

---

# 📁 Project Structure

```text
AI-University-Customer-Support-Agent/
│
├── data/
│   └── NexGen_University_Info.pdf
│
├── n8n/
│   └── automation.json
│
├── notebook/
│
├── src/
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   └── load_pdf.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   └── query.py
│   │
│   └── vectorstore/
│       └── __init__.py
│
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ System Workflow

```text
University PDF
        │
        ▼
Document Loading
        │
        ▼
Text Chunking
        │
        ▼
Embedding Generation
(HuggingFace)
        │
        ▼
ChromaDB Vector Store
        │
        ▼
Hybrid Retriever
(Dense + Sparse)
        │
        ▼
Document Re-ranking
        │
        ▼
OpenAI GPT
        │
        ▼
FastAPI Endpoint
        │
        ▼
n8n Automation
        │
        ▼
User Response
```

---

# 🚀 API Endpoint

### POST `/ask`

### Request

```json
{
  "question": "What is the fee structure?"
}
```

### Response

```json
{
  "success": true,
  "answer": "The fee structure for BS Computer Science is..."
}
```

---

# 🔄 n8n Workflow

The project includes an n8n automation workflow that:

1. Receives user questions through a Webhook.
2. Extracts the question from the request.
3. Sends it to the FastAPI endpoint.
4. Receives the AI-generated response.
5. Returns a structured JSON response to the client.

---

# 📸 Demo

## 🎥 Demo Video

[![Watch Demo](assets/rag_pipeline_flowchart_en.png)](assets/demo.mp4)

---

# 💡 Future Improvements

- Multi-document Support
- Conversation Memory
- Authentication & Authorization
- Docker Deployment
- Streaming Responses
- Source Citations
- Admin Dashboard
- Feedback Collection

---

# 👨‍💻 Author

**Muhammad Rafay**

AI Engineer | RAG Applications | FastAPI | LangChain | n8n | Generative AI

If you like this project, consider giving it a ⭐ on GitHub.
