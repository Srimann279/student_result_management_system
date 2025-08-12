import sqlite3

def create_tables():
    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        course TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        roll_no TEXT,
        subject TEXT,
        marks REAL,
        FOREIGN KEY (roll_no) REFERENCES students(roll_no)
    )
    """)

    conn.commit()
    conn.close()

def add_student(roll_no, name, course):
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (roll_no, name, course))
    conn.commit()
    conn.close()

def add_result(roll_no, subject, marks):
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    c.execute("INSERT INTO results VALUES (?, ?, ?)", (roll_no, subject, marks))
    conn.commit()
    conn.close()

def get_results(roll_no):
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    c.execute("""
    SELECT s.roll_no, s.name, s.course, r.subject, r.marks
    FROM students s
    JOIN results r ON s.roll_no = r.roll_no
    WHERE s.roll_no = ?
    """, (roll_no,))
    data = c.fetchall()
    conn.close()
    return data


