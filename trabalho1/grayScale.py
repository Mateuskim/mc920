from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import sys
import math

def log(img):
    new_img = np.log(img+1)
    c = 255/np.max(new_img+1)
    return c*new_img


def exp(img):
    new_img = img/255
    new_img = np.exp(new_img)
    c = 255/np.max(new_img)
    return c*(new_img-1)


def square(img):
    new_img = img/255
    new_img = np.square(new_img)
    c = 255/np.max(new_img)
    return c*(new_img)


def rootSq(img):
    new_img = np.sqrt(img)
    c = 255/np.max(new_img+1)
    return c*new_img


def contrast(img):
    alpha  = float(input("Digite os valor de alpha:"))
    beta = float(input("Digite os valor de beta:"))
    gama = float(input("Digite os valor de gama:"))
    a = int(input("Digite os valor de a:"))
    b = int(input("Digite os valor de b:"))
    new_img = img
    new_img = np.where(new_img <= a, alpha * new_img,
                    np.where(new_img <= b, beta*(new_img-a) + alpha * a,
                            gama * (new_img - b) + beta * (b - a) + alpha * a
                    ))
    return new_img


# main function for intensity where you can choose the filter
def main(img_path, function):
    new_img = img = misc.imread(img_path)

    if function == "log":
        new_img = log(img).astype(int)
    elif function == "exp":
        new_img = exp(img).astype(int)
    elif function == "sqrt":
        new_img = square(img).astype(int)
    elif function == "root":
        new_img = rootSq(img).astype(int)
    elif function == "contrast":
        new_img = contrast(img).astype(int)

    # path and name of the new image
    new_name = "output/1.3/"+img_path[4:-4]+'-'+function+".png"

    # saving the new image
    plt.imsave(new_name, new_img, cmap='gray', vmin=0, vmax=255)

    plt.imshow(new_img, cmap='gray', vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
