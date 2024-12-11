import cv2 as cv
import serial
import time

arduino = serial.Serial("COM5",9600)
time.sleep(2)

haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
capture = cv.VideoCapture(0)

angle = 90
threshold = 3

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("Failed to read frame from camera.")
        break
    
    if isTrue:
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
        
        if len(faces) > 0:
            x,y,w,h = faces[0]
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv.circle(frame,((x+w//2),(y+h//2)),2,(0,255,0),thickness=2)
            new_angle = int(((x+w//2)*180)/frame.shape[1])

            if abs(angle - new_angle) > 10 :
                angle = new_angle
                print(angle)
                arduino.write(f"{angle}\n".encode())



        # cv.imshow("Gray video",gray)
        cv.imshow("Video",frame)
    
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
