import sqlite3
from datetime import datetime
from typing import List, Dict, Any

DB_NAME = "tasks.db"

def conect_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

def create_tables() -> None:
    conn = conect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                deadline DATE NOT NULL,
                status TEXT NOT NULL DEFAULT 'to do',
                start_date TEXT NOT NULL,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """)

        conn.commit()
    finally:
        conn.close()

def insert_task(title, description, start_date, deadline, category_id=None):
    conn = conect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks(title, description, start_date, deadline, category_id) VALUES(?, ?, ?, ?, ?)""",
             (title, description, start_date, deadline, category_id))
        conn.commit()
        task_id = cursor.lastrowid
        return task_id
    finally:
        conn.close()

def list_tasks(status=None):
    conn = conect_db()
    try:
        cursor = conn.cursor()

        if status == None:
            cursor.execute("SELECT * FROM tasks")
        else:
            cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
        
        rows = cursor.fetchall()
        tasks = [dict(row) for row in rows]
        return tasks
    finally:
        conn.close()

def src_task_id(id):
    conn = conect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()

def update_status_task(id, new_status):
    conn = conect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, id))
        conn.commit()
    finally:
        conn.close()

def delete_task(id):
    conn = conect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
        conn.commit()
    finally:
        conn.close()

def edit_task(id, title, description):
    conn = conect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?",(title, description, id))
        conn.commit()
    finally:
        conn.close()