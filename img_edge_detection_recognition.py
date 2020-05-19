"""边缘检测"""
import cv2
import numpy as np

original =cv2.imread("imag01.jpg")
cv2.Sobel(original,cv2.CV_64F,1,
0,ksize=5)
#cv2.CV_64F :卷积运算使用数据类型为64位浮点型
#1：水平方向是否索贝尔偏积分
#0：垂直方向是否索贝尔偏积分
#ksize :卷积核为5*5
#拉普拉斯边缘识别
cv2.Laplacian(original,cv2.CV_64F)
#Canny边缘识别
cv2.Canny(original,50,240)


im_data =cv2.imread('imag01.jpg',cv2.IMREAD_GRAYSCALE)
print(im_data.shape)
cv2.imshow('im_data',im_data)
# hsobel =cv2.Sobel(im_data,cv2.CV_64F,1,0,ksize=5)
# cv2.imshow('H-sobel',hsobel)
# vsobel =cv2.Sobel(im_data,cv2.CV_64F,0,1,ksize=5)
# cv2.imshow('V',vsobel)
sobel =cv2.Sobel(im_data,cv2.CV_64F,1,1,ksize=5)
cv2.imshow("sobel",sobel)
laplacian =cv2.Laplacian(im_data,cv2.CV_64F)
cv2.imshow("Laplacian",laplacian)
canny =cv2.Canny(im_data,50,240)
cv2.imshow('C',canny)
cv2.waitKey()







