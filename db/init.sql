CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    content TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
