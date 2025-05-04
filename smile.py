import cv2

# Load pre-trained Haar Cascade Classifiers for face and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Start the webcam
cap = cv2.VideoCapture(0)

# Flag to check if the smile has been detected already
smile_detected = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Region of interest (ROI) for smile detection
        roi_gray = gray[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        for (sx, sy, sw, sh) in smiles:
            # Draw rectangle around the smile
            cv2.rectangle(frame, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 255, 0), 2)

            # Capture image when a smile is detected
            if not smile_detected:
                smile_detected_image = frame[y:y + h, x:x + w]
                cv2.imwrite("smile_detected.jpg", smile_detected_image)
                print("Smile detected! Image saved.")

                # Display the captured image
                cv2.imshow("Captured Image", smile_detected_image)

                # Set the flag to True so the image is captured only once
                smile_detected = True
                break

    # If a smile has already been detected, stop processing further
    if smile_detected:
        break

    # Display the frame with detected faces and smiles
    cv2.imshow('Smile Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
