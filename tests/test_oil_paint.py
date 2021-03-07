from droneblocksutils.image_effects import oil_painting
import cv2
import imutils

if __name__ == '__main__':
    image = cv2.imread('../media/chicago-skyline.jpg')
    image = imutils.resize(image, width=600)

    new_image = oil_painting(image)

    cv2.imshow("Original", image)
    cv2.imshow("Oil Painting", new_image)
    cv2.waitKey(0)