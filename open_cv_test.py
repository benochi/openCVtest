import cv2

capture = cv2.VideoCapture(0) #can pass in filename.avi as example. 

while(True):#if using file use cap.isOpened() instead of True
    ret, frame = capture.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('cvtest', frame)#use gray for grayscale

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
