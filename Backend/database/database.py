"""
Adaptive Context Intelligence Engine (ACIE)
SQLite Database Module
"""

import sqlite3


class Database:

    def __init__(self, db_name="acie.db"):

        self.connection = sqlite3.connect(
            db_name,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            query TEXT,

            importance INTEGER,

            confidence REAL,

            decision TEXT,

            created_at TEXT,

            last_accessed TEXT,

            access_count INTEGER,

            state TEXT
        )
        """)

        self.connection.commit()

    def insert_memory(
        self,
        query,
        importance,
        confidence,
        decision,
        created_at,
        last_accessed,
        access_count,
        state
    ):

        self.cursor.execute(
            """
            INSERT INTO memory
            (
                query,
                importance,
                confidence,
                decision,
                created_at,
                last_accessed,
                access_count,
                state
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                query,
                importance,
                confidence,
                decision,
                created_at,
                last_accessed,
                access_count,
                state
            )
        )

        self.connection.commit()

        return self.cursor.lastrowid

    def fetch_all(self):

        self.cursor.execute(
            """
            SELECT
                id,
                query,
                importance,
                confidence,
                decision,
                created_at,
                last_accessed,
                access_count,
                state
            FROM memory
            """
        )

        return self.cursor.fetchall()

    def fetch_by_id(self, memory_id):

        self.cursor.execute(
            """
            SELECT *
            FROM memory
            WHERE id = ?
            """,
            (memory_id,)
        )

        return self.cursor.fetchone()

    def update_access(self, memory_id, last_accessed, access_count):

        self.cursor.execute(
            """
            UPDATE memory
            SET
                last_accessed = ?,
                access_count = ?
            WHERE id = ?
            """,
            (
                last_accessed,
                access_count,
                memory_id
            )
        )

        self.connection.commit()

    def update_state(self, memory_id, state):

        self.cursor.execute(
            """
            UPDATE memory
            SET state = ?
            WHERE id = ?
            """,
            (
                state,
                memory_id
            )
        )

        self.connection.commit()

    def delete_memory(self, memory_id):

        self.cursor.execute(
            """
            DELETE FROM memory
            WHERE id = ?
            """,
            (memory_id,)
        )

        self.connection.commit()

    def close(self):

        self.connection.close()


if __name__ == "__main__":

    db = Database()

    print("Database initialized successfully.")

    memories = db.fetch_all()

    print(memories)