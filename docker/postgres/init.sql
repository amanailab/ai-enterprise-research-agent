CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS research_reports (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    report_content TEXT NOT NULL,
    user_id INTEGER NOT NULL,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_report_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
);


CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    title VARCHAR(500),

    report_id INTEGER NOT NULL,

    CONSTRAINT fk_source_report
        FOREIGN KEY (report_id)
        REFERENCES research_reports(id)
);


CREATE TABLE IF NOT EXISTS agent_runs (
    id SERIAL PRIMARY KEY,

    company_name VARCHAR(255) NOT NULL,

    status VARCHAR(50) NOT NULL,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);