import sqlite3

DB_NAME = "tasks.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
            )
        """)


def add_task(title: str):
    with get_connection() as conn:
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))


def list_tasks():
    with get_connection() as conn:
        return conn.execute("SELECT id, title, done, created_at FROM tasks ORDER BY id").fetchall()


def complete_task(task_id: int):
    with get_connection() as conn:
        rows = conn.execute("UPDATE tasks SET done = 1 WHERE id = ? AND done = 0", (task_id,)).rowcount
        return rows > 0


def delete_task(task_id: int):
    with get_connection() as conn:
        rows = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,)).rowcount
        return rows > 0
