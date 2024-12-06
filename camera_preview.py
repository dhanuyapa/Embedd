import cv2  # Import OpenCV library
import time  # Import time for delays

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Show the camera feed for 10 seconds
print("Press 'q' to quit.")
start_time = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Display the frame in a window
    cv2.imshow("Camera Feed", frame)

    # Exit when 'q' is pressed or after 10 seconds
    if cv2.waitKey(1) & 0xFF == ord('q') or (time.time() - start_time) > 10:
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
