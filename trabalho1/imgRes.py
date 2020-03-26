from scipy import misc
import matplotlib.pyplot as plt
import math
import numpy as np
import sys
import cv2

def imageResolution(img):
    scale_percent = 50  # percent of original size
    j = 1
    for i in range(6):
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        new_img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)

        new_name = "output/1.1/interaction " + str(j) + ".png"
        # Saving image
        plt.imsave(new_name, new_img, cmap='gray')
        plt.imshow(new_img, cmap='gray')
        plt.show()
        j += 1

def main(img_path):

    # Reading image and applying filters
    img = misc.imread(img_path)
    imageResolution(img)


# Argument1 = image | Argument2 = times reduced
if __name__ == "__main__":
    main(sys.argv[1])
