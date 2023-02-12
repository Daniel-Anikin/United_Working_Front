import cv2
import sqlite3

count = 0
sum_of_points_db = sqlite3.connect("sum_of_points.db")


def find_contours_of_dices_and_points(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    T, thresh_img = cv2.threshold(blurred, 215, 255, cv2.THRESH_BINARY)
    cnts, _ = cv2.findContours(thresh_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return cnts


def find_sum_of_points(cnts):
    global count
    for i in range(0, len(cnts)):
        x, y, w, h = cv2.boundingRect(cnts[i])
        if 10 < w < 50 and 10 < h < 50:
            count += 1


if __name__ == '__main__':
    main_image = cv2.imread('images/dices.jpg')
    gray_main_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    contours = find_contours_of_dices_and_points(gray_main_image)
    find_sum_of_points(contours)
    cur = sum_of_points_db.cursor()
    cur.execute(
        "insert into sum_table(result) values(?);", str(count))
    sum_of_points_db.commit()
