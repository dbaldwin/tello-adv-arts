from droneblocksutils.image_effects import style_transfer, reset_style_model
import cv2
import imutils

models = [
    "../models/starry_night.t7",
    "../models/candy.t7",
    "../models/feathers.t7",
    "../models/la_muse.t7",
    "../models/the_scream.t7",
    "../models/udnie.t7",
    "../models/mosaic.t7"

]

if __name__ == '__main__':
    image = cv2.imread('../media/chicago-skyline.jpg')
    image = imutils.resize(image, width=500)

    for model in models:
        new_image = style_transfer(image, model)

        cv2.imshow("Chicago", image)
        cv2.imshow(model.replace("../models/","").replace(".t7", ""), new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        reset_style_model()
