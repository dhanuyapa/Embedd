import cv2  # Import OpenCV

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture a single frame
ret, frame = cap.read()
if ret:
    # Save the captured image to a file
    cv2.imwrite('captured_image.jpg', frame)
    print("Image captured and saved as captured_image.jpg")
else:
    print("Failed to capture image.")

# Release the webcam
cap.release()
cv2.destroyAllWindows()
