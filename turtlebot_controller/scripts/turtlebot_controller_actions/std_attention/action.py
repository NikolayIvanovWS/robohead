from turtlebot_controller_actions.main import *

def run(turtlebot_controller:TurtlebotController, cmds:str): # Обязательно наличие этой функции, именно она вызывается при голосовой команде
    script_path = os.path.dirname(os.path.abspath(__file__)) + '/'
    
    msg = PlayMediaRequest()
    msg.is_blocking = 0
    msg.is_cycled = 0
    msg.path_to_file = script_path + 'attention.png'
    turtlebot_controller.display_driver_srv_PlayMedia(msg)

    msg = EarsSetAngleRequest()
    msg.left_ear_angle = -30
    msg.right_ear_angle = -30
    turtlebot_controller.ears_driver_srv_EarsSetAngle(msg)

    msg = NeckSetAngleRequest()
    msg.horizontal_angle = min(max(turtlebot_controller.respeaker_driver_doa_angle, -30),30)
    msg.vertical_angle = 30
    msg.duration = 1
    msg.is_blocking = 0
    turtlebot_controller.neck_driver_srv_NeckSetAngle(msg)

    msg = PlayAudioRequest()
    msg.path_to_file = script_path + 'attention.mp3'
    msg.is_blocking = 1
    msg.is_cycled = 0
    turtlebot_controller.speakers_driver_srv_PlayAudio(msg)