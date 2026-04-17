import streamlit as st
import sys
import os

# ----------------------------
# FIX IMPORT PATH
# ----------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ingestion.loader import load_all_docs
from ingestion.splitter import split_docs
from ingestion.vector_store import create_vectorstore
from retrieval.retriever import retrieve_docs
from retrieval.rag_pipeline import generate_answer

st.set_page_config(page_title="Enterprise RAG Chatbot", layout="centered")
st.title("Enterprise RAG Chatbot")

# ----------------------------
# INIT STATES
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "feedback" not in st.session_state:
    st.session_state.feedback = []

# ----------------------------
# INPUTS
# ----------------------------
role = st.selectbox("Select Role", ["HR", "Finance", "Marketing", "Engineer", "Admin"])
query = st.text_input("Ask your question")

# ----------------------------
# BUILD DB ONLY ONCE
# ----------------------------
@st.cache_resource
def build_db():
    raw_docs = load_all_docs("data")
    chunks = split_docs(raw_docs)
    db = create_vectorstore(chunks)
    return raw_docs, chunks, db


raw_docs, chunks, db = build_db()

st.write("Loaded docs:", len(raw_docs))
st.write("Chunks created:", len(chunks))
st.write("DB ready:", db is not None)

# ----------------------------
# QUERY FLOW
# ----------------------------
if query:
    q_lower = query.lower()

    # 🔴 COUNT QUERY
    if "how many" in q_lower or "count" in q_lower:
        answer = f"Total employees: {len(raw_docs)}"
        st.success(answer)

    # 🔴 LIST PEOPLE
    elif "who works" in q_lower or "employees in" in q_lower:
        docs = retrieve_docs(query, db, role)

        if not docs:
            answer = "No data found"
            st.warning(answer)
        else:
            names = []
            for doc in docs:
                parts = doc.page_content.split(",")
                if len(parts) > 1:
                    names.append(parts[1])

            answer = ", ".join(names[:5])
            st.success(answer)

    # 🟢 RAG FLOW
    else:
        docs = retrieve_docs(query, db, role)
        st.write("Retrieved docs:", len(docs))

        if not docs:
            answer = "No access or no relevant data found"
            st.warning(answer)
        else:
            answer = generate_answer(
                query,
                docs,
                role,
                st.session_state.chat_history
            )
            st.success(answer)

            # 🔍 SOURCE DISPLAY
            with st.expander("View Sources"):
                for i, doc in enumerate(docs[:3]):
                    st.write(f"Source {i+1}:")
                    st.write(doc.page_content[:300])
                    st.write("---")

            # ----------------------------
            # 👍 FEEDBACK BUTTONS
            # ----------------------------
            col1, col2 = st.columns(2)

            with col1:
                if st.button("👍 Good", key=f"up_{query}"):
                    st.session_state.feedback.append((query, answer, "up"))

            with col2:
                if st.button("👎 Bad", key=f"down_{query}"):
                    st.session_state.feedback.append((query, answer, "down"))

    # ----------------------------
    # SAVE CHAT HISTORY
    # ----------------------------
    st.session_state.chat_history.append((query, answer))

# ----------------------------
# SHOW CHAT HISTORY
# ----------------------------
st.subheader("Chat History")

for q, a in reversed(st.session_state.chat_history[-5:]):
    st.write(f"🧑 {q}")
    st.write(f"🤖 {a}")
    st.write("---")

# ----------------------------
# FEEDBACK SUMMARY
# ----------------------------
st.subheader("Feedback Summary")

total = len(st.session_state.feedback)

if total > 0:
    up = sum(1 for _, _, r in st.session_state.feedback if r == "up")
    down = total - up

    st.write(f"Total feedback: {total}")
    st.write(f"👍 Positive: {up}")
    st.write(f"👎 Negative: {down}")
    st.write(f"Accuracy: {round((up / total) * 100, 2)}%")
else:
    st.write("No feedback yet")