import tkinter as tk
from tkinter import messagebox
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rishabh.4002",
    database="employee_db"
)
cursor = db.cursor()


def add_employee():
    eid = entry_id.get()
    name = entry_name.get()
    pos = entry_pos.get()
    sal = entry_sal.get()

    if eid and name and pos and sal:
        cursor.execute(
            "INSERT INTO employees VALUES (%s,%s,%s,%s)",
            (eid, name, pos, sal)
        )
        db.commit()
        messagebox.showinfo("Success", "Employee Added")
    else:
        messagebox.showwarning("Error", "All fields required")

def remove_employee():
    eid = entry_id.get()
    cursor.execute("DELETE FROM employees WHERE emp_id=%s", (eid,))
    db.commit()
    messagebox.showinfo("Success", "Employee Removed")

def promote_employee():
    eid = entry_id.get()
    sal = entry_sal.get()
    cursor.execute(
        "UPDATE employees SET salary=%s WHERE emp_id=%s",
        (sal, eid)
    )
    db.commit()
    messagebox.showinfo("Success", "Employee Promoted")

def display_employee():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    display.delete("1.0", tk.END)
    for row in records:
        display.insert(tk.END, f"ID:{row[0]}  Name:{row[1]}  Role:{row[2]}  Salary:{row[3]}\n")


root = tk.Tk()
root.title("Employee Management System")
root.geometry("500x450")

tk.Label(root, text="Employee Management System", font=("Arial", 16)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Employee ID").grid(row=0, column=0)
tk.Label(frame, text="Name").grid(row=1, column=0)
tk.Label(frame, text="Position").grid(row=2, column=0)
tk.Label(frame, text="Salary").grid(row=3, column=0)

entry_id = tk.Entry(frame)
entry_name = tk.Entry(frame)
entry_pos = tk.Entry(frame)
entry_sal = tk.Entry(frame)

entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_pos.grid(row=2, column=1)
entry_sal.grid(row=3, column=1)

tk.Button(root, text="Add Employee", command=add_employee).pack(pady=5)
tk.Button(root, text="Remove Employee", command=remove_employee).pack(pady=5)
tk.Button(root, text="Promote Employee", command=promote_employee).pack(pady=5)
tk.Button(root, text="Display Employees", command=display_employee).pack(pady=5)

display = tk.Text(root, height=8, width=55)
display.pack(pady=10)

root.mainloop()
