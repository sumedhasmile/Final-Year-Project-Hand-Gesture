from django.shortcuts import redirect, render
from django.http import HttpResponse
import pyautogui as pg
# Create your views here.
def index(request):
    return render(request, "HomePage.html")

def Navigate(request):
    pg.hotkey('winleft')
    pg.typewrite('Movies\n',0.2)
    pg.press('enter')
    
    
    # Open commmand prompt 
    pg.hotkey('winleft')
    pg.typewrite('Command\n',0.2)
    pg.press('enter')
    pg.write('f:\n',0.2)
    pg.write('cd F:\Final Year Project\Hand Gesture3\n',0.2)
    pg.write('python hand_gesture_youtube.py\n',0.2)
    return render(request,"HomePage.html")