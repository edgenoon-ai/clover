import rospy
from clover import srv
from common import wait_arrival


rospy.init_node('flight')
navigate = rospy.ServiceProxy('navigate', srv.Navigate)

navigate(x=4, y=-2, z=0, frame_id='body')
wait_arrival()

