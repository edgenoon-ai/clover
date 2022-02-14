 #!/usr/bin/env python3
import sys
import rospy
import cv2

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
 
class ImageGrabber:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("main_camera/image_raw", Image, self.callback)
 
    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
 
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)
 
if __name__ == '__main__':
    ig = ImageGrabber()
    rospy.init_node('image_grabber', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()