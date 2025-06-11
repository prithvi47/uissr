import cv2
import face_recognition
import os
import time
import webbrowser
import subprocess
from datetime import datetime

# Path to known face image
KNOWN_FACE_PATH = "meter.jpg" # Change this to the correct path

# Load the known face image and encode it
known_image = face_recognition.load_image_file(KNOWN_FACE_PATH)
known_encoding = face_recognition.face_encodings(known_image)[0]

# Extract name from filename
name = os.path.splitext(os.path.basename(KNOWN_FACE_PATH))[0]

# Open webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break  # Exit if no frame is captured

    # Resize frame for faster processing (reduces lag)
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and encode them
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    current_time = datetime.now().strftime("%H:%M:%S")
    match_found = False

    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        # Compare face with the known encoding
        matches = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.5)

        if matches[0]:  # Face matches
            match_found = True
            label = name
            color = (0, 255, 0)  # Green for known user
        else:
            label = "Unknown User"
            color = (0, 0, 255)  # Red for unknown user

        # Adjust coordinates after resizing
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        # Draw rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), color, 3)

        # Label background
        cv2.rectangle(frame, (left, top - 40), (right, top), color, -1)

        # Display label
        cv2.putText(frame, label, (left + 5, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Display time
        cv2.rectangle(frame, (left, bottom), (left + 100, bottom + 30), color, -1)
        cv2.putText(frame, current_time, (left + 5, bottom + 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    cv2.imshow("Face Recognition", frame)

    # If a match is found, open index.html and break
    if match_found:
        print("✅ Face Matched! Opening index.html...")
        html_path = "file://" + os.path.abspath("/Users/prithviraj/Documents/UISSR/index.html")

        try:
            webbrowser.open(html_path)  # Try to open with webbrowser module
            webbrowser.get().open(html_path)  # Ensure it uses the default browser
        except:
            print("⚠️ Webbrowser module failed, trying subprocess...")
            subprocess.run(["open", os.path.abspath("/Users/prithviraj/Documents/UISSR/index.html")])  # macOS

        time.sleep(3)  # Wait to prevent multiple openings
        break

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
