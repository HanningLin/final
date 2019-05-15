import numpy
import argparse
import cv2
def sober(path,newpath):
    image = cv2.imread(path)
    #cv2.imshow("Original", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Gray", gray)
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S
    sobelx=cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    sobely=cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    sobelx=cv2.convertScaleAbs(sobelx,sobelx)
    sobely=cv2.convertScaleAbs(sobely,sobely)
    grad = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    #display two images in a figure
        # cv2.imshow("Edge detection by Sobel", numpy.hstack([gray,sobelx,sobely, sobelcombine]))
    #cv2.imwrite(newpath, numpy.hstack([gray,sobelx,sobely, sobelcombine]))
    cv2.imwrite(newpath,grad)


def hough(path,newpath1,newpath2,Length,Gap,Length1,Gap1,num):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_back=img
    img1 = cv2.Canny(img, 50, 200, None, 3)
    cv2.imwrite('canny'+str(num)+'.jpg',img1)
    lines1 = cv2.HoughLinesP(img1, 1, numpy.pi / 180, 50, None, Length, Gap)
    #lines = cv2.HoughLinesP(img,1.0,numpy.pi/180,20,None,minLineLength,maxLineGap)
    lines1 = lines1[:,0,:]
    for x1,y1,x2,y2 in lines1[:]:
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
    cv2.imwrite(newpath2,img)


    scale = 1
    delta = 0
    ddepth = cv2.CV_16S
    sobelx=cv2.Sobel(img, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    sobely=cv2.Sobel(img, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    sobelx=cv2.convertScaleAbs(sobelx,sobelx)
    sobely=cv2.convertScaleAbs(sobely,sobely)
    grad = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    lines2 = cv2.HoughLinesP(grad, 1, numpy.pi / 180, 50, None, Length1, Gap1)
    #lines = cv2.HoughLinesP(img,1.0,numpy.pi/180,20,None,minLineLength,maxLineGap)
    lines2 = lines2[:,0,:]
    for x1,y1,x2,y2 in lines2[:]:
        cv2.line(img_back,(x1,y1),(x2,y2),(255,0,0),2)
    cv2.imwrite(newpath1,img_back)


sober('test1.tif','result/test1_edge_by_sobel.jpg')
sober('test2.png','result/test2_edge_by_sobel.jpg')
sober('test3.jpg','result/test3_edge_by_sobel.jpg')
sober('test4.bmp','result/test4_edge_by_sobel.jpg')
sober('test5.png','result/test5_edge_by_sobel.jpg')
sober('test6.jpg','result/test6_edge_by_sobel.jpg')
    
hough('test1.tif','result/test1_sobel_hough.jpg','result/test1_canny_hough.jpg',10,20,200,1,1)
hough('test2.png','result/test2_sobel_hough.jpg','result/test2_canny_hough.jpg',20,30,200,1,2)
hough('test3.jpg','result/test3_sobel_hough.jpg','result/test3_canny_hough.jpg',30,30,160,1,3)
hough('test4.bmp','result/test4_sobel_hough.jpg','result/test4_canny_hough.jpg',120,30,120,1,4)
hough('test5.png','result/test5_sobel_hough.jpg','result/test5_canny_hough.jpg',10,3,40,1,5)
hough('test6.jpg','result/test6_sobel_hough.jpg','result/test6_canny_hough.jpg',100,3,400,1,6)



