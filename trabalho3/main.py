import imageio
import matplotlib.pyplot as plt
import cv2
import numpy as np
from sys import argv

def read_args():
    k = 100
    if len(argv) == 3:
        k = int(argv[2])

    return argv[1], k


def main():
    # reading the image
    img_path, k = read_args()
    img = imageio.imread(img_path)


    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)


    # cria mascara passa baixa
    masklp = np.zeros((rows, cols, 2), np.uint8)
    r_lp = 10
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_lp * r_lp
    masklp[mask_area] = 1

    #cria mascara passa alta
    maskhp = np.ones((rows, cols, 2), np.uint8)
    r_hp = 90
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_hp * r_hp
    maskhp[mask_area] = 0

    #cria mascara passa faixa
    maskbp = np.zeros((rows, cols, 2), np.uint8)
    r_out = 90
    r_in = 40
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                               ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
    maskbp[mask_area] = 1

    img_float32 = np.float32(img)

    dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    #espectro de Fourier
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]) + 1)

    #imagem apos inversa de fourier
    f_ishift = np.fft.ifftshift(dft_shift)
    img_FourierI = cv2.idft(f_ishift)
    img_FourierI = cv2.magnitude(img_FourierI[:, :, 0], img_FourierI[:, :, 1])
    img_FourierI -= img_FourierI.min()
    img_FourierI = img_FourierI*255/img_FourierI.max()
    img_FourierI = img_FourierI.astype(np.uint8)


    # nucleo passa baixa
    fshift = dft_shift * masklp
    fshift_mask_mag_lp = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]) + 1)

    # imagem passa baixa
    f_ishift = np.fft.ifftshift(fshift)
    img_pb = cv2.idft(f_ishift)
    img_pb = cv2.magnitude(img_pb[:, :, 0], img_pb[:, :, 1])
    img_pb -= img_pb.min()
    img_pb = img_pb*255/img_pb.max()
    img_pb = img_pb.astype(np.uint8)

    # nucleo passa alta
    fshift = dft_shift * maskhp
    fshift_mask_mag_hp = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]) + 1)

    # imagem passa alta
    f_ishift = np.fft.ifftshift(fshift)
    img_hb = cv2.idft(f_ishift)
    img_hb = cv2.magnitude(img_hb[:, :, 0], img_hb[:, :, 1])
    img_hb -= img_hb.min()
    img_hb = img_hb*255/img_hb.max()
    img_hb = img_hb.astype(np.uint8)

    # nucleo passa faixa
    fshift = dft_shift * maskbp
    fshift_mask_mag_bp = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]) + 1)

    # imagem passa faixa
    f_ishift = np.fft.ifftshift(fshift)
    img_bb = cv2.idft(f_ishift)
    img_bb = cv2.magnitude(img_bb[:, :, 0], img_bb[:, :, 1])
    img_bb -= img_bb.min()
    img_bb = img_bb*255/img_bb.max()
    img_bb = img_bb.astype(np.uint8)




    #imprimindo e salvando imagens
    plt.figure(figsize=(10, 10))
    imgname = 'Imagem original(512x512 pixels)'
    plt.subplot(3 , 3, 1), plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png', img, cmap='gray', vmin=0, vmax=255)

    imgname = 'espectro de Fourier'
    plt.subplot(3 , 3, 2), plt.imshow(magnitude_spectrum, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png', magnitude_spectrum, cmap='gray', vmin=0, vmax=255)

    imgname = 'Imagem apos inversa de Fourier'
    plt.subplot(3 , 3, 3), plt.imshow(img_FourierI, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png',img_FourierI, cmap='gray', vmin=0, vmax=255)

    imgname = 'núcleo do filtro passa-baixa'
    plt.subplot(3 , 3, 4), plt.imshow(fshift_mask_mag_lp, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png',fshift_mask_mag_lp, cmap='gray', vmin=0, vmax=255)

    imgname = 'núcleo do filtro passa-alta'
    plt.subplot(3 , 3, 5), plt.imshow(fshift_mask_mag_hp, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png',fshift_mask_mag_hp, cmap='gray', vmin=0, vmax=255)

    imgname ='núcleo do filtro passa-faixa'
    plt.subplot(3 , 3, 6), plt.imshow(fshift_mask_mag_bp, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png',fshift_mask_mag_bp, cmap='gray', vmin=0, vmax=255)

    imgname ='imagem passa-baixa'
    plt.subplot(3 , 3, 7), plt.imshow(img_pb, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png',img_pb, cmap='gray', vmin=0, vmax=255)

    imgname ='imagem passa-alta'
    plt.subplot(3 , 3, 8), plt.imshow(img_hb, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png',img_hb, cmap='gray', vmin=0, vmax=255)

    imgname ='imagem passa-faixa'
    plt.subplot(3 , 3, 9), plt.imshow(img_bb, cmap='gray', vmin=0, vmax=255)
    plt.title(imgname), plt.xticks([]), plt.yticks([])
    plt.imsave('output/' + imgname + '.png',img_bb, cmap='gray', vmin=0, vmax=255)

    plt.show()


if __name__ == "__main__":
    main()