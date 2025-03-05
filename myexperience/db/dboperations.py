# myexperience/db/dboperations.py

import sqlite3

def execute_query(query):
    """Executes a given SQL query on a SQLite database."""
    try:
        conn = sqlite3.connect("database.db")  # Connect to a local database file
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        return "Query executed successfully"
    except Exception as e:
        return f"Database error: {e}"

def insert(query):
    """Executes an INSERT query."""
    return execute_query(query)

def update(query):
    """Executes an UPDATE query."""
    return execute_query(query)

def delete(query):
    """Executes a DELETE query."""
    return execute_query(query)

def select(query):
    """Executes a SELECT query and fetches results."""
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return f"Database error: {e}"
