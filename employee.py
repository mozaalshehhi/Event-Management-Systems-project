import pickle## Importing pickle module for serialization/de
import tkinter as tk#for the GUI
from tkinter import ttk#Importing ttk
import tkinter.messagebox#for displaying messages
import os#file operations

class EmployeeForm:
    

    def __init__(self, data_layer):
        self.data_layer = data_layer#interacting with employee data
        self.root = tk.Tk()#make windoow
        self.root.geometry("400x400")#decide on the size of the root window
        self.root.title("Employee Management System")#its title
                # make labels and stuff to enter for. so, employee attributes!

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
                # Now the buttons to click! on the assigned operations in the assignment so ddd, delete, modify, display all, display by the ID

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
        
        self.root.mainloop()## Start the Tkinter event loop

    def clear_boxes(self):
        #clear all entry boxes in the GUI 
        self.name_entry.delete(0, tk.END)#clear the name
        self.id_entry.delete(0, tk.END)# clear the id and so on.....
        self.department_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)

    def add_employee(self):
        #add new employes
        name = self.name_entry.get()# get the name from the 'Name' entry box
        id = self.id_entry.get()# get the employee ID from the 'Employee ID' entry box and so on....
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()

        employee = Employee(name, id, department, job_title)#make the new emp obj

        if id in all_employees:#see if the ID already exists in the dictionary of all employees so that it give a message for so
            tk.messagebox.showinfo("ID Check", f"The ID '{id}' already exists for an employee.")#it will show this if soo
        else:
            all_employees[id] = employee#else so if the id is not there then add the new employee to the dictionary
            tk.messagebox.showinfo("ID Check", f"The employee with ID '{id}' has been added successfully.")
            self.data_layer.write_employees_to_file(all_employees)# updated
            self.clear_boxes()## Will clear entry boxes in the GUI , so that we can repete the proccess of addiing new emp
            self.display_all_employees() # Display all employees in the GUI

    def delete_employee(self):
        #del employee
        id = self.id_entry.get()# Getting the employee ID from the 'Employee ID' entry box

        if id in all_employees:# See if the ID exists in the dictionary of all employee
            del all_employees[id]
            tk.messagebox.showinfo("Deletion", f"The employee with ID '{id}' has been deleted successfully.")
            self.data_layer.write_employees_to_file(all_employees)
            self.clear_boxes()# del fron dict
            self.display_all_employees()# Display all employees in the GUI
        else:
            tk.messagebox.showinfo("Deletion", f"No employee found with ID '{id}'.")

    def modify_employee(self):
        #mod employee
        id = self.id_entry.get()# Getting the employee ID from the 'Employee ID' entry box as we did in the others above


        if id in all_employees:# See if the ID exists in the dictionary of all employees
            name = self.name_entry.get()## Getting the new name from the 'Name' entry box and so on for the dep, job ..
            department = self.department_entry.get()# Update the employee's name
            job_title = self.job_title_entry.get()

            employee = all_employees[id]#here we can see/get the employee object using the ID the inputed
            employee.name = name# Update the employee's name and the dep, job below and so on....
            employee.department = department
            employee.job_title = job_title

            tk.messagebox.showinfo("Modification", f"The employee with ID '{id}' has been modified successfully.")
            self.data_layer.write_employees_to_file(all_employees)
            self.clear_boxes()
            self.display_all_employees()
        else:
            tk.messagebox.showinfo("Modification", f"No employee found with ID '{id}'.")# Show the message if no employee found so that they know

    def display_all_employees(self):
        #dis all the employe
        top = tk.Toplevel()# make a new window
        top.title("All Employees")#this is the title remember this is a new window that will open to show all detail
#Treeview widget to display employee details in a row
        table = ttk.Treeview(top, columns=('ID', 'Name', 'Department', 'Job Title'), show='headings')
        table.heading('ID', text='ID')#colums
        table.heading('Name', text='Name')#colums....
        table.heading('Department', text='Department')
        table.heading('Job Title', text='Job Title')
        table.pack(pady=20)

        for employee in all_employees.values():#now we iterate all employees and insert their details into the table
            table.insert('', 'end', values=(employee.id, employee.name, employee.department, employee.job_title))

    def display_employee_by_id(self):
        #dis the employe by the ID , same before 
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
    #class to represent a employe

    def __init__(self, name="", id="", department="", job_title=""):
        self.name = name
        self.id = id
        self.department = department
        self.job_title = job_title

class DataLayer:
    #class for employees data

    def __init__(self, filename):
        self.filename = filename

    def read_all_employees(self):
        #read all the employees from file
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                all_employees = pickle.load(file)
            return all_employees if isinstance(all_employees, dict) else {}

    def write_employees_to_file(self, all_employees):
        #write employees to the file
        with open(self.filename, 'wb') as f:
            pickle.dump(all_employees, f)


filename = "employees.pkl"#a typical name of the file that saves/storing the employee data
data_layer = DataLayer(filename)
all_employees = data_layer.read_all_employees()#reading

form = EmployeeForm(data_layer) # makeing a object of EmployeeForm
