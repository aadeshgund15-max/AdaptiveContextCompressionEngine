"""
Adaptive Context Intelligence Engine (ACIE)
SQLite Database Module
"""

import sqlite3


class Database:

    def __init__(self, db_name="acie.db"):

        self.connection = sqlite3.connect(db_name)

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            query TEXT,

            importance INTEGER,

            confidence REAL,

            decision TEXT
        )
        """)

        self.connection.commit()

    def insert_memory(self, query, importance, confidence, decision):

        self.cursor.execute("""

        INSERT INTO memory
        (query,importance,confidence,decision)

        VALUES (?,?,?,?)

        """, (query, importance, confidence, decision))

        self.connection.commit()

        return self.cursor.lastrowid

    def fetch_all(self):

        self.cursor.execute("SELECT * FROM memory")

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()


if __name__ == "__main__":

    db = Database()

    print(db.fetch_all())