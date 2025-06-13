import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r'C:\Users\dhanu\OneDrive\Desktop\dog.jpeg',cv2.IMREAD_GRAYSCALE)
_,thresh_simple = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
thresh_adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY, 11, 2)
plt.figure(figsize=(20, 10))
plt.subplot(1,3,1)
plt.imshow(image,cmap='gray')
plt.subplot(1,3,2)
plt.imshow(thresh_simple,cmap='gray')
plt.subplot(1,3,3)
plt.imshow(thresh_adaptive,cmap='gray')


