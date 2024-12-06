import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound  # Use `os` module for non-Windows systems
#import os  # Use `os` module for non-Windows systems


class EyeBreakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eye Break Reminder")
        self.running = False
        
        self.label = tk.Label(root, text="Eye Break Reminder", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, bg="green", fg="white")
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, bg="red", fg="white", state="disabled")
        self.stop_button.pack(pady=10)
        
        self.timer_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.timer_label.pack(pady=20)
        
    def start_timer(self):
        self.running = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        self.run_timer()

    def stop_timer(self):
        self.running = False
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"
        self.timer_label.config(text="")

    def run_timer(self):
        if self.running:
            # Start a new thread for 10-minute countdown
            threading.Thread(target=self.break_reminder).start()
    
    def break_reminder(self):
        while self.running:
            time.sleep(1 * 60)  # Wait for 10 minutes
            if not self.running:
                break
            # Show reminder
            self.show_reminder()
            # 20-second countdown
            self.countdown(20)
            # Beep at the end
            if self.running:
                self.beep()

    def show_reminder(self):
        messagebox.showinfo("Eye Break Reminder", "Time to take a 20-second break!")

    def countdown(self, seconds):
        for i in range(seconds, 0, -1):
            if not self.running:
                break
            self.timer_label.config(text=f"Time left: {i} seconds")
            time.sleep(1)
        self.timer_label.config(text="")

    def beep(self):
        # Beep sound (Windows-specific, replace with `os.system` for Linux/Mac)
        for _ in range(3):
            winsound.Beep(1000, 200)

# Run the app
root = tk.Tk()
app = EyeBreakApp(root)
root.mainloop()

