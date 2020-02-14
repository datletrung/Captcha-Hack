import cv2
import time
import pyautogui
import numpy as np

button = 'img/button.png'
refresh = 'img/refresh.png'
cascade = cv2.CascadeClassifier('haar.xml')
wsize,hsize = pyautogui.size()

time.sleep(2)
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

loc = pyautogui.locateOnScreen(button)
if loc != None:
    loc = pyautogui.center(loc)
    while True:
        pyautogui.moveTo(loc)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        fragment = cascade.detectMultiScale(gray)
        if len(fragment) == 0:
            print("Cannot solve! Changing captcha...")
            locTemp = pyautogui.locateOnScreen(refresh)
            pyautogui.click(locTemp)
            pyautogui.moveTo(0,hsize//2)
            time.sleep(3)
            print("Trying again...")
            img = pyautogui.screenshot()
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            continue
        for (x,y,w,h) in fragment:
            center = (x + w//2, y + h//2)
            if w <= 120 and h <= 120 and center[0]-loc[0] > 85:
                
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                
                print("Captcha found! Solving...")
                pyautogui.dragTo(center[0]-25, loc[1], .5, button='left')
                print("Done!")
                break
        img = img[loc[1]-400:loc[1]+30, loc[0]-20:loc[0]+600]
        cv2.imshow("",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break
else:
    print("No captcha detected!")
