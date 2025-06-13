import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r'C:\Users\dhanu\OneDrive\Desktop\dog.jpeg', cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
bit_planes = []
for i in range(8):
    bit_plane = (image & (1 << i)) >> i
    bit_plane = bit_plane * 255
    bit_planes.append(bit_plane)
plt.figure(figsize=(12, 6))
plt.subplot(2, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
for i in range(8):
    plt.subplot(2, 4, i + 2)
    plt.imshow(bit_planes[i], cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')
plt.tight_layout()
plt.show()
