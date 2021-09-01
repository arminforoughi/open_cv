import cv2 as cv
import numpy as np

#making a blank img
'''blank = np.zeros((500, 500, 3), dtype = 'uint8')

img = cv.imread('T.50 Press Release Image.jpg')
#cv.imshow('blank', blank)

blank[:] = 0, 255, 0'''


#cv.imshow('blank', blank)
#cv.imshow('car', img)
#making grayscale
'''gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#making blury
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)

#edge detection
canny = cv.Canny(img, 124, 124)
cv.imshow('car', canny)
cv.waitKey(0)'''


capture = cv.VideoCapture(0)
x= 0
while True:
    x +=1
    isture, frame = capture.read()
    if not isture:
        print('number of frames: {}'.format(x))
        break
    cv.rectangle(frame, (1,2),(10,20),(255,0,0),2)
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        bsreak

#capture.release()
#cv.destroyAllWindows()
#cv.waitKey(0)

#Documents/DSC/open_cv/
