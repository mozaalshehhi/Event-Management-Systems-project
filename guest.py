import pickle
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os

class GuestForm:
    #class to represent a GUI to enter guest details

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Guest Management System")
        
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        self.id_label = tk.Label(self.root, text="Guest ID:")
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
        
        self.submit_button = tk.Button(self.root, text="Add Guest", command=self.add_guest)
        self.submit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Guest", command=self.delete_guest)
        self.delete_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        
        self.modify_button = tk.Button(self.root, text="Modify Guest", command=self.modify_guest)
        self.modify_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
        
        self.display_all_button = tk.Button(self.root, text="Display All Guests", command=self.display_all_guests)
        self.display_all_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
        
        self.display_id_button = tk.Button(self.root, text="Display Guest by ID", command=self.display_guest_by_id)
        self.display_id_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)
        
        self.root.mainloop()

    def clear_boxes(self):
        #clear the entry boxes
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)

    def add_guest(self):
        #add guest
        name = self.name_entry.get()
        guest_id = self.id_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()

        guest = Guest(guest_id, name, address, contact_details)

        if guest_id in all_guests:
            tk.messagebox.showinfo("ID Check", f"The ID '{guest_id}' already exists for a guest.")
        else:
            all_guests[guest_id] = guest
            tk.messagebox.showinfo("ID Check", f"The guest with ID '{guest_id}' has been added successfully.")
            self.data_layer.write_guests_to_file(all_guests)
            self.clear_boxes()
            self.display_all_guests()

    def delete_guest(self):
        #delete guest
        guest_id = self.id_entry.get()

        if guest_id in all_guests:
            del all_guests[guest_id]
            tk.messagebox.showinfo("Deletion", f"The guest with ID '{guest_id}' has been deleted successfully.")
            self.data_layer.write_guests_to_file(all_guests)
            self.clear_boxes()
            self.display_all_guests()
        else:
            tk.messagebox.showinfo("Deletion", f"No guest found with ID '{guest_id}'.")

    def modify_guest(self):
        #modify guest
        guest_id = self.id_entry.get()

        if guest_id in all_guests:
            name = self.name_entry.get()
            address = self.address_entry.get()
            contact_details = self.contact_entry.get()

            guest = all_guests[guest_id]
            guest.name = name
            guest.address = address
            guest.contact_details = contact_details

            tk.messagebox.showinfo("Modification", f"The guest with ID '{guest_id}' has been modified successfully.")
            self.data_layer.write_guests_to_file(all_guests)
            self.clear_boxes()
            self.display_all_guests()
        else:
            tk.messagebox.showinfo("Modification", f"No guest found with ID '{guest_id}'.")

    def display_all_guests(self):
        #display all guests
        top = tk.Toplevel()
        top.title("All Guests")

        table = ttk.Treeview(top, columns=('ID', 'Name', 'Address', 'Contact Details'), show='headings')
        table.heading('ID', text='ID')
        table.heading('Name', text='Name')
        table.heading('Address', text='Address')
        table.heading('Contact Details', text='Contact Details')
        table.pack(pady=20)

        for guest in all_guests.values():
            table.insert('', 'end', values=(guest.guest_id, guest.name, guest.address, guest.contact_details))

    def display_guest_by_id(self):
        #display guest by ID
        guest_id = self.id_entry.get()

        if guest_id in all_guests:
            guest = all_guests[guest_id]
            top = tk.Toplevel()
            top.title(f"Guest Details - ID: {guest_id}")
            label = tk.Label(top, text=f"Name: {guest.name}\nID: {guest.guest_id}\nAddress: {guest.address}\nContact Details: {guest.contact_details}")
            label.pack(pady=20)
        else:
            tk.messagebox.showinfo("Guest Details", f"No guest found with ID '{guest_id}'.")

class Guest:
    #class to represent a guest

    def __init__(self, guest_id="", name="", address="", contact_details=""):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

class DataLayer:

    def __init__(self, filename):
        self.filename = filename

    def read_all_guests(self):
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                all_guests = pickle.load(file)
            return all_guests if isinstance(all_guests, dict) else {}

    def write_guests_to_file(self, all_guests):
        with open(self.filename, 'wb') as f:
            pickle.dump(all_guests, f)


filename = "guests.pkl"
data_layer = DataLayer(filename)
all_guests = data_layer.read_all_guests()

form = GuestForm(data_layer)
