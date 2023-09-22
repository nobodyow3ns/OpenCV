import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Take each frame
    _, frame = cap.read()
    
    canny=cv2.Canny(frame, 100,200)
    cv2.imshow('canny',canny)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of color in HSV
    lower= np.array([35,0,0]) #initially set everything to 0
    upper= np.array([70,255,255]) #initially set everything to 255
    #Hue 35-70 Green, using the Green Imperial Pennx Book
    
    # Threshold the HSV image to get only the range mentioned
    mask = cv2.inRange(hsv, lower, upper)
    #initially mask shows everything

    #make a numpy kernel of one with dimension 15x15
    #and datatype 32 bit float. 225 is 15*15
    kernel1 = np.ones((15,15), np.float32)/225
    
    #Median # Almost No noise. # A little blurred though
    median = cv2.medianBlur(mask,15)
    cv2.imshow('Median Blur', median)
     
    kernel2 = np.ones((5,5),np.uint8)
    #feeding the Median Blur masked image into dilation
    dilation = cv2.dilate(median, kernel2, iterations=1)

    final=cv2.bitwise_and(frame,frame,mask=dilation)
    finaledge = add(final+canny)
    
    cv2.imshow('frame',frame)
    cv2.imshow('Final filter',final)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    

cv2.destroyAllWindows()
cap.release()
