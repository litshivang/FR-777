from align_faces import AlignFacesApp
from train_model import train_model
from gui import RecognizeFacesApp
import tkinter as tk
from capture_images import CaptureImagesApp

def main():
    # Step 1: Capture Images    
    root = tk.Tk()
    capture_images_app = CaptureImagesApp(root)
    root.mainloop()

    # Step 2: Align Faces
    root = tk.Tk()
    align_faces_app = AlignFacesApp(root)
    root.mainloop()

    # Step 3: Train Face Recognition Model
    train_model()

    # Step 4: Recognize Faces (Test)
    root = tk.Tk()
    recognize_faces_app = RecognizeFacesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
