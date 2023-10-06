import pyodbc

conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes"

db = pyodbc.connect(conn_str)
cur = db.cursor()

cur.execute("""
CREATE TABLE Student(
    StudentID int NOT NULL,
    FirstName nvarchar(40) NOT NULL,
    Surname nvarchar(30) NULL,
    Course nvarchar(30) NULL,
    City nvarchar(15) NULL,
    PRIMARY KEY (StudentID)
);
""")

db.commit()
db.close()