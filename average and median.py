import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r'C:\Users\user\Pictures\wall-art-2852231_1920.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
averaging=cv2.blur(image,(3,3))
median=cv2.medianBlur(image,3)
plt.subplot(1,3,1)
plt.imshow(image)
plt.subplot(1,3,2)
plt.imshow(averaging)
plt.subplot(1,3,3)
plt.imshow(median)
plt.show()

