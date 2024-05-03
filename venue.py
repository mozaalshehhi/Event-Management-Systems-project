from tkinter import ttk
import tkinter.messagebox
import os

class VenueForm:

    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x500")
        self.root.title("Venue Management System")
        
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        self.id_label = tk.Label(self.root, text="Venue ID:")
        self.id_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        
        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        
        self.contact_label = tk.Label(self.root, text="Contact:")
        self.contact_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.root)
        self.contact_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
        self.min_guests_label = tk.Label(self.root, text="Minimum Guests:")
        self.min_guests_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.min_guests_entry = tk.Entry(self.root)
        self.min_guests_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.max_guests_label = tk.Label(self.root, text="Maximum Guests:")
        self.max_guests_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.max_guests_entry = tk.Entry(self.root)
        self.max_guests_entry.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        
        self.submit_button = tk.Button(self.root, text="Add Venue", command=self.add_venue)
        self.submit_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Venue", command=self.delete_venue)
        self.delete_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
        
        self.modify_button = tk.Button(self.root, text="Modify Venue", command=self.modify_venue)
        self.modify_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)
        
        self.display_all_button = tk.Button(self.root, text="Display All Venues", command=self.display_all_venues)
        self.display_all_button.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)
        
        self.display_id_button = tk.Button(self.root, text="Display Venue by ID", command=self.display_venue_by_id)
        self.display_id_button.grid(column=1, row=10, sticky=tk.E, padx=5, pady=5)
        
        self.root.mainloop()

    def clear_boxes(self):    
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.min_guests_entry.delete(0, tk.END)
        self.max_guests_entry.delete(0, tk.END)

    def add_venue(self):
        name = self.name_entry.get()
        venue_id = self.id_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        min_guests = int(self.min_guests_entry.get())
        max_guests = int(self.max_guests_entry.get())

        venue = Venue(venue_id, name, address, contact, min_guests, max_guests)

        if venue_id in all_venues:
            tk.messagebox.showinfo("ID Check", f"The ID '{venue_id}' already exists for a venue.")
        else:
            all_venues[venue_id] = venue
            tk.messagebox.showinfo("ID Check", f"The venue with ID '{venue_id}' has been added successfully.")
            self.data_layer.write_venues_to_file(all_venues)
            self.clear_boxes()
            self.display_all_venues()

    def delete_venue(self):
        venue_id = self.id_entry.get()

        if venue_id in all_venues:
            del all_venues[venue_id]
            tk.messagebox.showinfo("Deletion", f"The venue with ID '{venue_id}' has been deleted successfully.")
            self.data_layer.write_venues_to_file(all_venues)
            self.clear_boxes()
            self.display_all_venues()
        else:
            tk.messagebox.showinfo("Deletion", f"No venue found with ID '{venue_id}'.")

    def modify_venue(self):
        venue_id = self.id_entry.get()
        if venue_id in all_venues:
            name = self.name_entry.get()
            address = self.address_entry.get()
            contact = self.contact_entry.get()
            min_guests = int(self.min_guests_entry.get())
            max_guests = int(self.max_guests_entry.get())
            venue = all_venues[venue_id]
            venue.name = name
            venue.address = address
            venue.contact = contact
            venue.min_guests = min_guests
            venue.max_guests = max_guests
            tk.messagebox.showinfo("Modification", f"The venue with ID '{venue_id}' has been modified successfully.")
            self.data_layer.write_venues_to_file(all_venues)
            self.clear_boxes()
            self.display_all_venues()
        else:
            tk.messagebox.showinfo("Modification", f"No venue found with ID '{venue_id}'.")

    def display_all_venues(self):
        top = tk.Toplevel()
        top.title("All Venues")
        table = ttk.Treeview(top, columns=('ID', 'Name', 'Address', 'Contact', 'Min Guests', 'Max Guests'), show='headings')
        table.heading('ID', text='ID')
        table.heading('Name', text='Name')
        table.heading('Address', text='Address')
        table.heading('Contact', text='Contact')
        table.heading('Min Guests', text='Min Guests')
        table.heading('Max Guests', text='Max Guests')
        table.pack(pady=20)

        for venue in all_venues.values():
            table.insert('', 'end', values=(venue.venue_id, venue.name, venue.address, venue.contact, venue.min_guests, venue.max_guests))

    def display_venue_by_id(self):
      
        venue_id = self.id_entry.get()

        if venue_id in all_venues:
            venue = all_venues[venue_id]
            top = tk.Toplevel()
            top.title(f"Venue Details - ID: {venue_id}")
            label = tk.Label(top, text=f"Name: {venue.name}\nID: {venue.venue_id}\nAddress: {venue.address}\nContact: {venue.contact}\nMin Guests: {venue.min_guests}\nMax Guests: {venue.max_guests}")
            label.pack(pady=20)
        else:
            tk.messagebox.showinfo("Venue Details", f"No venue found with ID '{venue_id}'.")

class Venue:

    def __init__(self, venue_id="", name="", address="", contact="", min_guests=0, max_guests=0):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

class DataLayer:

    def __init__(self, filename):
        self.filename = filename

    def read_all_venues(self):
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                all_venues = pickle.load(file)
            return all_venues if isinstance(all_venues, dict) else {}

    def write_venues_to_file(self, all_venues):
        with open(self.filename, 'wb') as f:
            pickle.dump(all_venues, f)


filename = "venues.pkl"
data_layer = DataLayer(filename)
all_venues = data_layer.read_all_venues()

form = VenueForm(data_layer)
