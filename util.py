import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([[color]])

    # Convert the input color to grayscale
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY) # hsv = Hue, Saturation, Value

    # Sets the range for hue (intensity) to isolate certain colors
    lower_limit = hsvC[0][0][0] - 10, 100, 100
    upper_limit = hsvC[0][0][0] + 10, 255, 255
    
    # Convert both limits back to NumPy array
    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return lower_limit, upper_limit