😄 Smile Detection with OpenCV
A simple Python program that uses Haar Cascade classifiers to detect smiles from a webcam feed and automatically captures a photo when a smile is detected.

📦 Features
-Face detection using Haar cascades
-Smile detection within detected face regions
-Automatically clicks and saves an image when a smile is detected
-Saves the image as smile_detected.jpg 
-Displays the captured image with the detected smile
-Exits automatically after capturing a smile or when you press q

🛠 Requirements
-Python 3.x
-OpenCV (cv2)

Install OpenCV using pip:
-pip install opencv-python


Allow camera access when prompted.

Smile! 😄 The program will detect your smile, capture the image, and save it as smile_detected.jpg.

🎮 Controls & Behavior
Action	- Trigger
Start detection-	Run the script
Smile-	Automatically clicks and saves the photo of your smile
Exit- manually	Press q
Auto-exit-	After one smile is captured

📝 Notes
The Haar Cascade files are bundled with OpenCV and loaded via cv2.data.haarcascades.

Only one smile image is captured per session to avoid repeated saves.

The image is saved as smile_detected.jpg and displayed in the program.

Works best in well-lit environments and with the face clearly visible.
