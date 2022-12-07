import cv2 as cv

capture = cv.VideoCapture('videos/glasses.gif')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Demo', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
