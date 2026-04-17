# app/guardrails.py
def is_safe(query):
    blocked = ["salary of", "ssn", "personal data"]
    return not any(word in query.lower() for word in blocked)