import cv2
from util import get_limits

webcam = cv2.VideoCapture(0)
color = [0, 255, 255] # Yellow in BGR

while True:
    ret, frame = webcam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = get_limits(color)
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    cv2.imshow('frame', mask)

    # Check if the kqy 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()