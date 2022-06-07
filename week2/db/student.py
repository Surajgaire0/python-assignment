import sqlite3

import pyodbc


class Student:
    def __init__(self, id, fname, lname):
        self.fname = fname
        self.lname = lname
        self.id = id


class Fee:
    def __init__(self, student_id, amount):
        self.student_id = student_id
        self.amount = amount


def create_tables(cur, db_type):
    if db_type == "sqlite":
        cur.execute(
            """create table if not exists student (
            id integer primary key,
            fname text,
            lname text
        )"""
        )

        cur.execute(
            """create table if not exists fee (
                student_id integer,
                amount real,
                foreign key(student_id) references student(id)
                )"""
        )

    elif db_type == "sqlserver":
        cur.execute(
            """create table if not exists student (
            id int primary key,
            fname varchar(15),
            lname varchar(15)
        )"""
        )

        cur.execute(
            """create table if not exists fee (
                student_id int,
                amount real,
                foreign key(student_id) references student(id)
                )"""
        )

    else:
        raise Exception("db_type must be sqlite or sqlserver")


def add_student(cur, student):
    cur.execute(
        "insert into student values (:id,:fname,:lname)",
        {"id": student.id, "fname": student.fname, "lname": student.lname},
    )


def add_fee(cur, fee):
    cur.execute(
        "insert into fee values (:id,:amount)",
        {"id": fee.student_id, "amount": fee.amount},
    )


def display_student_info(cur, id):
    cur.execute(
        "select id, fname, lname, amount from student inner join fee on student.id=fee.student_id where student.id=?",
        (id,),
    )
    return cur.fetchall()


def create_connection(db_type):
    if db_type == "sqlite":
        conn = sqlite3.Connection("student.db")
        cur = conn.cursor()
    elif db_type == "sqlserver":
        conn_string = None  # replace it with conection string
        conn = pyodbc.connect(conn_string)
        cur = conn.cursor()
    else:
        raise Exception("db_type must be sqlite or sqlserver")
    return conn, cur


def main():
    db_type = input("Which dbms do you want to use? sqlite or sqlserver: ").lower()

    conn, cur = create_connection(db_type)

    create_tables(cur, db_type)

    student1 = Student(1, "Ram", "Sharma")
    student2 = Student(2, "Shyam", "Shah")

    fee1 = Fee(1, 10000)
    fee2 = Fee(2, 20000.4)

    with conn:
        add_student(cur, student1)
        add_fee(cur, fee1)
        add_student(cur, student2)
        add_fee(cur, fee2)

        stu_id = int(input("Enter student id:"))
        info = display_student_info(cur, stu_id)

        print(f"Student {stu_id} details: {info}")

    conn.close()


if __name__ == "__main__":
    main()
