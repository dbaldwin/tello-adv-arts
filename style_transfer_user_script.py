from droneblocksutils.image_effects import apply_style_transfer

time_between_styles = 3 # in seconds

def init(tello, fly_flag=False):
    """

    :param tello: Reference to the DJITelloPy Tello object.
    :type tello: Tello
    :param fly_flag: True - the fly flag was specified and the Tello will take off. False - the Tello will NOT
                        be instructed to take off
    :type fly_flag:  bool
    :return: None
    :rtype:
    """
    print(f"Inside init method.  fly_flag: {fly_flag}")


def handler(tello, frame, fly_flag=False):
    """

    :param tello: Reference to the DJITelloPy Tello object.
    :type tello: Tello
    :param frame: image
    :type frame:
    :param fly_flag: True - the fly flag was specified and the Tello will take off. False - the Tello will NOT
                        be instructed to take off
    :type fly_flag:  bool
    :return: None or frame.  If frame, then use the returned frame for display
    :rtype:
    """

    new_image = apply_style_transfer(frame, time_between_styles)

    return new_image
