from robohead_controller_actions.main import *
import rospy
import os
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
import numpy as np

latest_image_msg = None

def image_callback(msg):
    global latest_image_msg
    latest_image_msg = msg

def run(robohead_controller: RoboheadController, cmds: str):
    global latest_image_msg
    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'

    # Настройка ушей
    msg = EarsSetAngleRequest()
    msg.left_ear_angle = -30
    msg.right_ear_angle = -30
    robohead_controller.ears_driver_srv_EarsSetAngle(msg)

    # Настройка шеи
    msg = NeckSetAngleRequest()
    msg.horizontal_angle = 0
    msg.vertical_angle = 30
    msg.duration = 1
    msg.is_blocking = 1
    robohead_controller.neck_driver_srv_NeckSetAngle(msg)

    # Подписка на видеопоток
    rospy.Subscriber('/front_camera/image_raw/compressed', CompressedImage, image_callback)
    rospy.sleep(0.5)  # время на запуск подписки

    # Запуск видеопотока на экран на 7 секунд
    cvBridge = CvBridge()
    start_time = rospy.get_time()
    while rospy.get_time() - start_time < 7.0:
        if latest_image_msg:
            np_arr = np.frombuffer(latest_image_msg.data, np.uint8)
            cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            cv_image = cv2.resize(cv_image, (1080, 1080))

            robohead_controller.display_driver_pub_PlayMedia.publish(
                cvBridge.cv2_to_imgmsg(cv_image, encoding="bgr8"))

        rospy.sleep(0.05)  # ~20 кадров в секунду

 #   rospy.sleep(4)
