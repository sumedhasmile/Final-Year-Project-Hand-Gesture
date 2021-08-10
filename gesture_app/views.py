

from django.shortcuts import redirect, render
import cv2
import os
import numpy as np
import pyautogui as pg
from . import HandTrackingModule as htm  

########################
brushThickness =10
eraserThickness =100
wCam,hCam = 640,480
########################
# Create your views here.
def index(request):
    return render(request, "index.html")



def Navigate_Vedio(request):
    pTime =0
    pg.hotkey('winleft')
    pg.sleep(1)
    pg.typewrite('Movies\n',0.4)
    pg.press('enter')
    cap=cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)



    folderPath = "F:\Final Year Project\Hand-Gesture-Web\hand_gesture_app\gesture_app\FingerImages"
    myList = os.listdir(folderPath)
    overlayList =[]
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)
    print(len(overlayList))

    detector = htm.handDetector(detectionCon=0.75)
    
    tipIds = [4,8,12,16,20]
    while True:
        success,img =cap.read()
        # img = cv2.flip(img,1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img,draw=False)
    

        if len(lmList) != 0:
            fingers = []


            #Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                    fingers.append(1)
            else:
                    fingers.append(0)

            # 4 fingers

            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # print(fingers)      
            totalFingers = fingers.count(1) 
            print(totalFingers)

            h,w,c = overlayList[totalFingers-1].shape
            img[0:h,0:w] = overlayList[totalFingers-1] 

            if totalFingers == 1:
                pg.press("space",interval=1)              
                cv2.putText(img, "Play/Pause",(400,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0), 3)
        
            elif totalFingers == 2:
                pg.press("volumeup")
                cv2.putText(img, "Volume Up",(400,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0), 3)

            elif totalFingers == 3:
                pg.press("volumedown")
                cv2.putText(img, "Volume Down",(400,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0), 3)


            elif totalFingers == 4:
                pg.press("volumemute",interval=1)
                cv2.putText(img, "Mute/Unmute",(400,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0), 3)

            else:
                cv2.putText(img,"NONE",(400,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),10)
        
        cv2.imshow("Image",img)
        #Help Window
        path = r'F:\Final Year Project\Hand-Gesture-Web\hand_gesture_app\gesture_app\Header\help-vedio.jpg'
        image = cv2.imread(path)
        help = 'image'
        cv2.resizeWindow(help,247,349)
        cv2.imshow(help, image)

        

        if cv2.waitKey(5) == 13:  # if I press Enter it will break 
            break
    cap.release()
    cv2.destroyAllWindows()
    return redirect('index')

def Navigate_Player(request):
    pg.hotkey('winleft')
    pg.sleep(1)
    pg.typewrite('PowerPoint\n',0.5)
    pg.press('enter')
    
    cap=cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)


    folderPath = "F:\Final Year Project\Hand-Gesture-Web\hand_gesture_app\gesture_app\FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList =[]
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)
    print(len(overlayList))

    detector = htm.handDetector(detectionCon=0.75)


    tipIds = [4,8,12,16,20]
    while True:
        success,img =cap.read()
        # img = cv2.flip(img,1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img,draw=False)
    

        if len(lmList) != 0:
            fingers = []


            #Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                    fingers.append(1)
            else:
                    fingers.append(0)

            # 4 fingers

            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # print(fingers)      
            totalFingers = fingers.count(1) 
            print(totalFingers)

            h,w,c = overlayList[totalFingers-1].shape
            img[0:h,0:w] = overlayList[totalFingers-1] 

            if totalFingers == 1:
                pg.press("left",interval=0.5)              
                cv2.putText(img, "Left",(400,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0), 3)
        
            elif totalFingers == 2:
                pg.press("right",interval=0.5)
                cv2.putText(img, "Right",(400,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0), 3)

            elif totalFingers == 3:
                cv2.putText(img, "Escape",(400,70), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0), 3)
                pg.press("sleep",interval=1)
                pg.press("esc")
                break

            else:
                cv2.putText(img,"NONE",(400,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),10)

        #Help Window
        path = r'F:\Final Year Project\Hand-Gesture-Web\hand_gesture_app\gesture_app\Header\help-presentation.jpg'
        image = cv2.imread(path)
        help = 'image'
        cv2.resizeWindow(help,240,289)
        cv2.imshow(help, image)
        cv2.imshow("Image",img)

        if cv2.waitKey(5) == 13:  # Press enter to close window 
            break
    cap.release()
    cv2.destroyAllWindows()        
    return redirect('index')

def PaintWindow(request):

    folderPath = "F:\Final Year Project\Hand-Gesture-Web\hand_gesture_app\gesture_app\Header"
    myList = os.listdir(folderPath)
    # print(myList)
    overlayList =[]
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)
    # print(len(overlayList))
    header = overlayList[0]

    drawColor = (0,0,255)

    cap = cv2.VideoCapture(0)
    cap.set(3,900)
    cap.set(4,720)

    detector = htm.handDetector(detectionCon=0.85)
    xp,yp=0,0
    imgCanvas = np.zeros((480,640,3),np.uint8)

    while True:
        # 1. Import Image
        success,img = cap.read()
        img = cv2.flip(img,1)

        # 2. Find Hand Landmarks
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList)!=0:
        

            # tip of index and middle fingers
            x1,y1 = lmList[8][1:]
            x2,y2 = lmList[12][1:]

            # 3. Check which fingers are up
            fingers = detector.fingersUp()


            # 4. If selection Mode - 2 fingers are up
            if fingers[1] and fingers[2]:
                xp,yp =0,0

                #Checking for the click
                if y1 < 120:
                    if 100<x1<200:
                        header = overlayList[0]
                        drawColor= (0,0,255) #red
                    elif 250<x1<350:
                        header = overlayList[1]
                        drawColor= (0,165,255) #orange
                    elif 400<x1<500:
                        header = overlayList[2]
                        drawColor = (255,0,0) #blue
                    elif 500<x1<639:
                        header = overlayList[3]
                        drawColor = (0,0,0) #eraser
                cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)

            # 5. If Drawing Mode - Index finger is up

            if fingers[1] and fingers[2] == False:
                cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
                # print("Drawing Mode")
                if xp==0 and yp==0:
                    xp,yp = x1,y1

                if drawColor ==(0,0,0):
                    cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness)
                    cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
                else:  
                    cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
                    cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)

                xp,yp = x1,y1
    
        imgGray = cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)        
        imgInv =cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img,imgInv)
        img = cv2.bitwise_or(img,imgCanvas)

        #setting the header image
        img[0:120,0:639]=header
        cv2.imshow("Image",img)
        cv2.imshow("Canvas",imgCanvas)

        #Help Window
        path = r'F:\Final Year Project\Hand-Gesture-Web\hand_gesture_app\gesture_app\Header\help-paint.jpg'
        image = cv2.imread(path)
        help = 'image'
        cv2.resizeWindow(help,295,273)
        cv2.imshow(help, image)

        if cv2.waitKey(5) == 13:  # if I press Enter it will break 
            break
    cap.release()
    cv2.destroyAllWindows()
    return redirect('index')


def Home(request):
    return render(request,'index.html')