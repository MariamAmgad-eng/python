# main.py

from myexperience import fileoperation
from myexperience.db import dboperations

# File Operations
print(fileoperation.write("example.txt", "Hello, World!", "write"))
print(fileoperation.append("example.txt", "\nNew Line!", "write"))
print(fileoperation.read("example.txt", "all"))

# Database Operations
print(dboperations.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"))  # Ensure table exists
print(dboperations.insert("INSERT INTO users (name, age) VALUES ('Alice', 25)"))
print(dboperations.select("SELECT * FROM users"))
