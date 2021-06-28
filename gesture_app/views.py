

from django.shortcuts import redirect, render
import cv2
import os
import numpy as np
import math
import pyautogui as pg
from . import HandTrackingModule as htm  

########################
brushThickness =15
eraserThickness =100
########################
# Create your views here.
def index(request):
    return render(request, "HomePage.html")



def Navigate_Vedio(request):
    pg.hotkey('winleft')
    pg.sleep(1)
    pg.typewrite('Movies\n',0.4)
    pg.press('enter')
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):

        ret ,img = cap.read()

        cv2.rectangle(img, (300,300),(100,100), (0,255,0),0)
        crop_img = img[100:300, 100:300]

        grey = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)

        value = (35,35)
        blurred = cv2.GaussianBlur(grey,value,0)

        _, thresh1 = cv2.threshold(blurred,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        cv2.imshow('thresholded',thresh1)

        (version, _, _) = cv2.__version__.split('.')

        if version == '3':
            image,contours,hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_NONE)
        elif version == '4':
            contours,hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_NONE)

        cnt = max(contours, key=lambda x: cv2.contourArea(x))

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(crop_img,(x,y), (x+w, y+h), (0,0,255),0)

        hull = cv2.convexHull(cnt)

        drawing = np.zeros(crop_img.shape,np.uint8)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
        cv2.drawContours(drawing,[hull],0,(0,255,0),0)

        hull = cv2.convexHull(cnt, returnPoints=False)

        defects = cv2.convexityDefects(cnt,hull)
        count_defects = 0
        cv2.drawContours(thresh1,contours,-1,(0,255,0),3)


        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]


            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            #Cosin Rule
            
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57


            if angle < 90:
                count_defects += 1
                cv2.circle(crop_img,far,3,[0,0,255],-1)
            
            cv2.line(crop_img,start,end,[0,255,0], 2)
        
        if count_defects == 1:
            pg.press("space",interval=1)              
            cv2.putText(img, "Play/Pause", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 10)
            
        
        elif count_defects == 2:
            pg.press("volumeup")
            cv2.putText(img, "Volume Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 10)
            
        elif count_defects == 3:
            pg.press("volumedown")
            cv2.putText(img, "Volume Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 10)  

        elif count_defects == 4:
            pg.press("volumemute",interval=1)
            cv2.putText(img, "Mute/Unmute", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 10)

        else:
            cv2.putText(img,"NONE",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,10)
            

        cv2.imshow("Gesture", img)
        all_img = np.hstack((drawing, crop_img))
        cv2.imshow("Contours", all_img)

        #Help Window
        path = r'F:\Final Year Project\Hand Gesture3\help-vedio.jpg'
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
    
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret ,img = cap.read()

        cv2.rectangle(img, (300,300),(100,100), (0,255,0),0)
        crop_img = img[100:300, 100:300]

        grey = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)

        value = (35,35)
        blurred = cv2.GaussianBlur(grey,value,0)

        _, thresh1 = cv2.threshold(blurred,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        cv2.imshow('thresholded',thresh1)

        (version, _, _) = cv2.__version__.split('.')

        if version == '3':
            image,contours,hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        elif version == '4':
            contours,hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            

        cnt = max(contours, key=lambda x: cv2.contourArea(x))

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(crop_img,(x,y), (x+w, y+h), (0,0,255),0)

        hull = cv2.convexHull(cnt)

        drawing = np.zeros(crop_img.shape,np.uint8)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
        cv2.drawContours(drawing,[hull],0,(0,255,0),0)

        hull = cv2.convexHull(cnt, returnPoints=False)

        defects = cv2.convexityDefects(cnt,hull)
        count_defects = 0
        cv2.drawContours(thresh1,contours,-1,(0,255,0),3)

        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]


            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            #Cosin Rule
            
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57


            if angle < 90:
                    count_defects += 1
                    cv2.circle(crop_img,far,3,[0,0,255],-1)

            cv2.line(crop_img,start,end,[0,255,0], 2)
        if count_defects == 1:
            pg.press("left",interval=0.5)              
            cv2.putText(img, "Left", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 10)
        elif count_defects == 2:
            pg.press("right",interval=0.5)              
            cv2.putText(img, "Right", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 10)
        elif count_defects == 3:
            cv2.putText(img, "Escape", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 10)
            pg.press('sleep',interval=1)
            pg.press("esc")
            break
        
        else:
            cv2.putText(img,"NONE",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,2)
            

        cv2.imshow("Gesture", img)
        all_img = np.hstack((drawing, crop_img))
        cv2.imshow("Contours", all_img)
        #Help Window
        path = r'F:\Final Year Project\Hand Gesture3\help-presentation.jpg'
        image = cv2.imread(path)
        help = 'image'
        cv2.resizeWindow(help,240,289)
        cv2.imshow(help, image)   


        key = cv2.waitKey(10) & 0xFF    
        if key == 27: 
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
        # windowWidth=img.shape[1]
        # windowHeight=img.shape[0]
        # print(windowWidth)
        # print(windowHeight)

        # 2. Find Hand Landmarks
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList)!=0:
        
            # print(lmList)

            # tip of index and middle fingers
            x1,y1 = lmList[8][1:]
            x2,y2 = lmList[12][1:]

            # 3. Check which fingers are up
            fingers = detector.fingersUp()
            # print(fingers)


            # 4. If selection Mode - 2 fingers are up
            if fingers[1] and fingers[2]:
                xp,yp =0,0
                # print("Selection Mode")
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

        if cv2.waitKey(5) == 13:  # if I press Enter it will break 
            break
    cap.release()
    cv2.destroyAllWindows()
    return redirect('index')
