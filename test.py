import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('girl.jpg')


def resizing(new_width=None, new_height=500, interp=cv2.INTER_LINEAR):
    h, w = img.shape[:2]

    if new_width is None and new_height is None:
        return img

    if new_width is None:
        ratio = new_height / h
        dimension = (int(w * ratio), new_height)

    else:
        ratio = new_width / w
        dimension = (new_width, int(h * ratio))

    res_img = cv2.resize(img, dimension, interpolation=interp)
    cv2.imshow('girl', res_img)
    cv2.waitKey(0)


def shifting():
    h, w = img.shape[:2]
    translation_matrix = np.float32([[1, 0, 200], [0, 1, 300]])
    dst = cv2.warpAffine(img, translation_matrix, (w, h))
    cv2.imshow('girl', dst)
    cv2.waitKey(0)


def loading_displaying_saving():
    print("Высота:" + str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    (b, g, r) = img[300, 300]
    print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))
    img[300, 300] = (255, 0, 0)
    (b, g, r) = img[300, 300]
    print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))
    cv2.imshow('girl', img)
    cv2.waitKey(0)
    cv2.imwrite('graygirl.jpg', img)


def cropping():
    crop_img = img[10:450, 300:750]
    cv2.imshow('girl', crop_img)
    cv2.waitKey(0)


def rotation():
    (h, w) = img.shape[:2]
    center = (int(w / 2), int(h / 2))
    rotation_matrix = cv2.getRotationMatrix2D(center, -45, 0.6)
    rotated = cv2.warpAffine(img, rotation_matrix, (w, h))
    cv2.imshow('girl', rotated)
    cv2.waitKey(0)


rotation()

