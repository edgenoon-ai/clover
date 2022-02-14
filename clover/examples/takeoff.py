import rospy
from clover import srv
from common import wait_arrival

rospy.init_node('flight')
navigate = rospy.ServiceProxy('navigate', srv.Navigate)

print('Take off and hover 3 m above the ground')
navigate(x=0, y=0, z=3, frame_id='body', auto_arm=True)
wait_arrival()
