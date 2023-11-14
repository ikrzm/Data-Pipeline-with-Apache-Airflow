
\c users

-- Create table if it doesn't exist within the schema
CREATE TABLE IF NOT EXISTS utilisateurs (
    id SERIAL PRIMARY KEY,
    firt_name varchar(100),
    last_name varchar(100),
    job varchar(100),
    address varchar(300),
    phone_number varchar(100)
);