from robohead_controller_actions.main import *
import rospy
import cv2
from cv_bridge import CvBridge
import numpy as np
from sensor_msgs.msg import CompressedImage
import os

# Глобальная переменная для хранения последнего кадра из топика
latest_compressed_image_msg = None

def compressed_image_callback(msg):
    global latest_compressed_image_msg
    latest_compressed_image_msg = msg

def save_image(cv_image):
    """
    Сохраняет изображение в домашнюю папку пользователя.
    :param cv_image: Изображение в формате OpenCV (numpy массив).
    """
    # Определяем путь к домашней папке
    home_directory = os.path.expanduser("~")
    # Создаем имя файла с временной меткой
    timestamp = rospy.get_time()
    file_name = f"photo_{int(timestamp)}.jpg"
    file_path = os.path.join(home_directory, file_name)

    # Сохраняем изображение
    try:
        cv2.imwrite(file_path, cv_image)
        rospy.loginfo(f"Фотография успешно сохранена: {file_path}")
    except Exception as e:
        rospy.logerr(f"Ошибка при сохранении фотографии: {e}")

def run(robohead_controller: RoboheadController, cmds: str):  # Обязательно наличие этой функции, именно она вызывается при голосовой команде
    global latest_compressed_image_msg
    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'

    # Подписка на топик /front_camera/image_raw/compressed
    rospy.Subscriber('/front_camera/image_raw/compressed', CompressedImage, compressed_image_callback)
    rospy.sleep(0.5)  # Даем время для получения первого кадра

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

    cvBridge = CvBridge()

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 10
    fontColor = (255, 255, 255)
    thickness = 20
    lineType = 5

    prev_img = robohead_controller.usb_cam_image_raw

    for num in range(3, 0, -1):
        str_num = str(num)
        timer_start = rospy.get_time()

        while (rospy.get_time() - timer_start) < 1:
            if latest_compressed_image_msg:
                # Если есть данные с топика /front_camera/image_raw/compressed
                np_arr = np.frombuffer(latest_compressed_image_msg.data, np.uint8)
                cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            else:
                # Если данных с топика нет, используем usb_cam_image_raw
                try:
                    cv_image = cvBridge.imgmsg_to_cv2(robohead_controller.usb_cam_image_raw, "bgr8")
                except Exception as e:
                    rospy.logwarn(f"Ошибка при получении изображения из usb_cam_image_raw: {e}")
                    cv_image = np.zeros((1080, 1080, 3), dtype=np.uint8)  # Черный экран в случае ошибки

            # Изменяем размер изображения до 1080x1080
            cv_image = cv2.resize(cv_image, (1080, 1080))

            # Наносим обратный отсчет
            bottomLeftCornerOfText = (
                1080 // 2 - cv2.getTextSize(str_num, font, fontScale, thickness)[0][0] // 2,
                1080 // 2 + cv2.getTextSize(str_num, font, fontScale, thickness)[0][1] // 2
            )
            cv2.putText(
                cv_image,
                str_num,
                tuple(bottomLeftCornerOfText),
                font,
                fontScale,
                fontColor,
                thickness,
                lineType
            )

            # Публикуем изображение
            robohead_controller.display_driver_pub_PlayMedia.publish(
                cvBridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
            )

    # Воспроизведение звука
    msg = PlayAudioRequest()
    msg.path_to_file = script_path + 'make_photo.mp3'
    msg.is_blocking = 0
    msg.is_cycled = 0
    robohead_controller.speakers_driver_srv_PlayAudio(msg)

    rospy.sleep(0.5)

    # Определяем источник изображения для финальной фотографии
    if latest_compressed_image_msg:
        # Если есть данные с топика /front_camera/image_raw/compressed
        np_arr = np.frombuffer(latest_compressed_image_msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    else:
        # Если данных с топика нет, используем usb_cam_image_raw
        try:
            cv_image = cvBridge.imgmsg_to_cv2(robohead_controller.usb_cam_image_raw, "bgr8")
        except Exception as e:
            rospy.logwarn(f"Ошибка при получении изображения из usb_cam_image_raw: {e}")
            cv_image = np.zeros((1080, 1080, 3), dtype=np.uint8)  # Черный экран в случае ошибки

    # Изменяем размер изображения до 1080x1080
    cv_image = cv2.resize(cv_image, (1080, 1080))

    # Сохраняем фотографию
    save_image(cv_image)

    # Публикуем финальное изображение
    robohead_controller.display_driver_pub_PlayMedia.publish(
        cvBridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
    )

    rospy.sleep(4)