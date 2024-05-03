import pickle## Importing pickle module for serialization/de
import tkinter as tk#for the GUI
from tkinter import ttk#Importing ttk
import tkinter.messagebox#for displaying messages
import os#file operations

class EventForm:
    #class for GUI / manage event details

    def __init__(self, data_layer):#constructor meth, initialize EventForm object
        self.data_layer = data_layer
        self.root = tk.Tk()# make the main window
        self.root.geometry("400x400")#decide on the size of the root window
        self.root.title("Event Management System")
        # make the labels / input boxe for event details
        self.id_label = tk.Label(self.root, text="Event ID:")
        self.id_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        self.type_label = tk.Label(self.root, text="Type:")
        self.type_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.type_entry = tk.Entry(self.root)
        self.type_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        
        self.theme_label = tk.Label(self.root, text="Theme:")
        self.theme_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.theme_entry = tk.Entry(self.root)
        self.theme_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        
        self.date_label = tk.Label(self.root, text="Date:")
        self.date_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
        self.time_label = tk.Label(self.root, text="Time:")
        self.time_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        # Button to click so that we add an event and so on for the rest
        self.submit_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        self.submit_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        #notice that it is by ID i did it for all just to test it and i liked it more that what the assignment suggested
        #but the rest i followed the assignment instructions!! 
        self.display_button = tk.Button(self.root, text="Display Event by ID", command=self.display_event_by_id)
        self.display_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Event by ID", command=self.delete_event_by_id)
        self.delete_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
        
        self.modify_button = tk.Button(self.root, text="Modify Event by ID", command=self.modify_event_by_id)
        self.modify_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)
        
        self.display_all_button = tk.Button(self.root, text="Display All Events", command=self.display_all_events)
        self.display_all_button.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)
        
        self.root.mainloop()# Running main event loop

    def clear_boxes(self):
        #clear the entry boxes
        self.id_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.theme_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

    def add_event(self):
        #add event
        # get the data from entry boxes
        event_id = self.id_entry.get()
        type_ = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        event = Event(event_id, type_, theme, date, time)# Make a Event object with the data inputs

        if event_id in all_events:#see if the id is there/exists
            tk.messagebox.showinfo("ID Check", f"The ID '{event_id}' already exists for an event.")#notify with message
        else:
            all_events[event_id] = event
            tk.messagebox.showinfo("ID Check", f"The event with ID '{event_id}' has been added successfully.")
            self.data_layer.write_events_to_file(all_events)
            self.clear_boxes()# Clear entry boxes

    def display_event_by_id(self):
        #display event by ID
        id = self.id_entry.get()

        if id in all_events:
            event = all_events[id]
            top = tk.Toplevel()
            top.title(f"Event Details - ID: {id}")
            label = tk.Label(top, text=f"Type: {event.type_}\nTheme: {event.theme}\nDate: {event.date}\nTime: {event.time}")
            label.pack(pady=20)
        else:
            tk.messagebox.showinfo("Event Details", f"No event found with ID '{id}'.")

    def delete_event_by_id(self):
        #delete event by ID
        id = self.id_entry.get()

        if id in all_events:
            del all_events[id]
            tk.messagebox.showinfo("Deletion", f"The event with ID '{id}' has been deleted successfully.")
            self.data_layer.write_events_to_file(all_events)
            self.clear_boxes()
        else:
            tk.messagebox.showinfo("Deletion", f"No event found with ID '{id}'.")

    def modify_event_by_id(self):
        #modify event by ID
        event_id = self.id_entry.get()
        type_ = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        if event_id in all_events:
            event = all_events[event_id]
            event.type_ = type_
            event.theme = theme
            event.date = date
            event.time = time

            tk.messagebox.showinfo("Modification", f"The event with ID '{event_id}' has been modified successfully.")
            self.data_layer.write_events_to_file(all_events)
            self.clear_boxes()
        else:
            tk.messagebox.showinfo("Modification", f"No event found with ID '{event_id}'.")

    def display_all_events(self):
        #display all events
        top = tk.Toplevel()
        top.title("All Events")

        table = ttk.Treeview(top, columns=('ID', 'Type', 'Theme', 'Date', 'Time'), show='headings')
        table.heading('ID', text='ID')
        table.heading('Type', text='Type')
        table.heading('Theme', text='Theme')
        table.heading('Date', text='Date')
        table.heading('Time', text='Time')
        table.pack(pady=20)

        for event in all_events.values():
            table.insert('', 'end', values=(event.event_id, event.type_, event.theme, event.date, event.time))

class Event:
    #class to represent an event

    def __init__(self, event_id="", type_="", theme="", date="", time=""):
        self.event_id = event_id
        self.type_ = type_
        self.theme = theme
        self.date = date
        self.time = time

class DataLayer:
    #class for the read / write for events

    def __init__(self, filename):
        self.filename = filename

    def read_all_events(self):
        #read all events from file
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                all_events = pickle.load(file)
            return all_events if isinstance(all_events, dict) else {}

    def write_events_to_file(self, all_events):
        #write events to file
        with open(self.filename, 'wb') as f:
            pickle.dump(all_events, f)

filename = "events.pkl"
data_layer = DataLayer(filename)
all_events = data_layer.read_all_events()

event_form = EventForm(data_layer)
