import math                                
import numpy as np
import cv2

pic1 = np.zeros((512,512),np.uint8)        
pic2 = np.zeros((512,512),np.uint8)

pic1 = cv2.circle(pic1,(235,250),80,(255,255),-1)            
pic2 = cv2.rectangle(pic2,(100,300),(330,190),(255,255,255),-1)          


cv2.imshow("Image with white circle at center",pic1)
cv2.waitKey(0)
cv2.imshow("AND operation on images",cv2.bitwise_and(pic1,pic2))
cv2.waitKey(0)
cv2.imshow("NAND operation on images",cv2.bitwise_not(cv2.bitwise_and(pic1,pic2)))
cv2.waitKey(0)
cv2.imshow("OR operation on images",cv2.bitwise_or(pic1,pic2))
cv2.waitKey(0)
cv2.imshow("NOR operation on images",cv2.bitwise_not(cv2.bitwise_or(pic1,pic2)))
cv2.waitKey(0)
cv2.imshow("EXOR operation on images",cv2.bitwise_xor(pic1,pic2))
cv2.waitKey(0)
cv2.imshow("EXNOR operation on images",cv2.bitwise_not(cv2.bitwise_xor(pic1,pic2)))
cv2.waitKey(0)