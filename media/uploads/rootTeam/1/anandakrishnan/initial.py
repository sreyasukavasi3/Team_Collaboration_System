import cv2
import numpy as np

#1
img = cv2.imread('bubblingFish.jpg')
imgCopy = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(imgray, 20, 255, 0)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow("countour",img)
cv2.imwrite("bubbleFishResult.jpg",img)
contours.remove(contours[0])
contours = max(contours, key=cv2.contourArea)
cv2.drawContours(imgCopy, contours, -1, (0,255,0), 3)
cv2.imshow("maxCountour",imgCopy)
cv2.imwrite("bubbleFishMaxResult.jpg",imgCopy)
cv2.waitKey(0)
cv2.destroyAllWindows()

#2
img = cv2.imread('polygons.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(imgray, 200, 255, 0)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
	poly=cv2.approxPolyDP(contour, 0.2*cv2.arcLength(contour, True), True)
	if len(poly) == 3:
		cv2.drawContours(img, contour, -1, (0,0,0), 3)
cv2.imshow("countour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("polygonsResult.jpg",img)

#3
import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret, binary = cv2.threshold(gray, 75, 255, 0)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
# cv2.imshow("bin",edges)
minLineLength = 100
maxLineGap = 50
lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=135,minLineLength=minLineLength,maxLineGap=maxLineGap)
for line in lines:
	for x1,y1,x2,y2 in line:
	    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imwrite('sudokuResult.jpg',img)
cv2.imshow("sudokuResult",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
