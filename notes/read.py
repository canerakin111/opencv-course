# This will read a photo and open in a window

import cv2 as cv

# img = cv.imread('opencv-course/Resources/Photos/cat_large.jpg')

# cv.imshow('cat', img)

# cv.waitKey(0)

capture = cv.VideoCapture('opencv-course/resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()  # This will return frame by frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):  # if the letter d pressed, break out the loop
        break
capture.release()
cv.destroyAllWindows()
