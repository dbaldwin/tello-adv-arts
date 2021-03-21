import cv2
import imutils
from droneblocksutils.image_effects import *

if __name__ == '__main__':
    image = cv2.imread('../media/chicago-skyline.jpg')
    image = imutils.resize(image, width=600)

    new_image = oil_painting(image)

    cv2.imshow("Original", image)
    cv2.imshow("Oil Painting", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    image = cv2.imread('../media/chicago-skyline.jpg')
    image = imutils.resize(image, width=600)

    new_image = style_transfer(image, "../models/starry_night.t7")

    cv2.imshow("Chicago", image)
    cv2.imshow("StyleTransfer", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    reset_style_model()
