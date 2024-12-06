import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound  # Use `os` module for non-Windows systems

class HealthReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Reminder")
        self.running_eye = False
        self.running_water = False
        
        self.label = tk.Label(root, text="Health Reminder App", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_reminders, bg="green", fg="white")
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_reminders, bg="red", fg="white", state="disabled")
        self.stop_button.pack(pady=10)
        
        self.eye_timer_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.eye_timer_label.pack(pady=10)
        
        self.water_timer_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.water_timer_label.pack(pady=10)
        
    def start_reminders(self):
        self.running_eye = True
        self.running_water = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        threading.Thread(target=self.eye_break_timer).start()
        threading.Thread(target=self.water_reminder_timer).start()

    def stop_reminders(self):
        self.running_eye = False
        self.running_water = False
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"
        self.eye_timer_label.config(text="")
        self.water_timer_label.config(text="")

    def eye_break_timer(self):
        while self.running_eye:
            time.sleep(10 * 60)  # Wait for 10 minutes
            if not self.running_eye:
                break
            self.show_reminder("Eye Break Reminder", "Time to take a 20-second break!")
            self.countdown(20, self.eye_timer_label)
            if self.running_eye:
                self.beep()

    def water_reminder_timer(self):
        while self.running_water:
            time.sleep(30 * 60)  # Wait for 30 minutes
            if not self.running_water:
                break
            self.show_reminder("Water Reminder", "Time to drink some water!")
            if self.running_water:
                self.beep()

    def show_reminder(self, title, message):
        messagebox.showinfo(title, message)

    def countdown(self, seconds, label):
        for i in range(seconds, 0, -1):
            if not self.running_eye:
                break
            label.config(text=f"Time left: {i} seconds")
            time.sleep(1)
        label.config(text="")

    def beep(self):
        for _ in range(3):
            winsound.Beep(1000, 200)

# Run the app
root = tk.Tk()
app = HealthReminderApp(root)
root.mainloop()

