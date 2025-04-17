from robohead_controller_actions.main import *

def run(robohead_controller:RoboheadController, cmds:str): # Обязательно наличие этой функции, именно она вызывается при голосовой команде
    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'
    msg = PlayMediaRequest()
    msg.is_blocking = 0
    msg.is_cycled = 0
    msg.path_to_file = script_path + 'look_around_2.png'
    robohead_controller.display_driver_srv_PlayMedia(msg)

    msg = PlayAudioRequest()
    msg.path_to_file = script_path + 'look_around.mp3'
    msg.is_blocking = 0
    msg.is_cycled = 0
    robohead_controller.speakers_driver_srv_PlayAudio(msg)

    msg = NeckSetAngleRequest()
    msg.horizontal_angle = -30
    msg.vertical_angle = 0
    msg.duration = 2
    msg.is_blocking = 1
    robohead_controller.neck_driver_srv_NeckSetAngle(msg)

    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'
    msg = PlayMediaRequest()
    msg.is_blocking = 0
    msg.is_cycled = 0
    msg.path_to_file = script_path + 'look_around_3.png'
    robohead_controller.display_driver_srv_PlayMedia(msg)

    msg = NeckSetAngleRequest()
    msg.horizontal_angle = 30
    msg.vertical_angle = 0
    msg.duration = 2
    msg.is_blocking = 1
    robohead_controller.neck_driver_srv_NeckSetAngle(msg)

    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'
    msg = PlayMediaRequest()
    msg.is_blocking = 0
    msg.is_cycled = 0
    msg.path_to_file = script_path + 'look_around_2.png'
    robohead_controller.display_driver_srv_PlayMedia(msg)

    msg = NeckSetAngleRequest()
    msg.horizontal_angle = -30
    msg.vertical_angle = 0
    msg.duration = 2
    msg.is_blocking = 1
    robohead_controller.neck_driver_srv_NeckSetAngle(msg)

    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'
    msg = PlayMediaRequest()
    msg.is_blocking = 0
    msg.is_cycled = 0
    msg.path_to_file = script_path + 'look_around_3.png'
    robohead_controller.display_driver_srv_PlayMedia(msg)

    msg = NeckSetAngleRequest()
    msg.horizontal_angle = 30
    msg.vertical_angle = 0
    msg.duration = 2
    msg.is_blocking = 1
    robohead_controller.neck_driver_srv_NeckSetAngle(msg)

    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'
    msg = PlayMediaRequest()
    msg.is_blocking = 0
    msg.is_cycled = 0
    msg.path_to_file = script_path + 'look_around_2.png'
    robohead_controller.display_driver_srv_PlayMedia(msg)

    msg = NeckSetAngleRequest()
    msg.horizontal_angle = 0
    msg.vertical_angle = 0
    msg.duration = 2
    msg.is_blocking = 1
    robohead_controller.neck_driver_srv_NeckSetAngle(msg)