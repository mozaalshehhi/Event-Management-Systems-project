import pickle
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os

class SupplierForm:
    #class for a GUI to enter supplier details

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x500")
        self.root.title("Supplier Management System")
        
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        self.id_label = tk.Label(self.root, text="Supplier ID:")
        self.id_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        
        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        
        self.contact_label = tk.Label(self.root, text="Contact Details:")
        self.contact_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.root)
        self.contact_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
        self.menu_label = tk.Label(self.root, text="Menu:")
        self.menu_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.menu_entry = tk.Entry(self.root)
        self.menu_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.min_guests_label = tk.Label(self.root, text="Minimum Guests:")
        self.min_guests_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.min_guests_entry = tk.Entry(self.root)
        self.min_guests_entry.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        self.max_guests_label = tk.Label(self.root, text="Maximum Guests:")
        self.max_guests_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        self.max_guests_entry = tk.Entry(self.root)
        self.max_guests_entry.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
        
        self.submit_button = tk.Button(self.root, text="Add Supplier", command=self.add_supplier)
        self.submit_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Supplier", command=self.delete_supplier)
        self.delete_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)
        
        self.modify_button = tk.Button(self.root, text="Modify Supplier", command=self.modify_supplier)
        self.modify_button.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)
        
        self.display_all_button = tk.Button(self.root, text="Display All Suppliers", command=self.display_all_suppliers)
        self.display_all_button.grid(column=1, row=10, sticky=tk.E, padx=5, pady=5)
        
        self.display_id_button = tk.Button(self.root, text="Display Supplier by ID", command=self.display_supplier_by_id)
        self.display_id_button.grid(column=1, row=11, sticky=tk.E, padx=5, pady=5)
        
        self.root.mainloop()

    def clear_boxes(self):
        #clear the entry boxes
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.menu_entry.delete(0, tk.END)
        self.min_guests_entry.delete(0, tk.END)
        self.max_guests_entry.delete(0, tk.END)

    def add_supplier(self):
        #add supplier
        name = self.name_entry.get()
        supplier_id = self.id_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        menu = self.menu_entry.get()
        min_guests = int(self.min_guests_entry.get())
        max_guests = int(self.max_guests_entry.get())

        supplier = Supplier(supplier_id, name, address, contact_details, menu, min_guests, max_guests)

        if supplier_id in all_suppliers:
            tk.messagebox.showinfo("ID Check", f"The ID '{supplier_id}' already exists for a supplier.")
        else:
            all_suppliers[supplier_id] = supplier
            tk.messagebox.showinfo("ID Check", f"The supplier with ID '{supplier_id}' has been added successfully.")
            self.data_layer.write_suppliers_to_file(all_suppliers)
            self.clear_boxes()
            self.display_all_suppliers()

    def delete_supplier(self):
        #delete supplier
        supplier_id = self.id_entry.get()

        if supplier_id in all_suppliers:
            del all_suppliers[supplier_id]
            tk.messagebox.showinfo("Deletion", f"The supplier with ID '{supplier_id}' has been deleted successfully.")
            self.data_layer.write_suppliers_to_file(all_suppliers)
            self.clear_boxes()
            self.display_all_suppliers()
        else:
            tk.messagebox.showinfo("Deletion", f"No supplier found with ID '{supplier_id}'.")

    def modify_supplier(self):
        #modify supplier
        supplier_id = self.id_entry.get()

        if supplier_id in all_suppliers:
            name = self.name_entry.get()
            address = self.address_entry.get()
            contact_details = self.contact_entry.get()
            menu = self.menu_entry.get()
            min_guests = int(self.min_guests_entry.get())
            max_guests = int(self.max_guests_entry.get())

            supplier = all_suppliers[supplier_id]
            supplier.name = name
            supplier.address = address
            supplier.contact_details = contact_details
            supplier.menu = menu
            supplier.min_guests = min_guests
            supplier.max_guests = max_guests

            tk.messagebox.showinfo("Modification", f"The supplier with ID '{supplier_id}' has been modified successfully.")
            self.data_layer.write_suppliers_to_file(all_suppliers)
            self.clear_boxes()
            self.display_all_suppliers()
        else:
            tk.messagebox.showinfo("Modification", f"No supplier found with ID '{supplier_id}'.")

    def display_all_suppliers(self):
        #display all suppliers
        top = tk.Toplevel()
        top.title("All Suppliers")

        table = ttk.Treeview(top, columns=('ID', 'Name', 'Address', 'Contact Details', 'Menu', 'Min Guests', 'Max Guests'), show='headings')
        table.heading('ID', text='ID')
        table.heading('Name', text='Name')
        table.heading('Address', text='Address')
        table.heading('Contact Details', text='Contact Details')
        table.heading('Menu', text='Menu')
        table.heading('Min Guests', text='Min Guests')
        table.heading('Max Guests', text='Max Guests')
        table.pack(pady=20)

        for supplier in all_suppliers.values():
            table.insert('', 'end', values=(supplier.supplier_id, supplier.name, supplier.address, supplier.contact_details, supplier.menu, supplier.min_guests, supplier.max_guests))

    def display_supplier_by_id(self):
        #display supplier by ID
        supplier_id = self.id_entry.get()

        if supplier_id in all_suppliers:
            supplier = all_suppliers[supplier_id]
            top = tk.Toplevel()
            top.title(f"Supplier Details - ID: {supplier_id}")
            label = tk.Label(top, text=f"Name: {supplier.name}\nID: {supplier.supplier_id}\nAddress: {supplier.address}\nContact Details: {supplier.contact_details}\nMenu: {supplier.menu}\nMin Guests: {supplier.min_guests}\nMax Guests: {supplier.max_guests}")
            label.pack(pady=20)
        else:
            tk.messagebox.showinfo("Supplier Details", f"No supplier found with ID '{supplier_id}'.")

class Supplier:
    #class to represent a supplier

    def __init__(self, supplier_id="", name="", address="", contact_details="", menu="", min_guests=0, max_guests=0):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

class DataLayer:
    #class read / write operations for supplier data

    def __init__(self, filename):
        self.filename = filename

    def read_all_suppliers(self):
        #read all suppliers from file
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                all_suppliers = pickle.load(file)
            return all_suppliers if isinstance(all_suppliers, dict) else {}

    def write_suppliers_to_file(self, all_suppliers):
        #write suppliers to file
        with open(self.filename, 'wb') as f:
            pickle.dump(all_suppliers, f)


filename = "suppliers.pkl"
data_layer = DataLayer(filename)
all_suppliers = data_layer.read_all_suppliers()

form = SupplierForm(data_layer)
