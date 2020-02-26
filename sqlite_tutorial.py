import sqlite3
from Employee import Employee

con = sqlite3.connect("employee.db")

c = con.cursor()

# c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Malte', 'Nie', 100000)

# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

con.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay':emp_2.pay})

# c.execute("SELECT * FROM employees WHERE last='Schafer'")
# c.execute("SELECT * FROM employees LIMIT 10")

c.execute("SELECT * FROM employees WHERE last=?", ('Schafer'))

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})

# print(c.fetchone())
# c.fetchmany(5)
print(c.fetchall())

con.commit()

con.close()