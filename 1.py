import math 
import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0) # 0 for default camera,
cap.set(3, 800) # Width 
cap.set(4, 600) # Height
detector = HandDetector(detectionCon=0.7, maxHands=1)

class SnakeGameAI:
   def __init__(self):
      self.points = [] # List of points to draw the snake
      self.length = [] # List of lengths of the snake
      self.currentLength = 0 # Current length of the snake
      self.allowedLength = 250 # Maximum length of the snake
      self.previousHead = 0,0 # Previous head position of the snake
   def update(self , imgMain , currentHead):
      px , py = self.previousHead
      cx ,cy = currentHead
      self.points.append([cx,cy])
      distance = math.hypot(cx - px , cy - py)
      self.length.append(distance)
      self.currentLength += distance
      self.previousHead = cx , cy
      # draw worm 
      if self.points :
         for i , point in enumerate(self.points):
            if i != 0 : 
               cv2.line(imgMain , self.points[i-1] , self.points[i] , (0,0,255,255), 2)
            cv2.circle(imgMain , self.points[-1] , 20 , (200,0,200),cv2.FILLED)
      return imgMain
game = SnakeGameAI()
while True:
   success , img = cap.read()
   img = cv2.flip(img , 1) 
   hands , img = detector.findHands(img, flipType=False) 
   if hands:
      lmList = hands[0]['lmList']
      pointIndex = lmList[8][0:2]
      #cv2.circle(img,pointIndex, 20, (200,0,200), cv2.FILLED)
      img = game.update(img,pointIndex)

   cv2.imshow("Snake Game python AI", img)
   key = cv2.waitKey(1) 

