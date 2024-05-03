import pickle
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os

class EmployeeForm:
    """Class to represent a GUI form to enter employee details"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Employee Management System")
        
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        self.id_label = tk.Label(self.root, text="Employee ID:")
        self.id_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        
        self.department_label = tk.Label(self.root, text="Department:")
        self.department_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.department_entry = tk.Entry(self.root)
        self.department_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        
        self.job_title_label = tk.Label(self.root, text="Job Title:")
        self.job_title_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.job_title_entry = tk.Entry(self.root)
        self.job_title_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
        self.submit_button = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.submit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Employee", command=self.delete_employee)
        self.delete_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        
        self.modify_button = tk.Button(self.root, text="Modify Employee", command=self.modify_employee)
        self.modify_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
        
        self.display_all_button = tk.Button(self.root, text="Display All Employees", command=self.display_all_employees)
        self.display_all_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
        
        self.display_id_button = tk.Button(self.root, text="Display Employee by ID", command=self.display_employee_by_id)
        self.display_id_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)
        
        self.root.mainloop()

    def clear_boxes(self):
        """Clear the entry boxes"""
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)

    def add_employee(self):
        """Add employee"""
        name = self.name_entry.get()
        id = self.id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()

        employee = Employee(name, id, department, job_title)

        if id in all_employees:
            tk.messagebox.showinfo("ID Check", f"The ID '{id}' already exists for an employee.")
        else:
            all_employees[id] = employee
            tk.messagebox.showinfo("ID Check", f"The employee with ID '{id}' has been added successfully.")
            self.data_layer.write_employees_to_file(all_employees)
            self.clear_boxes()
            self.display_all_employees()

    def delete_employee(self):
        """Delete employee"""
        id = self.id_entry.get()

        if id in all_employees:
            del all_employees[id]
            tk.messagebox.showinfo("Deletion", f"The employee with ID '{id}' has been deleted successfully.")
            self.data_layer.write_employees_to_file(all_employees)
            self.clear_boxes()
            self.display_all_employees()
        else:
            tk.messagebox.showinfo("Deletion", f"No employee found with ID '{id}'.")

    def modify_employee(self):
        """Modify employee"""
        id = self.id_entry.get()

        if id in all_employees:
            name = self.name_entry.get()
            department = self.department_entry.get()
            job_title = self.job_title_entry.get()

            employee = all_employees[id]
            employee.name = name
            employee.department = department
            employee.job_title = job_title

            tk.messagebox.showinfo("Modification", f"The employee with ID '{id}' has been modified successfully.")
            self.data_layer.write_employees_to_file(all_employees)
            self.clear_boxes()
            self.display_all_employees()
        else:
            tk.messagebox.showinfo("Modification", f"No employee found with ID '{id}'.")

    def display_all_employees(self):
        """Display all employees"""
        top = tk.Toplevel()
        top.title("All Employees")

        table = ttk.Treeview(top, columns=('ID', 'Name', 'Department', 'Job Title'), show='headings')
        table.heading('ID', text='ID')
        table.heading('Name', text='Name')
        table.heading('Department', text='Department')
        table.heading('Job Title', text='Job Title')
        table.pack(pady=20)

        for employee in all_employees.values():
            table.insert('', 'end', values=(employee.id, employee.name, employee.department, employee.job_title))

    def display_employee_by_id(self):
        """Display employee by ID"""
        id = self.id_entry.get()

        if id in all_employees:
            employee = all_employees[id]
            top = tk.Toplevel()
            top.title(f"Employee Details - ID: {id}")
            label = tk.Label(top, text=f"Name: {employee.name}\nID: {employee.id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}")
            label.pack(pady=20)
        else:
            tk.messagebox.showinfo("Employee Details", f"No employee found with ID '{id}'.")

class Employee:
    """Class to represent an employee"""

    def __init__(self, name="", id="", department="", job_title=""):
        self.name = name
        self.id = id
        self.department = department
        self.job_title = job_title

class DataLayer:
    """Class to handle read and write operations for employee data"""

    def __init__(self, filename):
        self.filename = filename

    def read_all_employees(self):
        """Read all employees from file"""
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                all_employees = pickle.load(file)
            return all_employees if isinstance(all_employees, dict) else {}

    def write_employees_to_file(self, all_employees):
        """Write employees to file"""
        with open(self.filename, 'wb') as f:
            pickle.dump(all_employees, f)


filename = "employees.pkl"
data_layer = DataLayer(filename)
all_employees = data_layer.read_all_employees()

form = EmployeeForm(data_layer)
