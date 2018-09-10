


import cv2

import os

from threading import Thread

import subprocess
import numpy as np

import imutils

from collections import deque

from pynput.mouse import Button, Controller

mouse = Controller()

# def MyThread ():

# MyThread().start()





def func1():
	os.system("C:\Users\harman.singh.bhutani\Desktop\osk.exe");



if __name__ == '__main__':
    Thread(target = func1).start()


# subprocess.call(["C:\Windows\System32\osk.exe"])


mouse.position = (1024/2,1080/2)

RedLower = (0,70,50)

RedUpper = (10,255,255)

pts = deque(maxlen=64)

cam = cv2.VideoCapture(0)

while True:
	
	(grabbed, frame) = cam.read()


	frame = imutils.resize(frame, width=600)


	# font = cv2.FONT_HERSHEY_SIMPLEX
	# cv2.putText(frame, 'Harman', (40, 450), font, 2, (255, 255, 255), 2, cv2.LINE_AA)



	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, RedLower, RedUpper)

	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=15)
    #filteration methods for clean contours
	con = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    #finding contour area's
		cv2.CHAIN_APPROX_SIMPLE)[-2]

	center = None

	if len(con) > 0:

		c = max(con, key=cv2.contourArea)

		((x, y), radius) = cv2.minEnclosingCircle(c)
		#get its coordinates  and radius

		M = cv2.moments(c)

		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:

			mouse.position = (x*4, y*2)

			cv2.circle(frame, (int(x), int(y)), int(radius),
            
 				(0, 255, 255), 2)

			cv2.circle(frame, center, 5, (0, 0, 255), -1)

	pts.appendleft(center)

	cv2.imshow("Frame", frame)



	key = cv2.waitKey(1) & 0xFF

	if key == ord("h"):
		break


camera.release()


cv2.destroyAllWindows()
