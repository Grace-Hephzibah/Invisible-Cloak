import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()

    if success:
        cv2.imshow("Image", img)

        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite("Background.jpg", img)
            break

cap.release()
cv2.destroyAllWindows()