schema = {
    "student": {
        "sqlite": {"id": "integer primary key", "fname": "text", "lname": "text"},
        "sqlserver": {"id": "int primary key", "fname": "varchar(15)", "lname": "varchar(15)"},
    },
    "fee": {
        "sqlite": {"student_id": "integer unique not null", "amount": "real not null"},
        "sqlserver": {"student_id": "int unique not null", "amount": "real not null"},
    },
}

db = {"sqlite": "student.db", "sqlserver": None}
