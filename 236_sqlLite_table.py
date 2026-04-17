import sqlite3

# craete a database if not exist and return conection object 
conn= sqlite3.connect("company.db")


cursor= conn.cursor()

cursor.execute(""" 
create table if not exists employees (
               emp_id integer primary key autoincrement,
               name text not null,
               department text not null,
               sallary real not null,
               joining_date text not null )""")

# emp=[("ram","IT",12000,"12/01/2025"),("raj","IT",15000,"15/01/2025"),("mohan","HR",1000,"30/01/2025")]

# cursor.executemany("insert into employees (name , department, sallary ,joining_date) values (?,?,?,?) ",emp)

conn.commit()   

cursor.execute("select * from employees")
rows= cursor.fetchall()
print("\nall data of table :- ")
for row in rows:
    print(row)

cursor.execute("select * from employees where  department='IT'")
rows= cursor.fetchall()
print("\nonly  data of IT table :- ")
for row in rows:
    print(row)    

conn.close()
