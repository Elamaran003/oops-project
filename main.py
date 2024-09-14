import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from datetime import datetime

# Define Event class
class Event:
    def __init__(self, name, date, venue, max_participants, category="General"):
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.venue = venue
        self.max_participants = max_participants
        self.category = category
        self.participants = []

    def add_participant(self, participant_name):
        if len(self.participants) < self.max_participants:
            self.participants.append(participant_name)
        else:
            raise ValueError("Max participants reached.")

    def get_event_details(self):
        return f"Name: {self.name}\nDate: {self.date.strftime('%Y-%m-%d')}\nVenue: {self.venue}\nCategory: {self.category}\nMax Participants: {self.max_participants}\nCurrent Participants: {len(self.participants)}"

    def get_participants(self):
        return self.participants

# Define EventManagementSystem class
class EventManagementSystem:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event_name):
        event = self.search_event(event_name)
        if event:
            self.events.remove(event)
        else:
            raise ValueError("Event not found.")

    def search_event(self, event_name):
        for event in self.events:
            if event.name.lower() == event_name.lower():
                return event
        return None

    def get_event_names(self):
        return [event.name for event in self.events]

    def most_popular_event(self):
        if not self.events:
            return None
        return max(self.events, key=lambda e: len(e.participants))

# Define EventApp class with enhanced GUI
class EventApp(tk.Tk):
    def __init__(self, event_system):
        super().__init__()
        self.event_system = event_system
        self.title("Event Management System")
        self.geometry("800x600")
        self.configure(bg="#e0f7fa")

        # Custom Fonts
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.button_font = tkfont.Font(family="Helvetica", size=12)

        self.create_widgets()

    def create_widgets(self):
        # Title Frame
        title_frame = tk.Frame(self, bg="#00796b")
        title_frame.pack(fill="x")
        tk.Label(title_frame, text="Event Management System", font=self.title_font, bg="#00796b", fg="#ffffff").pack(pady=20)

        # Main Frame
        main_frame = tk.Frame(self, bg="#e0f7fa")
        main_frame.pack(pady=20)

        # Buttons with Hover Effect
        self.create_button(main_frame, "Add Event", self.add_event)
        self.create_button(main_frame, "View Events", self.view_events)
        self.create_button(main_frame, "Search Event", self.search_event)
        self.create_button(main_frame, "Delete Event", self.delete_event)
        self.create_button(main_frame, "Event Statistics", self.view_statistics)
        self.create_button(main_frame, "Update Event", self.update_event)
        self.create_button(main_frame, "Search Events by Date Range", self.search_events_by_date_range)
        self.create_button(main_frame, "View Participants", self.view_participants)
        self.create_button(main_frame, "Check Venue Capacity", self.check_venue_capacity)
        self.create_button(main_frame, "Submit Feedback", self.submit_feedback)
        self.create_button(main_frame, "Filter Events by Category", self.filter_events_by_category)
        self.create_button(main_frame, "Most Popular Event", self.most_popular_event)

        # Exit Button at the Bottom
        exit_button = tk.Button(self, text="Exit", font=self.button_font, command=self.exit_to_homepage, bg="#d32f2f", fg="#ffffff")
        exit_button.pack(pady=20)
        exit_button.bind("<Enter>", lambda e: exit_button.config(bg="#b71c1c"))
        exit_button.bind("<Leave>", lambda e: exit_button.config(bg="#d32f2f"))

    def create_button(self, parent, text, command):
        button = tk.Button(parent, text=text, font=self.button_font, command=command, bg="#00796b", fg="#ffffff")
        button.pack(pady=5, fill="x")
        button.bind("<Enter>", lambda e: button.config(bg="#004d40"))
        button.bind("<Leave>", lambda e: button.config(bg="#00796b"))

    def add_event(self):
        AddEventWindow(self, self.event_system)

    def view_events(self):
        ViewEventsWindow(self, self.event_system.get_event_names())

    def search_event(self):
        SearchEventWindow(self, self.event_system)

    def delete_event(self):
        DeleteEventWindow(self, self.event_system)

    def view_statistics(self):
        statistics = f"Total Events: {len(self.event_system.events)}\nMost Popular Event: {self.event_system.most_popular_event().name if self.event_system.most_popular_event() else 'None'}"
        messagebox.showinfo("Event Statistics", statistics)

    def update_event(self):
        UpdateEventWindow(self, self.event_system)

    def search_events_by_date_range(self):
        SearchEventsByDateRangeWindow(self, self.event_system)

    def view_participants(self):
        ViewParticipantsWindow(self, self.event_system)

    def check_venue_capacity(self):
        CheckVenueCapacityWindow(self, self.event_system)

    def submit_feedback(self):
        SubmitFeedbackWindow(self, self.event_system)

    def filter_events_by_category(self):
        FilterEventsByCategoryWindow(self, self.event_system)

    def most_popular_event(self):
        most_popular_event = self.event_system.most_popular_event()
        if most_popular_event:
            messagebox.showinfo("Most Popular Event", most_popular_event.get_event_details())
        else:
            messagebox.showwarning("No Events", "There are no events available.")

    def exit_to_homepage(self):
        self.destroy()
        Homepage().mainloop()

# Define additional windows (AddEventWindow, ViewEventsWindow, etc.)
class AddEventWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("Add Event")
        self.geometry("400x300")
        self.configure(bg="#fff3e0")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Event Name:", bg="#fff3e0").pack(pady=5)
        self.event_name_entry = tk.Entry(self)
        self.event_name_entry.pack(pady=5)

        tk.Label(self, text="Event Date (YYYY-MM-DD):", bg="#fff3e0").pack(pady=5)
        self.event_date_entry = tk.Entry(self)
        self.event_date_entry.pack(pady=5)

        tk.Label(self, text="Venue:", bg="#fff3e0").pack(pady=5)
        self.venue_entry = tk.Entry(self)
        self.venue_entry.pack(pady=5)

        tk.Label(self, text="Max Participants:", bg="#fff3e0").pack(pady=5)
        self.max_participants_entry = tk.Entry(self)
        self.max_participants_entry.pack(pady=5)

        tk.Label(self, text="Category:", bg="#fff3e0").pack(pady=5)
        self.category_entry = tk.Entry(self)
        self.category_entry.pack(pady=5)

        tk.Button(self, text="Add Event", command=self.add_event).pack(pady=20)

    def add_event(self):
        event_name = self.event_name_entry.get()
        event_date = self.event_date_entry.get()
        venue = self.venue_entry.get()
        max_participants = int(self.max_participants_entry.get())
        category = self.category_entry.get() or "General"

        event = Event(event_name, event_date, venue, max_participants, category)
        self.event_system.add_event(event)
        messagebox.showinfo("Success", "Event added successfully!")
        self.destroy()

class ViewEventsWindow(tk.Toplevel):
    def __init__(self, parent, events):
        super().__init__(parent)
        self.title("Event List")
        self.geometry("600x400")
        self.configure(bg="#e0f2f1")
        self.create_widgets(events)

    def create_widgets(self, events):
        tk.Label(self, text="Events List", font=("Helvetica", 16), bg="#e0f2f1").pack(pady=10)
        event_list = "\n".join(events)
        tk.Label(self, text=event_list, bg="#e0f2f1").pack(pady=10)

class SearchEventWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("Search Event")
        self.geometry("400x200")
        self.configure(bg="#e8f5e9")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter Event Name:", bg="#e8f5e9").pack(pady=5)
        self.search_entry = tk.Entry(self)
        self.search_entry.pack(pady=5)

        tk.Button(self, text="Search", command=self.search_event).pack(pady=20)

    def search_event(self):
        event_name = self.search_entry.get()
        event = self.event_system.search_event(event_name)
        if event:
            messagebox.showinfo("Event Found", event.get_event_details())
        else:
            messagebox.showwarning("Event Not Found", "No event found with that name.")

class DeleteEventWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("Delete Event")
        self.geometry("400x200")
        self.configure(bg="#fff3e0")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter Event Name to Delete:", bg="#fff3e0").pack(pady=5)
        self.delete_entry = tk.Entry(self)
        self.delete_entry.pack(pady=5)

        tk.Button(self, text="Delete Event", command=self.delete_event).pack(pady=20)

    def delete_event(self):
        event_name = self.delete_entry.get()
        try:
            self.event_system.remove_event(event_name)
            messagebox.showinfo("Success", "Event deleted successfully!")
        except ValueError:
            messagebox.showwarning("Error", "Event not found.")
        self.destroy()

class UpdateEventWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("Update Event")
        self.geometry("400x300")
        self.configure(bg="#e0f2f1")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter Event Name to Update:", bg="#e0f2f1").pack(pady=5)
        self.event_name_entry = tk.Entry(self)
        self.event_name_entry.pack(pady=5)

        tk.Label(self, text="New Date (YYYY-MM-DD):", bg="#e0f2f1").pack(pady=5)
        self.new_date_entry = tk.Entry(self)
        self.new_date_entry.pack(pady=5)

        tk.Label(self, text="New Venue:", bg="#e0f2f1").pack(pady=5)
        self.new_venue_entry = tk.Entry(self)
        self.new_venue_entry.pack(pady=5)

        tk.Label(self, text="New Max Participants:", bg="#e0f2f1").pack(pady=5)
        self.new_max_participants_entry = tk.Entry(self)
        self.new_max_participants_entry.pack(pady=5)

        tk.Label(self, text="New Category:", bg="#e0f2f1").pack(pady=5)
        self.new_category_entry = tk.Entry(self)
        self.new_category_entry.pack(pady=5)

        tk.Button(self, text="Update Event", command=self.update_event).pack(pady=20)

    def update_event(self):
        event_name = self.event_name_entry.get()
        new_date = self.new_date_entry.get()
        new_venue = self.new_venue_entry.get()
        new_max_participants = int(self.new_max_participants_entry.get())
        new_category = self.new_category_entry.get() or "General"

        event = self.event_system.search_event(event_name)
        if event:
            event.date = datetime.strptime(new_date, "%Y-%m-%d")
            event.venue = new_venue
            event.max_participants = new_max_participants
            event.category = new_category
            messagebox.showinfo("Success", "Event updated successfully!")
        else:
            messagebox.showwarning("Error", "Event not found.")
        self.destroy()

class SearchEventsByDateRangeWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("Search Events by Date Range")
        self.geometry("400x300")
        self.configure(bg="#e8f5e9")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Start Date (YYYY-MM-DD):", bg="#e8f5e9").pack(pady=5)
        self.start_date_entry = tk.Entry(self)
        self.start_date_entry.pack(pady=5)

        tk.Label(self, text="End Date (YYYY-MM-DD):", bg="#e8f5e9").pack(pady=5)
        self.end_date_entry = tk.Entry(self)
        self.end_date_entry.pack(pady=5)

        tk.Button(self, text="Search", command=self.search_events_by_date_range).pack(pady=20)

    def search_events_by_date_range(self):
        start_date_str = self.start_date_entry.get()
        end_date_str = self.end_date_entry.get()
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

        events = [event for event in self.event_system.events if start_date <= event.date <= end_date]
        if events:
            event_details = "\n\n".join(event.get_event_details() for event in events)
            messagebox.showinfo("Events", event_details)
        else:
            messagebox.showwarning("No Events", "No events found in the given date range.")
        self.destroy()

class ViewParticipantsWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("View Participants")
        self.geometry("400x300")
        self.configure(bg="#e0f2f1")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter Event Name:", bg="#e0f2f1").pack(pady=5)
        self.event_name_entry = tk.Entry(self)
        self.event_name_entry.pack(pady=5)

        tk.Button(self, text="View Participants", command=self.view_participants).pack(pady=20)

    def view_participants(self):
        event_name = self.event_name_entry.get()
        event = self.event_system.search_event(event_name)
        if event:
            participants = "\n".join(event.get_participants())
            messagebox.showinfo("Participants", participants if participants else "No participants yet.")
        else:
            messagebox.showwarning("Event Not Found", "No event found with that name.")
        self.destroy()

class CheckVenueCapacityWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("Check Venue Capacity")
        self.geometry("400x200")
        self.configure(bg="#e0f2f1")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter Event Name:", bg="#e0f2f1").pack(pady=5)
        self.event_name_entry = tk.Entry(self)
        self.event_name_entry.pack(pady=5)

        tk.Button(self, text="Check Capacity", command=self.check_capacity).pack(pady=20)

    def check_capacity(self):
        event_name = self.event_name_entry.get()
        event = self.event_system.search_event(event_name)
        if event:
            capacity = f"Venue: {event.venue}\nMax Participants: {event.max_participants}\nCurrent Participants: {len(event.get_participants())}"
            messagebox.showinfo("Venue Capacity", capacity)
        else:
            messagebox.showwarning("Event Not Found", "No event found with that name.")
        self.destroy()

class SubmitFeedbackWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("Submit Feedback")
        self.geometry("400x300")
        self.configure(bg="#fce4ec")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter Event Name:", bg="#fce4ec").pack(pady=5)
        self.event_name_entry = tk.Entry(self)
        self.event_name_entry.pack(pady=5)

        tk.Label(self, text="Your Feedback:", bg="#fce4ec").pack(pady=5)
        self.feedback_text = tk.Text(self, height=5)
        self.feedback_text.pack(pady=5)

        tk.Button(self, text="Submit Feedback", command=self.submit_feedback).pack(pady=20)

    def submit_feedback(self):
        event_name = self.event_name_entry.get()
        feedback = self.feedback_text.get("1.0", tk.END).strip()

        # Simulate feedback submission
        if feedback:
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        else:
            messagebox.showwarning("No Feedback", "Please provide some feedback.")
        self.destroy()

class FilterEventsByCategoryWindow(tk.Toplevel):
    def __init__(self, parent, event_system):
        super().__init__(parent)
        self.event_system = event_system
        self.title("Filter Events by Category")
        self.geometry("400x200")
        self.configure(bg="#e0f7fa")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter Category:", bg="#e0f7fa").pack(pady=5)
        self.category_entry = tk.Entry(self)
        self.category_entry.pack(pady=5)

        tk.Button(self, text="Filter", command=self.filter_events).pack(pady=20)

    def filter_events(self):
        category = self.category_entry.get()
        filtered_events = [event for event in self.event_system.events if event.category.lower() == category.lower()]
        if filtered_events:
            event_details = "\n\n".join(event.get_event_details() for event in filtered_events)
            messagebox.showinfo("Filtered Events", event_details)
        else:
            messagebox.showwarning("No Events", "No events found for the given category.")
        self.destroy()

class Homepage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Homepage")
        self.geometry("400x200")
        self.configure(bg="#e0f2f1")
        tk.Label(self, text="Welcome to the Event Management System", font=("Helvetica", 16), bg="#e0f2f1").pack(pady=50)

# Run the application
if __name__ == "__main__":
    event_system = EventManagementSystem()
    app = EventApp(event_system)
    app.mainloop()
