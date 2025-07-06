CREATE EXTENSION IF NOT EXISTS vector;

CREATE SCHEMA vector

CREATE TABLE vector.items
(
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(255),
    embedding   vector(512)
);
