import numpy as np
import cv2
import os
import mediapipe as mp
import time




def contour_faces(img,frame = 0):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    #img = cv2.imread(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 6)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 6)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Armin {}'.format(frame), (x+10, y+10), font, 1, (0, 255, 0), 2, cv2.LINE_AA, False)

    return faces


def contour_bymp(img):
    mpface = mp.solutions.face_detection

    face_detect = mpface.FaceDetection()

    mpdraw = mp.solutions.drawing_utils
    results = face_detect.process(img)
    if results.detections:
        for id, detect in enumerate(results.detections):
            box_pos = detect.location_data.relative_bounding_box

            mpdraw.draw_detection(img, detect)

    return


'''
to get the names with the most photos in the databse
goerge W bush, most common with 530 photos
Colin_Powell - 236
Tony_Blair - 144
'''
def get_top_names():
    directory = 'data/archive/lfw-deepfunneled/lfw-deepfunneled'
    first, fname = 0, None
    second, sname = 0, None
    third, tname = 0, None
    name = 'f'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        try:
            num = len(os.listdir(f))
            if first < num:
                third = second
                second = first
                first = num
                tname = sname
                second = fname
                fname = f
            elif second < num:
                third = second
                second = num
                tname = sname
                sname = f
            elif third < num:
                third = num
                tname = f
        except:
            continue
    print('first', first, fname)
    print('second', second, sname)
    print('third', third, tname)
    return



name_direct = 'data'

def detect(directory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        try:
            contour_faces(f)
        except:
            continue


def camera():
    capture = cv2.VideoCapture(0)
    x = 0
    while True:

        isture, frame = capture.read()
        contour_bymp(frame)
        #contour_faces(frame, x)
        x+=1
        cv2.imshow('video', frame)

        if cv2.waitKey(20) & 0xFF == ord('d'):
            break

def contour(x,y,w,h, img):

    return cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

camera()

'''img = cv2.imread('data/armin.jpg')
print(contour_faces(img))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
