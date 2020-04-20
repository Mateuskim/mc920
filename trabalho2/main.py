import sys
from scipy import misc
import matplotlib.pyplot as plt

from filters import *


def main(img_path, function):
    # reading the image
    new_img = img = misc.imread(img_path)

    new_img = 255*apply_filter(new_img/255, function)
    # path and name of the new image
    new_name = "output/" + img_path[4:-4] + '-' + function + ".png"

    # saving the new image
    plt.imsave(new_name, new_img, cmap='gray', vmin=0, vmax=255)

    plt.imshow(new_img, cmap='gray', vmin=0, vmax=255)
    plt.show()


def main_all(img_path):
    # reading the image
    img = misc.imread(img_path)
    x = []
    for i in range(1,10):
        x.append(255*apply_filter(img/255, 'h'+str(i)))

    plt.figure(figsize=(10,10))
    for i in range(9):
        plt.subplot(3,3,i+1)
        if i != 8:
            plt.title('H' + str(i+1))
        else:
            plt.title('SQRT(H3² + H4²)')
        plt.imshow(x[i], cmap='gray', vmin=0, vmax=255)
    # path and name of the new image
    new_name = "output/" + img_path[4:-4] + '_all_imgs.png'

    # saving the new image
    plt.savefig(new_name, cmap='gray', vmin=0, vmax=255)
    plt.show()



if __name__ == "__main__":
    if len(sys.argv) == 2:
        main_all(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("python3 main.py [IMG_PATH] [FILTER]*")
        print("* - optional")
