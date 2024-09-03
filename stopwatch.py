import tkinter as tk
from threading import Thread
import time

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        master.title("Stopwatch App")

        # Create timer display
        self.timer_display = tk.Label(master, text="00:00:00", font=("Helvetica", 24))
        self.timer_display.pack()

        # Create start button
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        # Create pause button
        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer, state="disabled")
        self.pause_button.pack()

        # Create reset button
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

        # Initialize timer variables
        self.timer_running = False
        self.seconds = 0
        self.minutes = 0
        self.milliseconds = 0

    def start_timer(self):
        self.timer_running = True
        self.start_button.config(state="disabled")
        self.pause_button.config(state="normal")
        self.thread = Thread(target=self.update_timer)
        self.thread.start()

    def pause_timer(self):
        self.timer_running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")

    def reset_timer(self):
        self.timer_running = False
        self.seconds = 0
        self.minutes = 0
        self.milliseconds = 0
        self.timer_display.config(text="00:00:00")
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")

    def update_timer(self):
        while self.timer_running:
            time.sleep(0.001)
            self.milliseconds += 1
            if self.milliseconds == 1000:
                self.milliseconds = 0
                self.seconds += 1
                if self.seconds == 60:
                    self.seconds = 0
                    self.minutes += 1
            self.timer_display.config(text=f"{self.minutes:02d}:{self.seconds:02d}:{self.milliseconds:03d}")

root = tk.Tk()
my_stopwatch_app = StopwatchApp(root)
root.mainloop()