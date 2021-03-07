from droneblocksutils.image_effects import line_drawing
import cv2
import imutils

if __name__ == '__main__':
    image = cv2.imread('../media/chicago-skyline.jpg')
    image = imutils.resize(image, width=600)

    new_image = line_drawing(image, inverse_image=False)

    cv2.imshow("Original", image)
    cv2.imshow("Line Drawing", new_image)
    cv2.waitKey(0)
