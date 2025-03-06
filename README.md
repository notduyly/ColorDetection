# Color Detection Project

This project demonstrates a simple approach to color detection using OpenCV and NumPy. It captures live video from your webcam, converts the video frames to the HSV color space, 
and applies a mask to detect a specific color.

- **main.py:**  
  - Captures webcam video.
  - Converts each frame from BGR to HSV.
  - Uses `get_limits` from `util.py` to define color thresholds.
  - Applies a mask to detect the specified color.
  - Draw a bounding box around the detected color.
  - Displays the bounding box until the 'q' key is pressed.

- **util.py:**  
  - Converts the detected color from BGR into HSV.
  - Calculates lower and upper HSV limits around the target hue.
  - Returns these limits as NumPy arrays, which are then used in `main.py`.

## Prerequisites

- [OpenCV](https://opencv.org/) (`opencv-python`)
- [NumPy](https://numpy.org/)
- [Pillow](https://pypi.org/project/pillow/)


You can install the required packages via pip:

```bash
pip install -r requirements.txt
