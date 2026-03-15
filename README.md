# Overview

This project demonstrates how to connect Python to a PostgreSQL database using psycopg2.
The script creates a table, inserts data into the table, and retrieves the stored records.

# Requirements

Python 3

PostgreSQL installed

psycopg2 library

Install psycopg2:

pip install psycopg2-binary
How the Script Works

getConnection() connects Python to the PostgreSQL database.

table() creates a table if it does not already exist.

The script inserts a sample record into the table.

It then retrieves the stored data and prints it.

# Running the Script
Example Output
('das',)