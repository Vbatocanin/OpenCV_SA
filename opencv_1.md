### OpenCV Through Python - From Zero to Object Detection



#### Introduction

OpenCV (Open Source Computer Vison) is an open source computer vision library. Computer vision is a branch of artificial intelligence that deals with how computers interpret everything that they can see through images/videos or in other words, a plethora of pixels. Nowadays, this kind of tech is essential for any kind of project where a computer needs to interact with the real world, the most well-known example would be self-driving cars. 

In this article, we'll be we'll learn how to detect, through the following topics:

%%%



#### Setting up OpenCV

The only prerequisite for installing OpenCV is `pip`. After you've installed `pip`, OpenCV can be set up with the following commands:

```bash
# The core package
pip install opencv-python

# The core package + contrib modules
pip install opencv-contrib-python

# NumPy as well as Matplotlib are not manditory, but very useful
pip install numpy && pip install matplotlib
```

Also note that because OpenCV is an  open source project, you can always build it yourself and directly integrate your code into their codebase. A more detailed explanation on how to do this can be found [here](https://docs.opencv.org/4.3.0/da/df6/tutorial_py_table_of_contents_setup.html).

As far as importing the library itself into the code, there's a tiny complication:

```python
# If you're lucky, this'll do the job
import cv2

# But in some cases, the opencv library doesn't play nice with the python execition architercuture, and just outright doesn't register the cv2 module as imported. This problem can be solved with substituting the former import with the following:
import cv2.cv2 as cv2
```



#### Basic Image Manipulation

OpenCV makes it easy for us to open and view various media sources, this is because we'll be doing this very frequently. A very important thing to note before diving into the code is that all images are represented by a color channel and an alpha channel. The color channel represent which colors are prominent in the image, and the alpha channel denotes the amount of transparency. In the example below you can see how we can import an image:

```python
import cv2

# The imread() method has 2 arguments
# 1) filepath - absolute or relative path to the source file
# 2) readmode - mode in which the file will be read, this argument has 3 potential values:
#	- cv.IMREAD_GRAYSCALE : reads in greyscale mode (reads shades of gray, not color)
#	- cv.IMREAD_COLOR : reads using the color channel, whithout the alpha channel
#	- cv.IMREAD_UNCHANGED : reads both the color and alpha channel
#	- (the second argument can be left out, it's default value is 1 - cv.IMREAD_COLOR)
img = cv2.imread("Resources/sampleImage.jpg")

# This next function creates a window in which the specified image fits.
cv2.imshow("Our first image", img)

# If you execture the code up to this snippet, the image will load, the window will appear... but then immediatelly dissappear. Because of this we need to prevent the program from terminating by waiting for keyboard input, and process the input until we get the kill command. 
while True:
    keyInput = cv2.waitKey(0)
    # ord() just converts the given letter to coresponding ascii code, useful ascii codes to remember are: 
    # 27  - escape
    # 127 - delete
    # 13  - enter
    if keyInput == ord('q'):
        # Note that this function identifies the window that will be deleted by its name, not the variable 	it's stored in.
        cv2.destroyWindow("Our first image")
```



We managed to display an image, however depending on its resolution it might take up a lot of your screen real-estate. So let's try and resize the images we have to a reasonable size and organize them in a single window:

```python
import cv2.cv2 as cv2
import numpy as np

img1 = cv2.imread("Resources/sampleImage.jpg")
img2 = cv2.imread("Resources/sampleImage2.jpg")

# We resize the original image and then show it. The second argument here is the shape of a numpy array's shape value, which denotes it's width and height (more on this later).
smallImg1 = cv2.resize(img1, (800, 600))
smallImg2 = cv2.resize(img2, (800, 600))

stackedImage = cv2.hconcat([smallImg1,smallImg2])

cv2.imshow("Stacked",stackedImage)

while True:
    keyInput = cv2.waitKey(0)
    if keyInput == ord('q'):
        cv2.destroyAllWindows()

```



As you can see, the images we're manipulating are nothing more than `numpy` multidimensional arrays, or in simpler terms matrices with 3 color values inside each matrix field, (e.g. BGR for OpenCV). So combining two images is nothing more than making a matrix that can contain both images, and copying the matrix values into corresponding sectors of the resulting matrix. 



#### Drawing Basics

In most cases, when an object has been detected, some sort of circle, rectangle or polygon is drawn on top of the source image to properly indicate that it's present. For this purpose, we need to learn how to draw basic shapes with OpenCV, let's start with making a blank canvas.

```python
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
```

> Important note: In a normal cartesian coordinate system, the `y` coordinate increases in value from the bottom-up, however, in OpenCV (and most computer vision and graphics software), the `y` coordinate increases in value from the top-down.



Aside from drawing lines manually, we can also use in-built functions:

```python
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

```



#### Object Detection Basics

First off, `object detection` is the act of recognizing that an entity of a specific type is present in our image and then define where it is in the picture with a center coordinate as well as size parameters (x, y, width, height). To do this, we'll be using the deep neural network module integrated into OpenCV. To utilize this neural network, we need an algorithm to harness it. In our case, we'll be utilizing the YOLO (You Only Look Once) algorithm for a couple of reasons:

1. It's fast (because it only **looks once**)
2. It easy to learn and implement
3. Training is a piece of cake