import cv2
import numpy as np

cap = cv2.VideoCapture(0)

count = 0
background = 0

for i in range(60):
    success, bg = cap.read()
background = np.flip(bg, axis=1)


while (cap.isOpened()):

    success, img = cap.read()
    if not success:
        break
    count += 1
    img = np.flip(img, axis=1)


    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    ## Open and Dilate the mask image
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    ## inverted mask
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img, img, mask=mask2)
    res2 = cv2.bitwise_and(background, background, mask=mask1)

    finalOutput = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow("magic", finalOutput)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()