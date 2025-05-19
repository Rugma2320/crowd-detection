import cv2
import datetime
# Start video capture (0 = default webcam; use a file path for trail camera 
footage)
cap = cv2.VideoCapture(0)
# Initialize first frame
first_frame = None
while True:
 ret, frame = cap.read()
 if not ret:
 break
 # Convert to grayscale and blur it for better accuracy
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 gray = cv2.GaussianBlur(gray, (21, 21), 0)
 # Set first frame as baseline for comparison
 if first_frame is None:
 first_frame = gray
 continue
import cv2
import datetime
# Start video capture (0 = default webcam; use a file path for trail camera 
footage)
cap = cv2.VideoCapture(0)
# Initialize first frame
first_frame = None
while True:
 ret, frame = cap.read()
 if not ret:
 break
 # Convert to grayscale and blur it for better accuracy
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 gray = cv2.GaussianBlur(gray, (21, 21), 0)
 # Set first frame as baseline for comparison
 if first_frame is None:
 first_frame = gray
 continue
 # Compute difference between current frame and first frame
 frame_delta = cv2.absdiff(first_frame, gray)
 thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
 # Dilate to fill in holes, then find contours
 thresh = cv2.dilate(thresh, None, iterations=2)
 contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
cv2.CHAIN_APPROX_SIMPLE)
 motion_detected = False
 for contour in contours:
 if cv2.contourArea(contour) < 1000:
 continue
 motion_detected = True
 (x, y, w, h) = cv2.boundingRect(contour)
 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
 # If motion is detected, save the frame
 if motion_detected:
 timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
 cv2.imwrite(f"wildlife_{timestamp}.jpg", frame)
 print(f"Motion detected! Saved frame at {timestamp}")
 # Display the video stream
 cv2.imshow("Wildlife Monitor", frame)
 # Break loop on 'q' key
 if cv2.waitKey(1) & 0xFF == ord('q'):
 break
# Cleanup
cap.release()
cv2.destroyAllWindows()