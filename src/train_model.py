import face_recognition
import os
import pickle

def train_model():
    known_face_encodings = []
    known_face_names = []

    images_dir = "../data/captured_images/"

    for image_file in os.listdir(images_dir):
        image_path = os.path.join(images_dir, image_file)
        face_image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(face_image)

        if face_encodings:
            encoding = face_encodings[0]
            known_face_encodings.append(encoding)
            known_face_names.append(image_file.split('_')[1].split('.')[0])

    with open("../models/trained_model.pkl", "wb") as file:
        data = {"encodings": known_face_encodings, "names": known_face_names}
        pickle.dump(data, file)

if __name__ == "__main__":
    train_model()
