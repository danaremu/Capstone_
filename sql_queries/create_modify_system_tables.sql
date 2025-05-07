CREATE TABLE system_roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    permissions JSON
);


CREATE TABLE system_users (
    user_id SERIAL PRIMARY KEY,
	full_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    profile_id VARCHAR(8) UNIQUE NOT NULL,
    role_id INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_system_role
        FOREIGN KEY (role_id)
        REFERENCES system_roles(role_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);