import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
from common import wait_arrival

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)

actual = get_telemetry()

print('Fly to GPS position')

# lonley landing pad
navigate_global(lat=47.397664, lon=8.5452953, z=actual.z, yaw=math.inf, speed=1)
wait_arrival()

rospy.loginfo('Arrive to 1. point')
rospy.sleep(5.0)

# landing pad with rover
navigate_global(lat=47.3975913, lon=8.5456449, z=actual.z, yaw=math.inf, speed=1)
wait_arrival()

rospy.loginfo('Arrive to 2. point')
rospy.sleep(5.0)

# landing pad with pickoup
navigate_global(lat=47.3980788, lon=8.5457014, z=actual.z, yaw=math.inf, speed=1)
wait_arrival()

rospy.loginfo('Arrive to 3. point')
rospy.sleep(5.0)