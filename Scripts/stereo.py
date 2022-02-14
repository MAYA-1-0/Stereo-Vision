#! /usr/bin/env python 
from capture import VideoGet
import cv2
import math
import rospy
from std_msgs.msg import Int32
import signal
global d,w


pub = rospy.Publisher("/direction",Int32,queue_size = 1)

CAM_0_CONFIG = "nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv flip-method=0 ! video/x-raw, width=640, height=480, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink sync=true "
#CAM_1_CONFIG = "nvarguscamerasrc sensor-id=1 ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv flip-method=0 ! video/x-raw, width=640, height=480, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink sync=true"

face_cascade=cv2.CascadeClassifier("/home/brain/stereo_ws/src/stereo_vision/src/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")

cam_0 = VideoGet(CAM_0_CONFIG)
#cam_1 = VideoGet(CAM_1_CONFIG)

cam_0.start()
#cam_1.start()


def keyboardInterruptHandler(signal, frame):
    	print("interrupt detected")
	cam_0.stop()
        exit(0)


def detect_face(cam,n):
  global d,w
  if True:
    frame=cam
    d=0
    w=0
    #cv2.imshow("Frame-{}".format(n),frame)
    width=frame.shape[0]
    height=frame.shape[1]
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.5,5)
    for x,y,w,h in faces:
      #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
      d=320-(x+(w/2))
      p = 240-(y+(h/2))	
      theta=(math.pi/2)-(d*0.654498)/320
      #cv2.putText(frame,"Angle"+str(theta*57.3),(x,y-1),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
      #cv2.imshow("Frame-{}".format(n),frame)
      roi_gray=gray[y:y+h,x:x+x+w]
      roi_color=frame[y:y+h,x:x+x+w]
      return theta

def dist(TL,TR):
	a=(6*math.sin(TL))/math.sin(math.pi-TL-TR)
	b=(6*math.sin(TR))/math.sin(math.pi-TL-TR)
	dist1=a*math.sin(TL)
	dist2=b*math.sin(TR)
	print("dist1 :",dist1,"dist2 :",dist2)
	return (dist1+dist2)/2
	



if __name__ == '__main__':
	while not cam_0.stopped : #and not cam_1.stopped:
		#frames=(cam_0.frame,cam_1.frame)
		theta_r=detect_face(cam_0.frame,0)
                global d,w
	        rospy.init_node("pub")
		rate=rospy.Rate(10)
		if abs(d)>w:
		  dir=d/abs(d)
		  pub.publish(dir)
		  rospy.loginfo(dir)
		  rate.sleep()
                else:
                  pub.publish(0)
		  rospy.loginfo(0)

		#theta_l=detect_face(frames[1],1)
		#distance=0
		#if theta_r and theta_l:
			#distance=dist(float(theta_l),float(theta_r))

		signal.signal(signal.SIGINT, keyboardInterruptHandler)
		k = cv2.waitKey(1)
		if k==ord('q'):
			cam_0.stop()
			break
	








