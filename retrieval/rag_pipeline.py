from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_answer(query, docs, role=None, chat_history=None):
    if not docs:
        return "Not found in provided documents."

    context = "\n\n---\n\n".join([doc.page_content for doc in docs[:5]])

    history_text = ""
    if chat_history:
        for q, a in chat_history[-3:]:
            history_text += f"Q: {q}\nA: {a}\n"

    prompt = f"""
You are an enterprise assistant.

Rules:
- Answer ONLY from the context below
- If answer is not present, reply EXACTLY: "Not found in provided documents."
- Keep answer short (2–4 lines)
- Do NOT guess

User Role: {role if role else "Unknown"}

Conversation History:
{history_text}

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()