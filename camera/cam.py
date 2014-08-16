#!/usr/bin/python
import cv
import os,time,sys,time

size = width, height = 640, 480
#speed = [1, 1]
#black = 0, 0, 0

#print os.path.isfile('/dev/video0')
#print os.path.exists('/dev/video0')
if os.path.exists('/dev/video0') ==False:
    print "no video0,exit"
    sys.exit(2)

try:
   cam = cv.CreateCameraCapture(0)
   cv.SetCaptureProperty(cam,cv.CV_CAP_PROP_FRAME_WIDTH, 640)
   cv.SetCaptureProperty(cam,cv.CV_CAP_PROP_FRAME_HEIGHT, 480);
except:
   print "system error,exit"
   sys.exit(1)

k=0
t = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
filename = '%s.jpg' %(t)
while 1:
    k += 1
    if k > 8: break
    try:
        cv.GrabFrame(cam)
        img = cv.RetrieveFrame(cam)
        cv.SaveImage(filename, img)
    except:
        pass
    cv.WaitKey(1500)
