from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image
import PIL


def adjust_brightness(img , lvl):
    return np.floor(img/lvl)

# main function for intensity where you can choose the filter
def main(img_path):

    img = misc.imread(img_path)

    for i in range(7, 0, -1):
        # changing the brightness of the image
        new_img = adjust_brightness(img, (2**i))

        # path and name of the new image
        new_name = "output/1.2/" + str(int(256/(2**i))) + "niveis.png"

        # saving the new image
        plt.imsave(new_name, new_img, cmap='gray')

        # showing the new image with the filter applied
        plt.imshow(new_img, cmap='gray')
        plt.show()


if __name__ == "__main__":
    main(sys.argv[1])
