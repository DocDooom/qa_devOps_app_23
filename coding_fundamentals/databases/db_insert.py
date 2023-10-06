import pyodbc
import csv

conn_str = r"DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes"
csv_path = "./students.csv"
student_tups = []

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:
        print(row)
        student_tups.append(tuple(row))
    

print(student_tups)

db = pyodbc.connect(conn_str)
cur = db.cursor()

for i in student_tups:
    print(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}")
    cur.execute(f"INSERT INTO Student VALUES ({i[0]},'{i[1]}','{i[2]}','{i[3]}','{i[4]}');")

db.commit()
db.close()