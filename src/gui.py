import face_recognition
import cv2
import pickle
import tkinter as tk
from tkinter import ttk

class RecognizeFacesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recognize Faces")

        self.label = ttk.Label(self.root, text="Recognizing Faces...", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Update the video capture to use DroidCam URL
        self.video_capture = cv2.VideoCapture('http://127.0.0.1:4747/video')

        self.face_names = []

        self.root.after(100, self.update_frame)

    def update_frame(self):
        _, frame = self.video_capture.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.6)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX

            if name != "Unknown":
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.video_capture.release()
            cv2.destroyAllWindows()
            self.root.destroy()
        else:
            self.root.after(10, self.update_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecognizeFacesApp(root)
    root.mainloop()
