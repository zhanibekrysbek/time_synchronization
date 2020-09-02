#!/usr/bin/env python

import rospy
import subprocess
# import shlex
import time
from datetime import datetime
from std_msgs.msg import Float64, String
from time_synchronization.srv import talker2


class Talker(object):

    def __init__(self):
        # false: silent
        # true: talking
        self.state = False

    def service_callback(self, req):
        rospy.loginfo('talker_2 service is called: %s', req.req)

        if req.req == 'talk':
            self.state = True

            return 'Starting to talk'

        elif req.req == 'stop':
            self.state = False

            return 'Going silent'

        else:
            return 'Unknown command! Use either "talk" -or- "stop" '

    def talk(self, time_pub):

        rate = rospy.Rate(50)
        t0 = rospy.get_time()
        ind = 0
        while not rospy.is_shutdown():

            if self.state:
                now = rospy.get_time() - t0

                time_pub.publish(str(ind) + " " + str(now))

                ind+=1

            rate.sleep()


def main():
    rospy.init_node("talker_1")
    rospy.on_shutdown(stop)

    time_pub = rospy.Publisher('/talker_2', String, queue_size=10)

    rospy.loginfo(' Starting the talker_2 node! ')

    talker = Talker()
    serv = rospy.Service('talker2', talker2, talker.service_callback )

    talker.talk(time_pub)



def stop():
    rospy.loginfo('Ending the program!')

if __name__ == '__main__':
    main()

