import cv2 
framewidth = 800
frameheight = 480
color = (255,0,255)
faceCascade = cv2.CascadeClassifier("D:/pycharm/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 100)



while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img , (x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img, "face1",(x,y-5),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break