import cv2
import numpy as np

kernel = np.ones(6)
imgRaw = cv2.imread("Resources/sampleImage.jpg")
imgResize = cv2.resize(imgRaw,(800,600))
imgEdges = cv2.Canny(imgResize,120,150)
imgDilate = cv2.dilate(imgEdges, kernel, iterations=3)

cv2.imshow("Edges", imgEdges)
cv2.imshow("Resized",imgDilate)

cv2.waitKey(0)