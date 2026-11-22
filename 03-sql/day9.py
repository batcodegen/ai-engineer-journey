import sqlite3

conn = sqlite3.connect("chat.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        chat TEXT,
        role TEXT,
        content TEXT
    )
"""
)

messages = (
    ('work','user', 'Day work'), 
    ('work','assistant','Got it'),
    ('study','user','What is SQL?'),
    ('study','assistant','A query language'),
    ('study','user','Is it hard?'),
    ('work','user','Night work')
)

for chat,role,content in messages:
    cur.execute(
        "INSERT into messages (chat, role, content) VALUES (?, ?, ?)",
        (chat, role, content),
    )
    conn.commit()

def add_message_db(conn, chat, role ,content):
    cur = conn.cursor()
    cur.execute(
        "INSERT into messages (chat, role, content) VALUES (?, ?, ?)",
        (chat, role, content),
    )
    conn.commit()

def count_by_role_db(conn, chat):
    cur = conn.cursor()
    cur.execute(
        "SELECT role, COUNT(*) FROM messages WHERE chat = ? GROUP BY role",
        (chat,)
    )
    return dict(cur.fetchall())

def last_messages_db(conn, chat, n):
    cur = conn.cursor()
    cur.execute(
                "SELECT role, content FROM messages WHERE chat = ? ORDER BY id DESC LIMIT ?",
                (chat, n),
            )
    return cur.fetchall()

# Task 2: the 3 queries
print(cur.execute("SELECT COUNT(*) FROM messages WHERE role = 'assistant'").fetchone())
print(cur.execute("SELECT chat, COUNT(*) FROM messages GROUP BY chat").fetchall())
print(cur.execute("SELECT content FROM messages WHERE chat = 'study' ORDER BY id DESC LIMIT 1").fetchone())

# Task 3: test the functions
add_message_db(conn, "work", "assistant", "Noted")
print(count_by_role_db(conn, "work"))
print(last_messages_db(conn, "work", 3))

conn.close()
