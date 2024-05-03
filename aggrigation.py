class Venue:

    def __init__(self, venue_id="", name="", address="", contact="", min_guests=0, max_guests=0):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests
class Client:
    def __init__(self, client_id="", name="", address="", contact_details="", budget=0.0):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget
class Guest:
    def __init__(self, guest_id="", name="", address="", contact_details=""):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
class Supplier:
    def __init__(self, supplier_id="", name="", address="", contact_details="", menu="", min_guests=0):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
class Event:
    def __init__(self, event_id="", type_="", theme="", date="", time="", duration="", venue=None,
                 client=None, guest_list=None, catering_company=""):
        if guest_list is None:
            guest_list = []
        self.event_id = event_id
        self.type_ = type_
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue  #aggregation--->Event has a Venue (Venue is part of Event)
        self.client = client  #aggregation---> Event has a Client (Client is part of Event)
        self.guest_list = guest_list  #aggregation--->Event has a list of Guests (Guests are part of Event)
        self.catering_company = catering_company  # Aggregation-----> Event has a catering company (Supplier is part of Event)
# Creating objects for aggregation example
venue = Venue(venue_id="A001", name="Hall 1", address="AD Main Street", contact="050...", min_guests=50, max_guests=200)
client = Client(client_id="B001", name="ABC Corp", address="456 Street RAK Street", contact_details="050...", budget=5000.0)
guest1 = Guest(guest_id="C001", name="John Doe", address="RAK ST 12", contact_details="050...")
guest2 = Guest(guest_id="D002", name="Jane Smith", address="Dubai Street 22", contact_details="050...")
supplier = Supplier(supplier_id="E001", name="Delicious Catering", address="AD Street 9", contact_details="050...", menu="Buffet", min_guests=50)
# Creating a Event object and assigning aggregated objects
event = Event(event_id="F001", type_="Birthday", theme="beach", date="2024-06-15", time="19:00", duration="4 hours",
              venue=venue, client=client, guest_list=[guest1, guest2], catering_company=supplier.name)
# Display Event attributes
print("Event Attributes:")
print("Event ID:", event.event_id)
print("Type:", event.type_)
print("Theme:", event.theme)
print("Date:", event.date)
print("Time:", event.time)
print("Duration:", event.duration)
print("Venue:", event.venue.name)  
print("Client:", event.client.name) 
print("Catering Company:", event.catering_company)
print()
# Display Venue attributes
print("Venue Attributes:")
print("Venue ID:", venue.venue_id)
print("Name:", venue.name)
print("Address:", venue.address)
print("Contact:", venue.contact)
print("Min Guests:", venue.min_guests)
print("Max Guests:", venue.max_guests)
print()
# Display Client attributes
print("Client Attributes:")
print("Client ID:", client.client_id)
print("Name:", client.name)
print("Address:", client.address)
print("Contact Details:", client.contact_details)
print("Budget:", client.budget)
print()
# Display Guest attributes
print("Guest Attributes:")
for guest in event.guest_list:
    print("Guest ID:", guest.guest_id)
    print("Name:", guest.name)
    print("Address:", guest.address)
    print("Contact Details:", guest.contact_details)
    print()
# Display Supplier attributes
print("Supplier Attributes:")
print("Supplier ID:", supplier.supplier_id)
print("Name:", supplier.name)
print("Address:", supplier.address)
print("Contact Details:", supplier.contact_details)
print("Menu:", supplier.menu)
print("Min Guests:", supplier.min_guests)
