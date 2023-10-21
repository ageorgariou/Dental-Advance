import cv2
import time
from simple_facerec import SimpleFacerec
from database_handler import setup_database, get_client_info
from messaging_system import send1_email  # Import the send1_email function

sfr = SimpleFacerec()

# Initialize the database (create it if it doesn't exist)
setup_database()

# Camera
cap = cv2.VideoCapture(0)

# Encoding faces
sfr.load_encoding_images("images/")

# Dictionary to keep track of email sent time for each face
email_sent_time = {}

def on_face_detected(client_name):  # Change the parameter to client_name
    current_time = time.time()

    # Check if we've sent an email for this face in the last 30 seconds
    if client_name in email_sent_time and (current_time - email_sent_time[client_name]) < 30:
        return

    client_info = get_client_info(client_name)
    if client_info:
        subject = f"Face Detected: {client_info['name']}"
        body = f"{client_info['name']} detected! Owe Amount: ${client_info['owe_amount']}. Last Activity: {client_info['last_activity']}. Booked for: {client_info['booked_activity']}."

        # Call the send1_email function with the client's name as a string
        send1_email(client_name)
        email_sent_time[client_name] = current_time

while True:
    ret, frame = cap.read()

    # Detect faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)  
        on_face_detected(name)  # Call the function when a face is detected

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()