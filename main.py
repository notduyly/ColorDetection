import cv2

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    cv2.imshow('app', frame)

    # Check if the kqy 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()