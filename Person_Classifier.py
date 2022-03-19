# 입력받은 이미지에서 사람을 검출하고 있으면 True 없으면 False를 리턴한다.
# 하나라도 True가 되면 나머지 실행하지 않고 다음 이미지로 넘어감
# False인 이미지(사람 검출 x) 파일들 이름만 리스트에 담아서 리턴한다.
import cv2 as cv
import argparse

isPersonList = list()

# 이미지에서 사람 검출하는 메서드
def detectPerson(image):
    # 이미지 그레이스케일로 변환
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 히스토그램 평활화
    image_gray = cv.equalizeHist(image_gray)

    # 사람이미지인지 아닌지 담는 변수
    isPerson = False

    # 얼굴 정면 검출
    faces = face_cascade.detectMultiScale(image_gray)
    if len(faces) != 0:
        isPerson = True
        print('얼굴 정면 검출')
        isPersonList.append(path)
        # return

    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        image = cv.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = image_gray[y:y+h,x:x+w]
    
    # 얼굴 측면 검출
    profilefaces = profileface_cascade.detectMultiScale(image_gray)
    if len(profilefaces) != 0:
        isPerson = True
        print('얼굴 측면 검출')
        isPersonList.append(path)
        # return
    
    # for (x,y,w,h) in profilefaces:
    #     center = (x + w//2, y + h//2)
    #     image = cv.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
    #     faceROI = image_gray[y:y+h,x:x+w]
    
    # 눈 검출
    eyes = eyes_cascade.detectMultiScale(image_gray)
    if len(eyes) != 0:
        isPerson = True
        print('눈 검출')
        isPersonList.append(path)
        # return

    for (x,y,w,h) in eyes:
        center = (x + w//2, y + h//2)
        image = cv.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = image_gray[y:y+h,x:x+w]
    
    # 몸 전체 검출
    fullbodys = fullbody_cascade.detectMultiScale(image_gray)
    if len(fullbodys) != 0:
        isPerson = True
        print('몸 전체 검출')
        isPersonList.append(path)
        # return
    
    for (x,y,w,h) in fullbodys:
        center = (x + w//2, y + h//2)
        image = cv.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = image_gray[y:y+h,x:x+w]
    
    # 상체 검출
    upperbodys = upperbody_cascade.detectMultiScale(image_gray)
    if len(upperbodys) != 0:
        isPerson = True
        print('상체 검출')
        isPersonList.append(path)
        # return

    for (x,y,w,h) in upperbodys:
        center = (x + w//2, y + h//2)
        image = cv.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = image_gray[y:y+h,x:x+w]
    
    # 하체 검출
    lowerbodys = lowerbody_cascade.detectMultiScale(image_gray)
    if len(lowerbodys) != 0:
        isPerson = True
        print('하체 검출')
        isPersonList.append(path)
        # return

    for (x,y,w,h) in lowerbodys:
        center = (x + w//2, y + h//2)
        image = cv.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = image_gray[y:y+h,x:x+w]

    # if isPerson == True:
    #     print(path+'이미지는 사람입니다.')
    #     isPersonList.append(path)
    # else :
    #     print(path+'이미지는 사람이 아닙니다.')

    image = cv.resize(image, dsize=(0, 0), fx=2, fy=2, interpolation=cv.INTER_AREA)
    cv.imshow('Capture - Face detection', image)
    cv.waitKey(0) == 27


parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial')

# 얼굴 정면 인식 인자
parser.add_argument('--face_cascade', help='Path to face cascade.' ,default='data/haarcascades/haarcascade_frontalface_alt.xml')
# 얼굴 측면 인식 인자
parser.add_argument('--profileface_cascade', help='Path to face profile cascade.', default='data/haarcascades/haarcascade_profileface.xml')
# 눈 인식 인자
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
# 몸 전체 인식 인자
parser.add_argument('--fullbody_cascade', help='Path to fullbody cascade.', default='data/haarcascades/haarcascade_fullbody.xml')
# 상체 인식 인자
parser.add_argument('--upperbody_cascade', help='Path to upperbody cascade.', default='data/haarcascades/haarcascade_upperbody.xml')
# 하체 인식 인자
parser.add_argument('--lowerbody_cascade', help='Path to lowerbody cascade.', default='data/haarcascades/haarcascade_lowerbody.xml')

# 인자 파싱해서 args변수에 담기
args = parser.parse_args()

# args변수에서 xml 파일명 가져오기
face_cascade_name = args.face_cascade
profileface_cascade_name = args.profileface_cascade
eyes_cascade_name = args.eyes_cascade
fullbody_cascade_name = args.fullbody_cascade
upperbody_cascade_name = args.upperbody_cascade
lowerbody_cascade_name = args.lowerbody_cascade

# cv::CascadeClassifier를 만듬
face_cascade = cv.CascadeClassifier()
profileface_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
fullbody_cascade = cv.CascadeClassifier()
upperbody_cascade = cv.CascadeClassifier()
lowerbody_cascade = cv.CascadeClassifier()

# cv::CascadeClassifier::load함수로 xml파일 로드
# 로드 실패하면 에러메세지 출력
if not face_cascade.load(face_cascade_name):
    print('--(!)Error loading face cascade')
    exit(0)
if not profileface_cascade.load(profileface_cascade_name):
    print('--(!)Error loading face profile cascade')
    exit(0)
if not eyes_cascade.load(eyes_cascade_name):
    print('--(!)Error loading eyes cascade')
    exit(0)
if not fullbody_cascade.load(fullbody_cascade_name):
    print('--(!)Error loading face cascade')
    exit(0)
if not upperbody_cascade.load(upperbody_cascade_name):
    print('--(!)Error loading eyes cascade')
    exit(0)

if not lowerbody_cascade.load(lowerbody_cascade_name):
    print('--(!)Error loading face profile cascade')
    exit(0)


# import cv2
# import os

# def load_images_from_folder(folder):
#     images = []
#     for filename in os.listdir(folder):
#         images.append(filename)
    # return images


# files = load_images_from_folder('data/img')

# for filename in files:    
#     path = 'data/img/'+filename
#     print('path',path)
#     image = cv.imread(path)
#     image = cv.resize(image,dsize=(0, 0), fx=1, fy=1, interpolation=cv.INTER_AREA)
#     detectPerson(image)

path = 'data/img/people6.jpg'
image = cv.imread(path)
image = cv.resize(image,dsize=(0, 0), fx=1, fy=1, interpolation=cv.INTER_AREA)
detectPerson(image)

print('isPersonList',isPersonList)