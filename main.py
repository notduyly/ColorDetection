import cv2
from util import get_limits

webcam = cv2.VideoCapture(0)
color = [0, 255, 255] # Yellow in BGR

while True:
    # Capture the frame at that moment
    ret, frame = webcam.read()

    # Converts the frame BGR -> HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the upper/lower limit of 
    lower_limit, upper_limit = get_limits(color)

    # Check each pixel in hsv frame and sets that pixel to
    # white (255) if it's within the range else black (0)
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    cv2.imshow('frame', mask)

    # Check if the key 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()