import rospy
from clover import srv
import math

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)

def wait_arrival(tolerance=0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)
