import cv2
import numpy as np

original =cv2.imread("")
cv2.imshow("original",original)
#显示图片某个颜色通道的图像
blue =np.zeros_like(original)
blue[:,:,0] =original[:,:,0]
cv2.imshow('blue',blue)
green =np.zeros_like(original)
green[:,:,1] = original[:,:,1]
cv2.imshow('Green',green)
red =np.zeros_like(original)
red[:,:,2] =original[:,:,2]
cv2.imread("red",red)
#图像裁剪
h,w =original.shape[:2]
l ,t =int(w/4),int(h/4)
r,b =int(w*3/4),int(h*3/4)
cropped =original[t:b,l:r]
cv2.imshow("Cropped",cropped)
#图像缩放 interpolation =线性插值
scaled1 =cv2.resize(original,(int(w/4),int(h/4)),interpolation=cv2.INTER_LINEAR)
cv2.imshow('Scaled1',scaled1)
scaled2 =cv2.resize(scaled1,None,fx=4,fy=4,interpolation=cv2.INTER_LINEAR)
cv2.imshow("Scaled2",scaled2)
cv2.waitKey()
#图像文件保存
cv2.imwrite('',blue)
cv2.imwrite("",green)
cv2.imwrite("",red)
cv2.imwrite("",cropped)
cv2.imwrite("",scaled1)
cv2.imwrite("",scaled2)






