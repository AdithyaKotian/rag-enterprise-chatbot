#  Enterprise RAG Chatbot (Role-Based Access)

🚀 Live Demo: https://rag-enterprise-chatbot-3zra5m55rtmgjv8vmxumym.streamlit.app/

A production-style **Retrieval-Augmented Generation (RAG)** chatbot that answers enterprise queries using internal documents with **role-based access control**.

Built using **LangChain, ChromaDB, HuggingFace Embeddings, Groq LLM (LLaMA 3), and Streamlit**.

---

##  Features

*  Role-Based Access (HR, Finance, Marketing, Engineer, Admin)
*  RAG Pipeline (semantic search + LLM reasoning)
*  Hybrid Query Handling:

  * Structured queries (count, list)
  * Natural language queries
*  Chat history support (context-aware answers)
*  Multi-format ingestion (CSV + TXT/MD)
*  Source visibility for transparency

---

##  Architecture

```
User (Streamlit UI)
        ↓
Query + Role
        ↓
Retriever (LangChain)
        ↓
Vector DB (Chroma)
        ↓
Relevant Documents
        ↓
Role-Based Filter
        ↓
LLM (Groq - LLaMA 3)
        ↓
Final Answer + Sources
```

---

##  System Flow

1. **Data Ingestion**

   * Loads documents from `data/` folder
   * Supports `.csv`, `.txt`, `.md`

2. **Chunking**

   * Splits documents into smaller chunks

3. **Embedding**

   * Converts text into vectors (HuggingFace)

4. **Vector Store**

   * Stores embeddings in ChromaDB

5. **Retrieval**

   * Fetches top relevant chunks

6. **Role Filtering**

   * Restricts access based on user role

7. **LLM Response**

   * Generates answer using Groq LLaMA

---

##  Project Structure

```
rag-enterprise-chatbot/
│
├── app/
│   └── main.py
│
├── ingestion/
│   ├── loader.py
│   ├── splitter.py
│   └── vector_store.py
│
├── retrieval/
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── data/
│   ├── hr/
│   ├── finance/
│   ├── marketing/
│   ├── engineering/
│   └── general/
│
├── config.py
├── requirements.txt
└── .env
```

---

##  Installation

### 1. Clone repository

```
git clone https://github.com/your-username/rag-enterprise-chatbot.git
cd rag-enterprise-chatbot
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Setup environment variables

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

##  Run the App

```
streamlit run app/main.py
```

---

##  Example Queries

### Structured Queries

* how many employees
* who works in finance

### RAG Queries

* explain company architecture
* marketing strategy Q4
* financial growth 2024

---

##  Role-Based Access

| Role      | Access           |
| --------- | ---------------- |
| HR        | HR data          |
| Finance   | Finance data     |
| Marketing | Marketing data   |
| Engineer  | Engineering data |
| Admin     | All data         |

---

##  Tech Stack

* **LangChain** – RAG pipeline
* **ChromaDB** – Vector database
* **HuggingFace** – Embeddings
* **Groq (LLaMA 3)** – LLM inference
* **Streamlit** – Frontend UI
* **Python** – Backend

---

##  Future Improvements

* Add authentication (login system)
* Add evaluation (RAGAS)
* Deploy on cloud (Streamlit / AWS)
* Add feedback loop (learning system)

---

## Value

This project demonstrates:

* End-to-end RAG system design
* LLM integration (Groq API)
* Vector database usage
* Role-based access control
* Real-world enterprise use case

---

##  License

MIT License
