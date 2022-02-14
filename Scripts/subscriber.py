#! /usr/bin/env python 
from std_msgs.msg import Int64
import rospy
from dynamixel_workbench_msgs.msg import DynamixelStateList
from dynamixel_workbench_msgs.srv import DynamixelCommand,DynamixelCommandRequest

d=0
position=0
client=rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command',DynamixelCommand)

def callback1(dir1):
	global d,position
	#rospy.loginfo(dir1.data)
	d=dir1.data
#	rospy.loginfo(d)
	req =DynamixelCommandRequest()
	req.id=50
	req.addr_name="Goal_Position"
	req.value=position+(d*200)
	rospy.loginfo(position+(d*200))
	resp=client(req)

def callback2(pos):
	global position
	rospy.loginfo(pos.dynamixel_state[2].present_position)
	position=(pos.dynamixel_state[2].present_position)
	rospy.loginfo(position)

def listener():
	rospy.init_node("Subscriber")
        rospy.Subscriber("/direction",Int64,callback1)
	rospy.Subscriber("/dynamixel_workbench/dynamixel_state",DynamixelStateList,callback2)



if __name__=="__main__":
#	while True:
	listener()
	rospy.spin()
