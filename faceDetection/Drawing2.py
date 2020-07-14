import cv2
import numpy as np

width = 800
height = 600
rectColor = (0, 200, 0)
circleColor = (0, 0, 200)
polyColor = (200, 0, 0)
canvas = np.zeros((height, width, 3))

# To draw a circle, we need to know its center point and its radius
cv2.circle(canvas, (400, 300), 150, circleColor, thickness=3)

# To draw a rectangle, we need to know its top left and bottom right corner
cv2.rectangle(canvas, (400 - 100, 300 - 100), (400 + 100, 300 + 100), rectColor, thickness=3)

# To draw a polygon, we need to define it's vertices manually
# and store them in an array of dimensions VERTEX_NUM X 1 X 2

# If multidimensional array notation confuses you, just try and read
# it linearly, for example an array of size 4x3x2 is an array of
# 4 elements of which every element contains 3 elements of which
# every element contains 2 elements.

polyVertices = np.array([[400, 300 - 100], [400 - 100, 300], [400, 300 + 100], [400 + 100, 300]], np.int32)
# The -1 in the reshape method is a placeholder for a dimension that can
# be deduced from context. Only one parameter of this type can be used at a time
polyVertices = polyVertices.reshape((-1, 1, 2))
cv2.polylines(canvas, [polyVertices], True, polyColor, thickness=3)

cv2.imshow("Drawing", canvas)
cv2.waitKey(0)
