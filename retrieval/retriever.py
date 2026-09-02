def get_allowed_departments(role):
    if not role:
        return []
    role_map = {
        "hr": ["hr"],
        "finance": ["finance"],
        "marketing": ["marketing"],
        "engineer": ["engineering"],
        "admin": ["hr", "finance", "marketing", "engineering", "general"]
    }
    return role_map.get(str(role).lower(), [])


def retrieve_docs(query, db, role):
    if db is None:
        return []

    # 🔥 better retrieval
    retriever = db.as_retriever(search_kwargs={"k": 8})

    docs = retriever.invoke(query)

    # 🔥 sort by richness (helps LLM)
    docs = sorted(docs, key=lambda x: len(x.page_content), reverse=True)

    # 🔥 role-based filtering
    allowed = [r.lower() for r in get_allowed_departments(role)]

    filtered_docs = [
        doc for doc in docs
        if doc.metadata.get("department", "").lower() in allowed
    ]

    if not filtered_docs:
        return []

    return filtered_docs