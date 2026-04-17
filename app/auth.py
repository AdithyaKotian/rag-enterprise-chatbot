# app/auth.py
def get_allowed_departments(role):
    access = {
        "HR": ["hr"],
        "Finance": ["finance"],
        "Marketing": ["marketing"],
        "Engineer": ["engineering"],
        "Admin": ["hr", "finance", "marketing", "engineering", "general"]
    }
    return access.get(role, [])