from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import sys
import cv2

def imageResolution(img):
    dimI = (img.shape[1], img.shape[0])
    for i in range(6):
        width = int(img.shape[1]/2)
        height = int(img.shape[0]/2)
        dim = (width, height)

        # resize image
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        new_img = cv2.resize(img, dimI, interpolation=cv2.INTER_AREA)

        new_name = "output/1.1/" + str(int(512/2**(i+1))) +"x"+ str(int(512/2**(i+1))) + ".png"
        # Saving image
        plt.imsave(new_name, new_img, cmap='gray')
        plt.imshow(new_img, cmap='gray')
        plt.show()

def main(img_path):

    # Reading image and applying filters
    img = misc.imread(img_path)
    imageResolution(img)


# Argument1 = image | Argument2 = times reduced
if __name__ == "__main__":
    main(sys.argv[1])
