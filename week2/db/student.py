import sqlite3

import pyodbc

from config import db, schema


def create_table(cur, db_type, table):
    sql = (
        # "create table if not exists "
        "create table "
        + table
        + " ( "
        + ",".join([col + " " + dtype for col, dtype in schema[table][db_type].items()])
        + " )"
    )
    cur.execute(sql)


def insert(cur, db_type, table):
    columns = schema[table][db_type].keys()  # column names
    values = [input(f"Enter {col}: ") for col in columns]  # ask for values to insert
    values = ["'{}'".format(value) if not value.isnumeric() else value for value in values]

    cur.execute("insert into {} values ({})".format(table, ",".join(values)))


def read(cur, table: "str", columns: "str" = "*", condition: "str" = "1=1"):
    cur.execute(
        "Select {} from {} where {}".format(
            columns,
            table,
            condition,
        )
    )
    return cur.fetchall()


def update(cur, table: "str", newdata: "dict", condition: "str"):
    cur.execute(
        "Update {} set {} where {}".format(
            table,
            ",".join(["{}='{}'".format(col, values) for col, values in newdata.items()]),
            condition,
        )
    )


def delete(cur, table: "str", condition: "str"):
    cur.execute(
        "Delete from {} where {}".format(
            table,
            condition,
        )
    )


def join(
    cur,
    table1,
    table2,
    join_condition: str,
    columns: str = "*",
    join_type="inner join",
    where_condition="1=1",
):
    cur.execute(
        f"select {columns} from {table1} {join_type} {table2} on {join_condition} where {where_condition}"
    )
    return cur.fetchall()


def create_connection(db_type):
    if db_type == "sqlite":
        conn = sqlite3.Connection(db[db_type])
        cur = conn.cursor()
    elif db_type == "sqlserver":
        conn = pyodbc.connect(db[db_type])
        cur = conn.cursor()
    else:
        raise Exception("db_type must be sqlite or sqlserver")
    return conn, cur


def main():
    db_type = input("Which dbms do you want to use? sqlite or sqlserver: ").lower()

    conn, cur = create_connection(db_type)

    # create_table(cur, db_type, "students") #uncomment to create students table
    # create_table(cur, db_type, "fee") # uncomment to  create fee table

    with conn:
        # CRUD operations for student table

        # insert row in student table
        # insert(cur, "sqlite", "students")
        insert(cur, "sqlite", "students")

        # select fname, lname from students where lname like 'S%'
        print(
            "Students whose last name begins with s: ",
            read(cur, "students", "fname, lname", "lname like 'S%'"),
        )

        # select * from students
        print("All entries from student", read(cur, "students"))

        # Update students set fname=try where id=1
        update(cur, "students", {"fname": "try"}, "id=1")

        # delete from students where lname like 'g%'
        delete(cur, "students", "fname like 'g%'")

        # CRUD operations for fee table

        insert(cur, "sqlite", "fee")
        # insert(cur, "sqlite", "fee")

        print("Student id whose amount > 100: ", read(cur, "fee", "student_id", "amount>100"))

        print("All entries from fee", read(cur, "fee"))

        update(cur, "fee", {"amount": 200}, "student_id=1")

        delete(cur, "fee", "student_id=2")

        # display joined table
        print("Student 1 data (joining student and fee): ", end="")
        print(
            join(
                cur,
                "students",
                "fee",
                join_condition="students.id=fee.student_id",
                join_type="inner join",
                where_condition="id=1",
            )
        )

    conn.close()


if __name__ == "__main__":
    main()
