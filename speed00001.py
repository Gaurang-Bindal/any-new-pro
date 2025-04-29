import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import random
import cv2
import os
import csv
import matplotlib.pyplot as plt
import logging

# --- Configuration ---
SENSOR_DISTANCE_METERS = 0.55
SPEED_LIMIT_KMPH = 50
IMAGE_DIR = "speeding_images"
LOG_FILE = "speed_log.csv"

# Ensure directories exist
os.makedirs(IMAGE_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SpeedBreakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Speed Breaker Monitor")
        self.running = False

        # UI Elements
        self.start_button = tk.Button(root, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=10)

        self.visualize_button = tk.Button(root, text="Visualize Data", command=self.visualize_data)
        self.visualize_button.pack(pady=5)

        self.status_label = tk.Label(root, text="Status: Idle", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.tree = ttk.Treeview(root, columns=("Time", "Speed", "Status", "Image"), show="headings")
        for col in ("Time", "Speed", "Status", "Image"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.cap = None

        # Initialize CSV
        self.init_log_file()

    def init_log_file(self):
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Speed_kmph", "Alert"])

    def start_monitoring(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.monitor_loop, daemon=True).start()
            self.status_label.config(text="Status: Monitoring...")
            if self.cap is None:
                self.cap = cv2.VideoCapture(0)
                if not self.cap.isOpened():
                    messagebox.showerror("Camera Error", "Unable to access the webcam.")
                    self.running = False

    def simulate_vehicle(self):
        time.sleep(random.uniform(1, 3))
        t1 = time.time()
        time.sleep(random.uniform(0.5, 1.5))
        t2 = time.time()
        speed = SENSOR_DISTANCE_METERS / (t2 - t1) * 3.6
        return round(speed, 2), time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

    def capture_image(self, filename):
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                path = os.path.join(IMAGE_DIR, filename)
                cv2.imwrite(path, frame)
                logging.info(f"Image captured: {path}")

    def log_data(self, timestamp, speed, alert):
        with open(LOG_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, speed, alert])

    def monitor_loop(self):
        while self.running:
            speed, timestamp = self.simulate_vehicle()
            alert = speed > SPEED_LIMIT_KMPH
            status = "⚠️ Hit" if alert else "Safe"
            image_file = ""

            if alert:
                image_file = f"speed_{timestamp}.jpg"
                self.capture_image(image_file)

            self.tree.insert("", "end", values=(timestamp, speed, status, image_file))
            self.status_label.config(text=f"Latest: {speed} km/h - {status}")
            self.log_data(timestamp, speed, alert)

            logging.info(f"Speed recorded: {speed} km/h, Alert: {alert}")

    def visualize_data(self):
        try:
            timestamps = []
            speeds = []
            with open(LOG_FILE, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                for row in reader:
                    timestamps.append(row[0])
                    speeds.append(float(row[1]))

            if not speeds:
                messagebox.showinfo("No Data", "No speed data to visualize.")
                return

            plt.figure(figsize=(10, 5))
            plt.plot(speeds, marker='o')
            plt.axhline(SPEED_LIMIT_KMPH, color='r', linestyle='--', label='Speed Limit')
            plt.title("Vehicle Speeds Over Time")
            plt.ylabel("Speed (km/h)")
            plt.xlabel("Event #")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            logging.error(f"Error visualizing data: {e}")
            messagebox.showerror("Error", "Failed to visualize data.")

    def close(self):
        self.running = False
        if self.cap and self.cap.isOpened():
            self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedBreakerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
