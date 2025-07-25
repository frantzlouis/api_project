CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    address TEXT,
    city TEXT,
    state CHAR(2) CHECK (state ~ '^[A-Za-z]{2}$'),
    zip INTEGER
);

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE NOT NULL,
    phone1 TEXT,
    phone2 TEXT,
    department TEXT,
    company_id INTEGER REFERENCES companies(id)
);
