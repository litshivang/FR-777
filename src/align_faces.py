import face_recognition
import cv2
import tkinter as tk
from tkinter import ttk
from train_model import train_model

class AlignFacesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Align Faces")

        self.label = ttk.Label(self.root, text="Aligning Faces...", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, length=300, mode="determinate")
        self.progress_bar.pack(pady=20)

        self.align_faces()

    @classmethod
    def align_faces(cls):
        cls.progress_var.set(0)
        cls.root.after(100, cls.update_progress)

    @classmethod
    def update_progress(cls):
        current_value = cls.progress_var.get()
        if current_value < 100:
            cls.progress_var.set(current_value + 1)
            cls.root.after(10, cls.update_progress)
        else:
            cls.root.destroy()
            train_model()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlignFacesApp(root)
    root.mainloop()
