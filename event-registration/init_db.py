import sqlite3

sql = """
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    location TEXT
);

CREATE TABLE registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    event_id INTEGER
);

INSERT INTO events (name, date, location) VALUES
('Tech Talk', '2025-01-10', 'Auditorium'),
('Hackathon', '2025-01-20', 'Lab 1'),
('AI Workshop', '2025-01-25', 'Hall');
"""

conn = sqlite3.connect("events.db")
conn.executescript(sql)
conn.close()

print("Database created!")
