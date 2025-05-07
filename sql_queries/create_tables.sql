CREATE TABLE companies (
    id UUID PRIMARY KEY,
    name VARCHAR NOT NULL,
    industry VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR CHECK (status IN ('active', 'inactive'))
);

CREATE TABLE user_roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    description TEXT,
    permissions JSON
);

CREATE TABLE users (
    id UUID PRIMARY KEY,
    company_id UUID NOT NULL,
    name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role_id INT,
    status VARCHAR CHECK (status IN ('active', 'suspended')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    code VARCHAR UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE items (
    id UUID PRIMARY KEY,
    company_id UUID NOT NULL,
    name VARCHAR NOT NULL,
    description TEXT,
    price DECIMAL,
    sku VARCHAR,
    created_by UUID,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE inventory (
    id UUID PRIMARY KEY,
    item_id UUID NOT NULL,
    company_id UUID NOT NULL,
    quantity INT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by UUID
);

CREATE TABLE stock_entries (
    id UUID PRIMARY KEY,
    item_id UUID NOT NULL,
    company_id UUID NOT NULL,
    quantity_added INT,
    price DECIMAL,
    note TEXT,
    created_by UUID,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sales (
    id UUID PRIMARY KEY,
    company_id UUID NOT NULL,
    user_id UUID NOT NULL,
    total_amount DECIMAL,
    sale_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR,
    customer_name VARCHAR
);

CREATE TABLE sale_items (
    id UUID PRIMARY KEY,
    sale_id UUID NOT NULL,
    item_id UUID NOT NULL,
    quantity INT,
    price_per_unit DECIMAL,
    subtotal DECIMAL
);

CREATE TABLE audit_logs (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    company_id UUID NOT NULL,
    action_type VARCHAR CHECK (action_type IN ('create', 'update', 'delete', 'read')),
    resource_type VARCHAR,
    resource_id UUID,
    details JSON,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transaction_logs (
    id UUID PRIMARY KEY,
    type VARCHAR CHECK (type IN ('stock_in', 'sale', 'adjustment')),
    reference_id UUID,
    user_id UUID,
    company_id UUID,
    affected_items JSON,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE analytics_cache (
    id UUID PRIMARY KEY,
    company_id UUID,
    report_type VARCHAR,
    period VARCHAR,
    metrics JSON,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE admins (
    id UUID PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    password_hash TEXT,
    access_level VARCHAR CHECK (access_level IN ('view_all', 'system_settings'))
);
