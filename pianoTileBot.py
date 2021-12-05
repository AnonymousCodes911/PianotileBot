

from pyautogui import * 
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
'''
these are the co-ordinates wrt to my machine change them at your will while in you machine
P1 X:  376 Y:  600 RGB: ( 88,  90, 117)
P2 X:  452 Y:  600 RGB: ( 82,  85, 116)
P3 X:  537 Y:  600 RGB: ( 78,  81, 115)
P4 X:  634 Y:  600 RGB: ( 84,  86, 116)
'''

def Mouseclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('y') == False :

    if pyautogui.pixel(376,600)[0] ==0: 

        Mouseclick(376,600)
    if pyautogui.pixel(452,600)[0] ==0: 
        Mouseclick(452,600)
    if pyautogui.pixel(537,600)[0] ==0: 
        Mouseclick(537,600)
    if pyautogui.pixel(634,600)[0] ==0: 
        Mouseclick(634,600)
