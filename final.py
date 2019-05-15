import numpy
import argparse
import cv2
def sober(path):
    image = cv2.imread(path，newpath)
    #cv2.imshow("Original", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Gray", gray)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    sobelx = numpy.uint8(numpy.absolute(sobelx))
    sobely = numpy.uint8(numpy.absolute(sobely))
    sobelcombine = cv2.bitwise_or(sobelx,sobely)
    #display two images in a figure
        # cv2.imshow("Edge detection by Sobel", numpy.hstack([gray,sobelx,sobely, sobelcombine]))
    cv2.imwrite(newpath, numpy.hstack([gray,sobelx,sobely, sobelcombine]))

    # f(cv2.waitKey(0)==27):
    #     cv2.destroyAllWindows()

sober（'test1.tif'，'result/test1_edge_by_sobel.jpg'）
sober（'test2.png'，'result/test2_edge_by_sobel.jpg'）
sober（'test3.jpg'，'result/test3_edge_by_sobel.jpg'）
sober（'test4.bmp'，'result/test4_edge_by_sobel.jpg'）
sober（'test5.png'，'result/test5_edge_by_sobel.jpg'）
sober（'test6.jpg'，'result/test6_edge_by_sobel.jpg'）
    