import pandas as pd
from faker import Faker
import hashlib
import random
import uuid
from datetime import datetime, timedelta

csv_dir = "./../../pseudo_data/system_data"

# --- Generate system_roles ---
roles = [
    ("Super Admin", "Full access to all companies' data and system settings."),
    ("System Auditor", "Read-only access for auditing all activities and logs."),
    ("Support Agent", "Handles customer issues across companies."),
    ("Platform Analyst", "Views aggregated analytics across companies.")
]


# Helper functions
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


def generate_uuid():
    return str(uuid.uuid4())


def text_to_hash(text: str) -> str:
    """Converts input text to a SHA-256 hash."""
    return  hashlib.sha256(text.encode()).hexdigest()


# Date range for random timestamps
start_date = datetime(2022, 1, 1)
end_date = datetime(2025, 1, 1)


system_roles = pd.DataFrame([{
    "role_id": i,
    "role_name": role[0],
    "description": f"{role[1]}",
    "permissions": "{}"
} for i, role in enumerate(roles, start=1)])


system_users = pd.DataFrame([{
    "user_id": generate_uuid(),
    "full_name": f"User_{i} Name_{i}",
    "email": f"system.user{i}@mail.com",
    "password_hash": text_to_hash("super-admin_hashed_password-123-for users"),
    "profile_id": str(random.randint(50311111, 78900000)),
    "role_id": random.choice(system_roles["role_id"].tolist()),
    "is_active": random.choice([True, True, False]),  # More active users
    "created_at": random_date(start_date, end_date),
    "updated_at": random_date(start_date, end_date),
} for i in range(1, 27)])


# --- Save to CSV ---
system_roles.to_csv(csv_dir + "system_roles.csv", index=False)
system_users.to_csv(csv_dir + "system_users.csv", index=False)

print("CSV files generated: system_roles.csv and system_users.csv")
