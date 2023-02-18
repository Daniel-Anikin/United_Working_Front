import cv2
import sqlite3

sum_of_points_db = sqlite3.connect("sum_of_points.db")


def find_dicCon(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    T, thresh_img = cv2.threshold(blurred, 215, 255, cv2.THRESH_BINARY)
    cnts, _ = cv2.findContours(thresh_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return cnts


def find_pointSum(cnts):
    count = 0
    for i in range(0, len(cnts)):
        w, h = cv2.boundingRect(cnts[i])[2:]
        if 10 < w < 50 and 10 < h < 50:
            count += 1
    return count


if __name__ == '__main__':
    main_image = cv2.imread('../images/dices.jpg')
    gray_main_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    contours = find_dicCon(gray_main_image)
    pointSum = find_pointSum(contours)
    cur = sum_of_points_db.cursor()
    cur.execute(
        "insert into sum_table(result) values(?);", str(pointSum))
    sum_of_points_db.commit()
