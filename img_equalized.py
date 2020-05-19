"""直方图均衡化"""
import cv2

original =cv2.imread('imag01.jpg')
cv2.imshow('Orignial',original)
# gray =cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray',gray)
# equalized_gray =cv2.equalizeHist(gray)
# cv2.imshow("equalized Gray",equalized_gray)
# cv2.waitKey()

#YUV :亮度，色度，饱和度
yuv =cv2.cvtColor(original,cv2.COLOR_BGR2YUV)
print(yuv.shape)
yuv[:,:,0]=cv2.equalizeHist(yuv[:,:,0])
equalized_color =cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)
cv2.imshow("Equalized Color",equalized_color)
cv2.waitKey()


