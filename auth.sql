CREATE DATABASE servise_d;
\c servise_d
CREATE SCHEMA servise;
CREATE TABLE servise.users (
    id serial,
    full_name VARCHAR NOT NULL,
    login VARCHAR PRIMARY KEY,
    password VARCHAR
);