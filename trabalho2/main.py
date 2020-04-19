from filters import *

def main(img_path, funtion):
    img = misc.imread(img_path)

    if filtro == "h1":
        h1(img)

    # path and name of the new image
    new_name = "output/1.3/" + img_path[4:-4] + '-' + function + ".png"

    # saving the new image
    plt.imsave(new_name, new_img, cmap='gray', vmin=0, vmax=255)

    plt.imshow(new_img, cmap='gray', vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main()