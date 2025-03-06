import numpy as np
import cv2

def get_limits(color):

    # 1x1 NumPy arr with given color(BGR)
    c = np.uint8([[color]])

    # Convert the input color to HSV
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) # hsv = Hue, Saturation, Value
    hue = hsv[0][0][0]

    # Sets the range for hue (intensity) to isolate certain colors.
    # Then, convert both limits back to NumPy array
    lower_limit = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upper_limit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lower_limit, upper_limit