from scipy import misc
import matplotlib.pyplot as plt
import math
import numpy as np
import sys


def imageResolution(img, res):

    size = 512,512
    new_img = np.resize(img, size)
    return new_img


def main(img_path, times):

    # Reading image and applying filters
    img = misc.imread(img_path)
    new_img = imageResolution(img, int(times))
    new_name = "output/1.1/" + times + ".png"

    # Saving image
    plt.imsave(new_name, new_img, cmap='gray')

    # showing the new image with the filter applied
    plt.imshow(new_img, cmap='gray')
    plt.show()


# Argument1 = image | Argument2 = times reduced
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
