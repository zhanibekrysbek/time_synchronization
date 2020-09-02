#!/usr/bin/env python

import rospy
import time
from datetime import datetime
from std_msgs.msg import Float64, String
from time_synchronization.msg import talker_msg
from time_synchronization.srv import talker1
from talker import Talker



def main():

    rospy.init_node("talker_1")
    rospy.on_shutdown(stop)

    time_pub = rospy.Publisher('/talker_1', talker_msg, queue_size=10)

    rospy.loginfo(' Starting the talker_1 node! ')

    talker = Talker('talker_1')
    serv = rospy.Service('talker1', talker1, talker.service_callback )

    talker.talk(time_pub)



def stop():
    rospy.loginfo('Ending the program!')

if __name__ == '__main__':
    main()

