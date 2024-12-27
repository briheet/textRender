#!/usr/bin/env python3

import cv2 as cv
import sys

sample = "wallhaven-kxy7j6.jpg"
font = cv.FONT_HERSHEY_SIMPLEX
distance = 10

def start():
    img = cv.imread(cv.samples.findFile(sample))
    if img is not None:
        img = cv.resize(img, (1000, 540))

    if img is None:
        sys.exit("No such image")

    i = 10
    while True:
        cv.imshow("Display", img)

        k = cv.waitKey(33)
        if k == 27:
            break
        elif k == -1:
            continue
        else:
            print(k)
            cv.putText(img, 'Distance: {}'.format(distance), (i, 50), font, 3, (0, 255, 0), 2, cv.LINE_AA)

    cv.waitKey(0)
    cv.destroyAllWindows()


def main():
    start() # This continues to work until the window is closed
    print("Hi")


if __name__ == "__main__":
    main()
