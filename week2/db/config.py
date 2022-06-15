schema = {
    "students": {
        "sqlite": {"id": "integer primary key", "fname": "text", "lname": "text"},
        "sqlserver": {"id": "int primary key", "fname": "varchar(15)", "lname": "varchar(15)"},
    },
    "fee": {
        "sqlite": {"student_id": "integer unique not null", "amount": "real not null"},
        "sqlserver": {"student_id": "int unique not null", "amount": "real not null"},
    },
}

# config for SQL Server
driver = "{ODBC Driver 17 for SQL Server}"
server = "server"  # needs replacement
database = "db"  # needs replacement
username = "username"  # needs replacement
password = "password"  # needs replacement

db = {
    "sqlite": "student.db",
    "sqlserver": f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}",
}
