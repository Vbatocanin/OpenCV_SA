import cv2
import numpy as np

# Window and drawing parameters
width = 800
height = 600
drawColor = (0, 200, 0)

# We're making a canvas that represents an 800x600 pixel image
# Each pixel in this image is represented by 3 values, in this order:
# Blue, Green, Red. Each of these values is a positive integer from 0 to 255
# that represents how prominent its corresponding color is in that very pixel.
# So, if we set the BGR values for all the pixels to (0,0,0), that means that
# it's devoid of all color, in other words, it's black
triangleVertices = [(400, 100), (200, 500), (600, 500)]
canvas = np.zeros((height, width, 3))

# Drawing the green triangle with 3 lines
cv2.line(canvas, triangleVertices[0], triangleVertices[1], drawColor, thickness=3)
cv2.line(canvas, triangleVertices[1], triangleVertices[2], drawColor, thickness=3)
cv2.line(canvas, triangleVertices[0], triangleVertices[2], drawColor, thickness=3)

cv2.imshow("Drawing", canvas)
cv2.waitKey(0)
