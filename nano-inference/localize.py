# A simple test script to access results of a classification
import jetson.inference
import jetson.utils

# load the object detection model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")  # using V4L2 ????

# display = jetson.utils.glDisplay()

while display.IsOpen():
    # main loop will go here
    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height)
    print(detections)
