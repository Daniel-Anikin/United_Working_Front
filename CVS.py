import cv2
import os

count = 0

def find_contours_of_cards(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    T, thresh_img = cv2.threshold(blurred, 215, 255, cv2.THRESH_BINARY)
    cnts, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return cnts


def find_coordinates_of_cards(cnts):
    global count
    for i in range(0, len(cnts)):
        x, y, w, h = cv2.boundingRect(cnts[i])
        print(w, h)
        if 10 < w < 160 and 10 < h < 160:
            count += 1


if __name__ == '__main__':
    main_image = cv2.imread('images/dices/main_image/dices.jpg')
    gray_main_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    contours = find_contours_of_cards(gray_main_image)
    find_coordinates_of_cards(contours)
    print(count)
