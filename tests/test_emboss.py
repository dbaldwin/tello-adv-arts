from droneblocksutils.image_effects import emboss
import cv2
import imutils

if __name__ == '__main__':
    image = cv2.imread('../media/chicago-skyline.jpg')
    image = imutils.resize(image, width=600)

    new_image = emboss(image, emboss_size=3)

    cv2.imshow("Original", image)
    cv2.imshow("Emboss", new_image)
    cv2.waitKey(0)
