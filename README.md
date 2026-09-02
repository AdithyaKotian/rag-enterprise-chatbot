# 🏢 Enterprise RAG Chatbot (Role-Based Access)

🚀 **Live Demo:** [Click here to view the live app](https://rag-enterprise-chatbot-3zra5m55rtmgjv8vmxumym.streamlit.app/)

A production-grade **Retrieval-Augmented Generation (RAG)** chatbot that securely answers enterprise queries using internal organizational documents, strictly enforced by **Role-Based Access Control (RBAC)**.

Built using **LangChain, ChromaDB, HuggingFace Embeddings, Groq Inference (openai/gpt-oss-20b), and Streamlit**.

---

## ✨ Features

* **Role-Based Access Control (RBAC):** Authentication system that restricts users (HR, Finance, Marketing, Engineering, Admin) strictly to authorized vector embeddings.
* **RAG Pipeline:** Semantic vector search combined with LLM reasoning for accurate, context-aware answers.
* **Hybrid Query Handling:**
  * Structured queries (employee counts, departmental listings)
  * Natural language conversational queries
* **Hallucination Guardrails:** Strict prompt engineering ensures the bot refuses to answer if context is absent from company documents.
* **Multi-Format Ingestion:** Automated data loading and recursive chunking for `.csv` and `.md` files.
* **Source Visibility:** Built-in transparency allows users to inspect the exact text chunks retrieved from the vector store.

---

## 🏗️ Architecture

```text
User (Streamlit UI)
        ↓
Login Authentication & Role Assignment
        ↓
Query + Role Context
        ↓
Retriever (LangChain)
        ↓
Vector DB (ChromaDB)
        ↓
Role-Based Metadata Filter
        ↓
LLM Inference (Groq: openai/gpt-oss-20b)
        ↓
Final Answer + Verifiable Sources
```

---

## 📂 Project Structure

```plaintext
rag-enterprise-chatbot/
│
├── .streamlit/
│   └── secrets.toml          # API Keys (Ignored by Git)
│
├── app/
│   ├── main.py               # Streamlit UI & Core Workflow
│   ├── auth.py               # RBAC & Authentication Logic
│   └── guardrails.py         # AI Safety & Prompt Constraints
│
├── ingestion/
│   ├── loader.py             # Multi-format document loading
│   ├── splitter.py           # Recursive text chunking
│   └── vector_store.py       # ChromaDB vector store initialization
│
├── retrieval/
│   ├── retriever.py          # Similarity search & metadata filtering
│   └── rag_pipeline.py       # LLM client & prompt orchestration
│
├── data/                     # Enterprise Knowledge Base
│   ├── hr/
│   ├── finance/
│   ├── marketing/
│   ├── engineering/
│   └── general/
│
├── config.py                 # System configurations & paths
├── requirements.txt          # Python dependencies
├── .gitignore                # Security exclusions
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone repository
```bash
git clone https://github.com/AdithyaKotian/rag-enterprise-chatbot.git
cd rag-enterprise-chatbot
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# .\venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Streamlit Secrets
Create the local `.streamlit` configuration directory:
```bash
mkdir -p .streamlit
touch .streamlit/secrets.toml
```

Add your Groq API key inside `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## 💻 Run the Application

Start the local Streamlit development server:
```bash
streamlit run app/main.py
```

Access the dashboard at `http://localhost:8501`.

---

## 🔐 Role-Based Access Testing

Test access permissions using the default test accounts:

| Role | Username | Password | Data Access Clearance |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin_user` | `admin123` | Full Access |
| **Engineer** | `engineer_user` | `engineer123` | Engineering Data Only |
| **Finance** | `finance_user` | `finance123` | Finance Data Only |
| **Marketing** | `marketing_user` | `marketing123` | Marketing Data Only |
| **HR** | `hr_user` | `hr123` | HR Data Only |

---

## 🛠️ Tech Stack

* **LangChain** – RAG pipeline orchestration
* **ChromaDB** – Local vector database for semantic search
* **HuggingFace** – Sentence transformers and open-source embeddings
* **Groq** – Low-latency LLM inference engine
* **Streamlit** – Interactive frontend application
* **Python** – Core backend logic

---

## 📈 Future Improvements

* Integrate production identity providers (OAuth 2.0 / SAML / SSO).
* Implement automated RAG evaluation metrics using the RAGAS framework.
* Add persistent PostgreSQL / Redis storage for multi-user session and chat history management.
* Implement dynamic vector re-indexing for real-time document updates.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.
