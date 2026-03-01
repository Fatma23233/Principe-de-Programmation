from db import get_connection


def get_all_students():
    conn   = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result


def get_student_by_id(student_id):
    conn   = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    cursor.close()
    conn.close()
    return student


def add_student(name, age):   
    conn   = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO students (name, age) VALUES (%s, %s)" 
    cursor.execute(query, (name, age))
    conn.commit()
    new_id = cursor.lastrowid

    cursor.close()
    conn.close()
    return new_id


def update_student(student_id, name, age):   
    conn   = get_connection()
    cursor = conn.cursor()

    query = "UPDATE students SET name = %s, age = %s WHERE id = %s"
    cursor.execute(query, (name, age, student_id))
    conn.commit()
    affected = cursor.rowcount

    cursor.close()
    conn.close()
    return affected


def delete_student(student_id):
    conn   = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    affected = cursor.rowcount

    cursor.close()
    conn.close()
    return affected