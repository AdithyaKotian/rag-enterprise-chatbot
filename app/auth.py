# app/auth.py

USERS = {
    "hr_user": ("hr123", "HR"),
    "finance_user": ("finance123", "Finance"),
    "marketing_user": ("marketing123", "Marketing"),
    "engineer_user": ("engineer123", "Engineer"),
    "admin_user": ("admin123", "Admin"),
}


def authenticate(username, password):
    user_data = USERS.get(username)
    if user_data and user_data[0] == password:
        return user_data[1]
    return None


def get_allowed_departments(role):
    if not role:
        return []
    access = {
        "hr": ["hr"],
        "finance": ["finance"],
        "marketing": ["marketing"],
        "engineer": ["engineering"],
        "admin": ["hr", "finance", "marketing", "engineering", "general"]
    }
    return access.get(str(role).lower(), [])