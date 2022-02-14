# Information: https://clover.coex.tech/programming

import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

land = rospy.ServiceProxy('land', Trigger)

land()
