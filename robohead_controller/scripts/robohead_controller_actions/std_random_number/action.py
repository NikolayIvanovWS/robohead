from robohead_controller_actions.main import *

import cv2
from cv_bridge import CvBridge
import numpy as np
import random

def run(robohead_controller:RoboheadController, cmds:str): # Обязательно наличие этой функции, именно она вызывается при голосовой команде
    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'

    msg = PlayAudioRequest()
    msg.path_to_file = script_path + 'random_number.mp3'
    msg.is_blocking = 0
    msg.is_cycled = 0
    robohead_controller.speakers_driver_srv_PlayAudio(msg)

    msg = EarsSetAngleRequest()
    msg.left_ear_angle = -30
    msg.right_ear_angle = -30
    robohead_controller.ears_driver_srv_EarsSetAngle(msg)

    msg = NeckSetAngleRequest()
    msg.horizontal_angle = 0
    msg.vertical_angle = 30
    msg.duration = 1
    msg.is_blocking = 1
    robohead_controller.neck_driver_srv_NeckSetAngle(msg)

    cvBridge = CvBridge()

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 10
    fontColor = (255,255,255)
    thickness = 20
    lineType = 5

    for _ in range(4):
        random_number = round(random.uniform(45.00, 85.00), 2)
        str_number = f"{random_number:.2f}"
        timer_start = rospy.get_time()

    
        while (rospy.get_time() - timer_start) < 1:
        # Создаем черное изображение
            black_image = np.zeros((1080, 1080, 3), dtype=np.uint8)

        # Вычисляем положение текста (по центру)
            text_size = cv2.getTextSize(str_number, font, fontScale, thickness)[0]
            text_x = (1080 - text_size[0]) // 2
            text_y = (1080 + text_size[1]) // 2

        # Наносим цифру на изображение
            cv2.putText(
                black_image,
                str_number,
                (text_x, text_y),
                font,
                fontScale,
                (255, 255, 255),  # белый цвет
                thickness,
                lineType
            )

        # Публикуем изображение
            robohead_controller.display_driver_pub_PlayMedia.publish(
                cvBridge.cv2_to_imgmsg(black_image, encoding="bgr8")
            )
