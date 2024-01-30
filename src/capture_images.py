import cv2
import tkinter as tk
from tkinter import ttk
from align_faces import AlignFacesApp

class CaptureImagesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Capture Images")

        self.directions = ["look straight", "look left", "look right", "look up", "look down"]
        self.current_direction = tk.StringVar()
        self.progress_var = tk.DoubleVar()

        self.label = ttk.Label(self.root, textvariable=self.current_direction, font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, length=300, mode="determinate")
        self.progress_bar.pack(pady=20)

        self.capture_button = ttk.Button(self.root, text="Capture Image", command=self.capture_image)
        self.capture_button.pack(pady=20)

        self.index = 0
        self.capture_image()

    def capture_image(self):
        if self.index < len(self.directions):
            self.current_direction.set(f"Please {self.directions[self.index]} into the camera...")
            self.progress_var.set(0)
            self.capture_button.configure(state="disabled")
            self.root.after(100, self.update_progress)
        else:
            self.root.destroy()
            AlignFacesApp.align_faces()

    def update_progress(self):
        current_value = self.progress_var.get()
        if current_value < 100:
            self.progress_var.set(current_value + 1)
            self.root.after(10, self.update_progress)
        else:
            self.index += 1
            self.capture_button.configure(state="normal")
            self.capture_button.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptureImagesApp(root)
    root.mainloop()
