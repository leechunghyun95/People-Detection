from __future__ import print_function
from multiprocessing.dummy import Array
import cv2 as cv
import argparse


def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    print('정면 및 눈 검출')
    faces = face_cascade.detectMultiScale(frame_gray)
    print('faces',faces)
    if len(faces) != 0:
        print('faces',faces) 
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    
    # 측면 얼굴 검출
    print('측면얼굴 검출')
    face_profile = face_profile_cascade.detectMultiScale(frame_gray)
    print('face_profile',face_profile)
    for (x,y,w,h) in face_profile:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255,0,255),4)
        faceROI = frame_gray[y:y+h, x:x+w]

    #-- In each face, detect eyes
    eyes = eyes_cascade.detectMultiScale(frame_gray)
    print('eyes',eyes)
    for  (x,y,w,h) in eyes:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255,0,255),4)
        faceROI = frame_gray[y:y+h, x:x+w]

    # f2 = cv.resize(frame,(500,500))
    cv.imshow('Capture - Face detection', frame)
    cv.waitKey(0) == 27


# argparse.ArgumentParser를 통해 실행할 때 인자값 전달할 수 있음
# 필수값 x니까 인자값 전달 안해도 되고, 인자값 전달 안하면 디폴트값이 저장됨
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial')
# 얼굴 정면 인식
parser.add_argument('--face_cascade', help='Path to face cascade.' ,default='data/haarcascades/haarcascade_frontalface_alt.xml')
# 얼굴 측면 인식
parser.add_argument('--face_profile_cascade', help='Path to face profile cascade.', default='data/haarcascades/haarcascade_profileface.xml')
# 눈 인식
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
# args 변수에 인자값 저장
args = parser.parse_args()

# args변수에서 xml파일이름 가져오기
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade

# 얼굴 측명 args 변수에서 xml파일 이름 가져오기
face_profile_name = args.face_profile_cascade

face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

face_profile_cascade = cv.CascadeClassifier()


if not face_cascade.load(face_cascade_name):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(eyes_cascade_name):
    print('--(!)Error loading eyes cascade')
    exit(0)

if not face_profile_cascade.load(face_profile_name):
    print('--(!)Error loading face profile cascade')
    exit(0)

camera_device = args.camera

# -- 2. Read the video stream
# cap = cv.VideoCapture(camera_device)
# if not cap.isOpened:
#     print('--(!)Error opening video capture')
#     exit(0)
# while True:
#     ret, frame = cap.read()
#     if frame is None:
#         print('--(!) No captured frame -- Break!')
#         break
#     detectAndDisplay(frame)
#     if cv.waitKey(10) == 27:
#         break

image = cv.imread('img/2.png')
image = cv.resize(image,(500,500))
detectAndDisplay(image)

