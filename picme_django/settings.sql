-- settings.sql
CREATE DATABASE picme;
CREATE USER picmeuser WITH PASSWORD 'picme';
GRANT ALL PRIVILEGES ON DATABASE picme TO picmeuser;