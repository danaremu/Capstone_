import pandas as pd
import uuid
import random
import hashlib
from datetime import datetime, timedelta

# Helper functions
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def generate_uuid():
    return str(uuid.uuid4())

def text_to_hash(text: str) -> str:
    """Converts input text to a SHA-256 hash."""
    return hashlib.sha256(text.encode()).hexdigest()

# Date range for random timestamps
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 1, 1)

# --- Generate system_roles ---
roles = [
    ("Company Owner / Admin", "Full control over their company’s users, items, settings, and reports"),
    ("Inventory Manager", "Can create/update items, manage stock entries, and view inventory reports"),
    ("Sales Manager", "Can view and manage sales transactions, approve price changes"),
    ("Sales Agent / Cashier", "Can perform sales, create invoices, and see own sales history"),
    ("Store Keeper", "Manages inventory updates and physical stock reconciliation"),
    ("Accountant", "Can view financial summaries, transaction history, and generate invoices"),
    ("Viewer / Auditor", "Read-only access for reports and history (no editing rights)"),
    ("HR Manager", "Can add/remove company users and manage access roles (optional)"),
    ("Marketing Analyst", "Access to product and sales analytics (no operational control)"),
    ("Procurement Officer", "Manages purchase orders and restocking (if module exists).")
]


# Generate data for each table
companies = pd.DataFrame([{
    "id": generate_uuid(),
    "name": f"Company_{i}",
    "industry": random.choice(["Retail", "Manufacturing", "Tech"]),
    "email": f"contact{i}@company.com",
    "phone": f"+23480123{i:04d}",
    "created_at": random_date(start_date, end_date),
    "status": random.choice(["active", "inactive"])
} for i in range(1, 4)])


user_roles = pd.DataFrame([{
    "id": i,
    "name": role[0],
    "description": f"{role[1]}",
    "permissions": "{}"
} for i, role in enumerate(roles, start=1)])


users = pd.DataFrame([{
    "id": generate_uuid(),
    "company_id": companies.sample(1).iloc[0]['id'],
    "name": f"User_{i}",
    "email": f"user{i}@mail.com",
    "password_hash": text_to_hash("hashed_password-123-for users"),
    "role_id": random.choice(user_roles["id"].tolist()),
    "status": random.choice(["active", "suspended"]),
    "created_at": random_date(start_date, end_date)
} for i in range(1, 21)])


permissions = pd.DataFrame([{
    "id": i,
    "code": f"PERM_{i}",
    "description": f"Permission {i}"
} for i in range(1, 21)])


items = pd.DataFrame([{
    "id": generate_uuid(),
    "company_id": companies.sample(1).iloc[0]['id'],
    "name": f"Item_{i}",
    "description": f"Item {i} description",
    "price": round(random.uniform(10.0, 100.0), 2),
    "sku": f"SKU{i:05d}",
    "created_by": users.sample(1).iloc[0]['id'],
    "created_at": random_date(start_date, end_date)
} for i in range(1, 21)])


inventory = pd.DataFrame([{
    "id": generate_uuid(),
    "item_id": items.sample(1).iloc[0]['id'],
    "company_id": companies.sample(1).iloc[0]['id'],
    "quantity": random.randint(10, 200),
    "updated_at": random_date(start_date, end_date),
    "updated_by": users.sample(1).iloc[0]['id']
} for _ in range(20)])


stock_entries = pd.DataFrame([{
    "id": generate_uuid(),
    "item_id": items.sample(1).iloc[0]['id'],
    "company_id": companies.sample(1).iloc[0]['id'],
    "quantity_added": random.randint(5, 50),
    "price": round(random.uniform(10.0, 100.0), 2),
    "note": "Restock",
    "created_by": users.sample(1).iloc[0]['id'],
    "created_at": random_date(start_date, end_date)
} for _ in range(20)])


sales = pd.DataFrame([{
    "id": generate_uuid(),
    "company_id": companies.sample(1).iloc[0]['id'],
    "user_id": users.sample(1).iloc[0]['id'],
    "total_amount": round(random.uniform(50.0, 500.0), 2),
    "sale_time": random_date(start_date, end_date),
    "payment_method": random.choice(["Cash", "Card", "Transfer"]),
    "customer_name": f"Customer_{i}"
} for i in range(1, 21)])


sale_items = pd.DataFrame([{
    "id": generate_uuid(),
    "sale_id": sales.sample(1).iloc[0]['id'],
    "item_id": items.sample(1).iloc[0]['id'],
    "quantity": random.randint(1, 10),
    "price_per_unit": round(random.uniform(10.0, 100.0), 2),
    "subtotal": round(random.uniform(10.0, 100.0), 2)
} for _ in range(20)])


audit_logs = pd.DataFrame([{
    "id": generate_uuid(),
    "user_id": users.sample(1).iloc[0]['id'],
    "company_id": companies.sample(1).iloc[0]['id'],
    "action_type": random.choice(["create", "update", "delete", "read"]),
    "resource_type": "Item",
    "resource_id": generate_uuid(),
    "details": "{}",
    "timestamp": random_date(start_date, end_date)
} for _ in range(1)])


transaction_logs = pd.DataFrame([{
    "id": generate_uuid(),
    "type": random.choice(["stock_in", "sale", "adjustment"]),
    "reference_id": generate_uuid(),
    "user_id": users.sample(1).iloc[0]['id'],
    "company_id": companies.sample(1).iloc[0]['id'],
    "affected_items": "{}",
    "timestamp": random_date(start_date, end_date)
} for _ in range(20)])


analytics_cache = pd.DataFrame([{
    "id": generate_uuid(),
    "company_id": companies.sample(1).iloc[0]['id'],
    "report_type": "monthly_summary",
    "period": "2024-12",
    "metrics": "{}",
    "generated_at": random_date(start_date, end_date)
} for _ in range(20)])


admins = pd.DataFrame([{
    "id": generate_uuid(),
    "name": f"Admin_{i}",
    "email": f"admin{i}@system.com",
    "password_hash": text_to_hash("admin_hashed_password-123-for admins"),
    "access_level": random.choice(["view_all", "system_settings"])
} for i in range(1, 21)])


# Save all data to CSVs
csv_dir = "./../../pseudo_data/"
companies.to_csv(csv_dir + "companies.csv", index=False)
user_roles.to_csv(csv_dir + "user_roles.csv", index=False)
users.to_csv(csv_dir + "users.csv", index=False)
permissions.to_csv(csv_dir + "permissions.csv", index=False)
items.to_csv(csv_dir + "items.csv", index=False)
inventory.to_csv(csv_dir + "inventory.csv", index=False)
stock_entries.to_csv(csv_dir + "stock_entries.csv", index=False)
sales.to_csv(csv_dir + "sales.csv", index=False)
sale_items.to_csv(csv_dir + "sale_items.csv", index=False)
audit_logs.to_csv(csv_dir + "audit_logs.csv", index=False)
transaction_logs.to_csv(csv_dir + "transaction_logs.csv", index=False)
analytics_cache.to_csv(csv_dir + "analytics_cache.csv", index=False)
admins.to_csv(csv_dir + "admins.csv", index=False)


csv_dir  # Display directory for downloads
