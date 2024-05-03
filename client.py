import pickle
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os

class ClientForm:
    #class to represent a GUI to enter client details

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Client Management System")
        
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        self.id_label = tk.Label(self.root, text="Client ID:")
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
        
        self.budget_label = tk.Label(self.root, text="Budget:")
        self.budget_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.budget_entry = tk.Entry(self.root)
        self.budget_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        
        self.submit_button = tk.Button(self.root, text="Add Client", command=self.add_client)
        self.submit_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Client", command=self.delete_client)
        self.delete_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
        
        self.modify_button = tk.Button(self.root, text="Modify Client", command=self.modify_client)
        self.modify_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
        
        self.display_all_button = tk.Button(self.root, text="Display All Clients", command=self.display_all_clients)
        self.display_all_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)
        
        self.display_id_button = tk.Button(self.root, text="Display Client by ID", command=self.display_client_by_id)
        self.display_id_button.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)
        
        self.root.mainloop()

    def clear_boxes(self):
        #clear the entry boxes
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)

    def add_client(self):
        #add client
        name = self.name_entry.get()
        client_id = self.id_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        budget = float(self.budget_entry.get())

        client = Client(client_id, name, address, contact_details, budget)

        if client_id in all_clients:
            tk.messagebox.showinfo("ID Check", f"The ID '{client_id}' already exists for a client.")
        else:
            all_clients[client_id] = client
            tk.messagebox.showinfo("ID Check", f"The client with ID '{client_id}' has been added successfully.")
            self.data_layer.write_clients_to_file(all_clients)
            self.clear_boxes()
            self.display_all_clients()

    def delete_client(self):
        #delete client
        client_id = self.id_entry.get()

        if client_id in all_clients:
            del all_clients[client_id]
            tk.messagebox.showinfo("Deletion", f"The client with ID '{client_id}' has been deleted successfully.")
            self.data_layer.write_clients_to_file(all_clients)
            self.clear_boxes()
            self.display_all_clients()
        else:
            tk.messagebox.showinfo("Deletion", f"No client found with ID '{client_id}'.")

    def modify_client(self):
        #modify client
        client_id = self.id_entry.get()

        if client_id in all_clients:
            name = self.name_entry.get()
            address = self.address_entry.get()
            contact_details = self.contact_entry.get()
            budget = float(self.budget_entry.get())

            client = all_clients[client_id]
            client.name = name
            client.address = address
            client.contact_details = contact_details
            client.budget = budget

            tk.messagebox.showinfo("Modification", f"The client with ID '{client_id}' has been modified successfully.")
            self.data_layer.write_clients_to_file(all_clients)
            self.clear_boxes()
            self.display_all_clients()
        else:
            tk.messagebox.showinfo("Modification", f"No client found with ID '{client_id}'.")

    def display_all_clients(self):
        #display all clients
        top = tk.Toplevel()
        top.title("All Clients")

        table = ttk.Treeview(top, columns=('ID', 'Name', 'Address', 'Contact Details', 'Budget'), show='headings')
        table.heading('ID', text='ID')
        table.heading('Name', text='Name')
        table.heading('Address', text='Address')
        table.heading('Contact Details', text='Contact Details')
        table.heading('Budget', text='Budget')
        table.pack(pady=20)

        for client in all_clients.values():
            table.insert('', 'end', values=(client.client_id, client.name, client.address, client.contact_details, client.budget))

    def display_client_by_id(self):
        #display client by ID
        client_id = self.id_entry.get()

        if client_id in all_clients:
            client = all_clients[client_id]
            top = tk.Toplevel()
            top.title(f"Client Details - ID: {client_id}")
            label = tk.Label(top, text=f"Name: {client.name}\nID: {client.client_id}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}")
            label.pack(pady=20)
        else:
            tk.messagebox.showinfo("Client Details", f"No client found with ID '{client_id}'.")

class Client:
    #class to represent a client

    def __init__(self, client_id="", name="", address="", contact_details="", budget=0.0):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

class DataLayer:
    #class to handle read and write operations for client data

    def __init__(self, filename):
        self.filename = filename

    def read_all_clients(self):
        #read all clients from file
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                all_clients = pickle.load(file)
            return all_clients if isinstance(all_clients, dict) else {}

    def write_clients_to_file(self, all_clients):
        #write clients to file
        with open(self.filename, 'wb') as f:
            pickle.dump(all_clients, f)


filename = "clients.pkl"
data_layer = DataLayer(filename)
all_clients = data_layer.read_all_clients()

form = ClientForm(data_layer)
