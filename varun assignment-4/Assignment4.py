import cv2

image_original = cv2.imread(r"C:\Users\udayn\OneDrive\Desktop\PYTHONFILES\DIP\Virat-Kohli-2.jpg")
img_red = cv2.imread(r"C:\Users\udayn\OneDrive\Desktop\PYTHONFILES\DIP\Virat-Kohli-2.jpg")
img_green = cv2.imread(r"C:\Users\udayn\OneDrive\Desktop\PYTHONFILES\DIP\Virat-Kohli-2.jpg")
img_blue = cv2.imread(r"C:\Users\udayn\OneDrive\Desktop\PYTHONFILES\DIP\Virat-Kohli-2.jpg")

img_blue[:,:,1],img_blue[:,:,2] = 0,0
img_green[:,:,0],img_green[:,:,2] = 0,0           
img_red[:,:,0],img_red[:,:,1] = 0,0

cv2.imshow("Original Image",image_original)
cv2.waitKey(0)
cv2.imshow("Reddish Image",img_red)
cv2.waitKey(0)
cv2.imshow("Greenish Image",img_green)
cv2.waitKey(0)
cv2.imshow("Blueish Image",img_blue)
cv2.waitKey(0)