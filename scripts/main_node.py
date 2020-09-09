#!/usr/bin/env python

import rospy
import subprocess
import time
from datetime import datetime
from std_msgs.msg import Float64, String
from time_synchronization.srv import talker1, talker2

class talker_handle(object):

	def __init__(self):
		# wait until both services will be available in the network
		rospy.wait_for_service('talker1')
		rospy.wait_for_service('talker2')

		self.talker1_serv = rospy.ServiceProxy('talker1', talker1)
		self.talker2_serv = rospy.ServiceProxy('talker2', talker1)

	def start(self):
		# trigger two nodes to broadcast data
		self.talker1_serv('talk')
		self.talker2_serv('talk')

	# to be called on rospy shutdown
	def stop(self):

		rospy.loginfo('Ending the program!')
		self.talker1_serv('stop')
		self.talker2_serv('stop')


def main():

	rospy.init_node('main_node')

	rospy.loginfo('starting up talker1 and talker2')

	handle = talker_handle()

	handle.start()

	rospy.on_shutdown(handle.stop)

	rospy.spin()


if __name__=='__main__':

	main()
