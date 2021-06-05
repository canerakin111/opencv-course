import cv2 as cv

# img = cv.imread('opencv-course/Resources/Photos/cat_large2.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # This will work for images, videos and live video
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # only works for live video, DOESNT WORK for stand alone videos
    capture,set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('opencv-course/resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()  # This will return frame by frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):  # if the letter d pressed, break out the loop
        break
capture.release()
cv.destroyAllWindows()