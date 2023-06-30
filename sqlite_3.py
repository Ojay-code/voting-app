import sqlite3
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('voter_data.db')
c = conn.cursor()

# Create a table to store voter details if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS voters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                address TEXT
            )''')
conn.commit()

# Function to insert voter details into the database
def insert_voter(name, age, address):
    c.execute("INSERT INTO voters (name, age, address) VALUES (?, ?, ?)",
              (name, age, address))
    conn.commit()
    print("Voter details inserted successfully!")

# Collect user details
name = input("Enter voter's name: ")
age = int(input("Enter voter's age: "))
address = input("Enter voter's address: ")

# Insert voter details into the database
insert_voter(name, age, address)

# Close the database connection
conn.close()
