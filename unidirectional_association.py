#unidirectional association
class Employee:
    def __init__(self, name="", id="", department="", job_title=""):
        self.name = name
        self.id = id
        self.department = department
        self.job_title = job_title
class Event:#does not need to know about the Employee its a "event" so by logic it does not have the ability to know..
    def __init__(self, event_id="", type_="", theme="", date="", time="", duration=""):
        self.event_id = event_id
        self.type_ = type_
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.employee = None  # employee associated with the event
# Creating a emoloyee object
employee = Employee(name="Moza Talib", id="A009", department="Sales", job_title="Manager")
# Creating a event object and associating it with the employee
event = Event(event_id="B0010", type_="Birthday", theme="Birthday", date="2024-06-15", time="19:00", duration="4 hours")
event.employee = employee
# Display Event attributes
print("Event Attributes:")
print("Event ID:", event.event_id)
print("Type:", event.type_)
print("Theme:", event.theme)
print("Date:", event.date)
print("Time:", event.time)
print("Duration:", event.duration)
print("employee Name:", event.employee.name)
print("employee ID:", event.employee.id)
print("Department:", event.employee.department)
print("Job Title:", event.employee.job_title)
