#!/usr/bin/env python

import rospy
import time
from datetime import datetime
from std_msgs.msg import Float64, String
from time_synchronization.msg import talker_msg
from time_synchronization.srv import talker2
from talker import Talker



def main():

    rospy.init_node("talker_2")
    rospy.on_shutdown(stop)

    time_pub = rospy.Publisher('/talker_2', talker_msg, queue_size=10)

    rospy.loginfo(' Starting the talker_2 node! ')

    talker = Talker('talker_2')
    serv = rospy.Service('talker2', talker2, talker.service_callback )

    talker.talk(time_pub)



def stop():
    rospy.loginfo('Ending the program!')

if __name__ == '__main__':
    main()

