import sys
from scipy import misc
import matplotlib.pyplot as plt

from filters import *


def main(img_path, function):
    # reading the image
    new_img = img = misc.imread(img_path)

    new_img = apply_filter(new_img, function)

    # path and name of the new image
    new_name = "output/" + img_path[4:-4] + '-' + function + ".png"

    # saving the new image
    plt.imsave(new_name, new_img, cmap='gray', vmin=0, vmax=255)

    plt.imshow(new_img, cmap='gray', vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
