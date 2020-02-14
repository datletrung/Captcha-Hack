import cv2

img = cv2.imread("test3.png")

def increaseBrightness(img, value):
    global v
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    '''
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    '''
    v.fill(255)
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

#img = increaseBrightness(img, 255)

cascade = cv2.CascadeClassifier('haar.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
fragment = cascade.detectMultiScale(gray)
for (x,y,w,h) in fragment:
    if w <= 100 and h <= 100:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow("",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
