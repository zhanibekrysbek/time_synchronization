import rospy
import time
from datetime import datetime
from std_msgs.msg import Float64, String
from time_synchronization.msg import talker_msg
from time_synchronization.srv import talker1, talker2


class Talker(object):

    def __init__(self, name, rate = 50):
        # false: silent
        # true: talking
        self.state = False
        self.name = name
        self.rate = rospy.Rate(rate)

    def service_callback(self, req):
        rospy.loginfo('%s service is called: %s', self.name, req.req)

        if req.req == 'talk':
            self.state = True
            self.t0 = rospy.get_time()
            
            rospy.loginfo('%s: talking', self.name)
            return 'Starting to talk'

        elif req.req == 'stop':
            self.state = False
            rospy.loginfo('%s: going silent', self.name)
            return 'Going silent'

        else:
            return 'Unknown command! Use either "talk" -or- "stop" '

    def talk(self, time_pub):

        ind = 0
        while not rospy.is_shutdown():

            if self.state:
                now = rospy.get_time() - self.t0

                msg = talker_msg()
                msg.time = now
                msg.msg_id = ind

                msg.word = self.name + ' data'

                time_pub.publish(msg)

                ind += 1

            self.rate.sleep()

