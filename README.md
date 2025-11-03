SILENT SPEECH RECOGNITION

This project focuses on recognizing unspoken or silent speech using visual and sensor data. It’s designed to help people with speech impairments communicate using AI-based systems.

💡 Project Overview

This project implements a secure, user-centric smart system interface activated by Face Recognition and controlled by hands-free gestures (Lip Tracking). It's designed for security-sensitive or accessibility-focused environments, allowing users to authenticate their presence and control devices like lights and fans using simple, discrete mouth movements detected via a webcam.
The system workflow is:
1. Authentication: The Python script (face.py) uses a webcam to verify the user's identity.
2. Access: Upon successful match, it automatically opens the main web interface (index.html).
3. Control: The web interface (lightfan.html) uses a live camera feed and JavaScript to translate specific mouth movements (e.g., opening and closing the mouth) into commands for home devices.

✨ Key Features

* Face Recognition Security (face.py): Uses the face_recognition library to compare live webcam feed against a known image, acting as the primary access gate.
* Hands-Free Device Control (lightfan.html): Implements Lip Tracking using MediaPipe Face Mesh to detect specific gestures (like the distance between the upper and lower lip) to toggle the light and fan status.
    * Example: One mouth open/close gesture toggles the Light; three rapid gestures toggle the Fan.
* Centralized Navigation (index.html): A landing page that provides a simple navigation structure to various smart system functionalities (Home Automation, Communication, Emergency Alert).
* Emergency Alerts (emergency-alert.html): A dedicated interface for quickly sending alerts to predefined contacts or emergency services.
* 3D Visual Integration (animation.blend): Includes a Blender file, suggesting plans for 3D modeling and visualization of the smart home environment or device controls.


💻 Tech Stack

Category	Technology/Library	Files Used	Purpose
Authentication	Python, OpenCV	face.py	Biometric login using face encoding comparison.
Hands-Free Control	MediaPipe, TensorFlow.js	lightfan.html	Real-time lip landmark tracking for gesture recognition.
User Interface	HTML5, CSS, JavaScript	*.html	Front-end interface for navigation and control feedback.
Data Logging	CSV	emg_data.csv	Placeholder/Log for potential Electromyography (EMG) or gesture data acquisition.
Modeling	Blender	animation.blend	3D assets for potential visualization or simulation.

⚙️ Setup and Installation Guide

To run this system, you need to set up the Python environment for face recognition and run the web files locally.

1. Python Setup (For Authentication)

# You likely need to install these key libraries
pip install opencv-python dlib face-recognition webbrowser

2. Configure face.py

You must update the KNOWN_FACE_PATH variable in face.py to point to the image of the authorized user.

# In face.py, update this line:
KNOWN_FACE_PATH = "/path/to/your/authorized_user_image.jpg"

3. Run the Authentication Script

Execute the Python file. This will open your webcam.

python face.py
* If the recognized face matches the known image, the script will print a success message and automatically open index.html in your default browser.
* If no match is found, the webcam stream will continue until a match is detected or the script is manually closed.

4. Web Interface (Hands-Free Control)

The web components (lightfan.html, emergency-alert.html) are pure HTML/JavaScript and are designed to run directly in a modern web browser, using the built-in webcam access provided by JavaScript's MediaPipe library. Once authenticated via face.py, the system is ready for hands-free interaction.
