
import cv2
import numpy as np

def pic():
    cap=cv2.VideoCapture(0)

    while(True):
        ret,frame = cap.read()
        cv2.imshow('webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('y'):
            cv2.imwrite('/home/sreeram/Documents/OpenCV/c1.png',frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    return

def Main():
    pic()
    image= cv2.imread('/home/sreeram/Documents/OpenCV/c1.png')
    cv2.imshow('Image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Main()



