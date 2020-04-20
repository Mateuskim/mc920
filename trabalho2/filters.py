import numpy as np
import cv2


def get_matrix(s):
    return filter_matrix[s]


def apply_filter(img, f):

    #if the filter exist
    if f in filter_matrix:
        print(get_matrix(f))
        print(cv2.filter2D(img, -1, get_matrix(f)))
        return cv2.filter2D(img, -1, get_matrix(f))

    elif f == 'h9':
        img3 = np.square(cv2.filter2D(img, -1, get_matrix('h3')))
        img4 = np.square(cv2.filter2D(img, -1, get_matrix('h4')))
        return np.sqrt(img3 + img4)


    else:
        print("filtro não existente")
        return False


h1 = np.array(([0, 0, -1, 0, 0],
               [0, -1, -2, -1, 0],
               [-1, -2, 16, -2, -1],
               [0, -1, -2, -1, 0],
               [0, 0, -1, 0, 0]), dtype='int')
h2 = np.array(([1, 4, 6, 4, 1],
               [4, 16, 24, 16, 4],
               [4, 24, 36, 24, 6],
               [4, 16, 24, 16, 4],
               [1, 4, 6, 4, 1]), dtype=np.float32)/256

h3 = np.array(([-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]), dtype='int')
h4 = np.array(([-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]), dtype='int')
h5 = np.array(([-1, -1, -1],
               [-1, 8, -1],
               [-1, -1, -1]), dtype='int')
h6 = np.array(([1, 1, 1],
               [1, 1, 1],
               [1, 1, 1]),  dtype=np.float32)/9
h7 = np.array(([-1, -1, 2],
               [-1, 2, -1],
               [2, -1, -1]), dtype='int')
h8 = np.array(([2, -1, -1],
               [-1, 2, -1],
               [-1, -1, 2]), dtype='int')

filter_matrix = {
    "h1": h1,
    "h2": h2,
    "h3": h3,
    "h4": h4,
    "h5": h5,
    "h6": h6,
    "h7": h7,
    "h8": h8
}
