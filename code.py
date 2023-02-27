import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.VideoCapture(0)

while True:
    ret,frame=img.read()
    if ret ==False:
        continue

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray,20,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        # print(x,y)
        cv.circle(frame,(x,y),3,(0,0,255),-1)
    
    cv.imshow("frame 1",frame)
    if cv.waitKey(1)==27:
        break
img.release()
cv.destroyAllWindows()
plt.imshow(img),plt.show()


