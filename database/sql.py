import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.execute("""
select
    *
from
    attendance as t0
    inner join
    employee as t1 on t0.id_employee = t1.id_employee;
""")
tablas = cursor.fetchall()

for tabla in tablas:

    print(tabla)

connection.close()