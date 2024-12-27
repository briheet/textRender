#!/usr/bin/env python3

import cv2 as cv
import sys

def start():
    img = cv.imread(cv.samples.findFile("wallhaven-kxy7j6.jpg"))
    if img is not None:
        img = cv.resize(img, (1000, 540))

    if img is None:
        sys.exit("No such image")

    cv.imshow("Display window", img)

    cv.waitKey(0)

    cv.destroyAllWindows()


def main():
    start() # This continues to work until the window is closed
    print("HI")


if __name__ == "__main__":
    main()
