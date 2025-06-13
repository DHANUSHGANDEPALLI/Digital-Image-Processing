import cv2
import numpy as np
import matplotlib.pyplot as plt
f = cv2.imread(r'C:\Users\user\Pictures\beech-fagus-from-below-in-black-and-white-mindelheim-unterallgaeu-CXR721.jpg')

F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)

plt.imshow(f, cmap='gray')
plt.axis('off')
plt.show()

[M,N,C] = f.shape
H = np.zeros_like(f)
D0 = 10 
n = 10  
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H[u,v] = 1 / (1 + (D/D0)**n)
        
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()

HPF = 1 - H
        
Gishift = Fshift * HPF
Gi = np.fft.ifftshift(Gishift)
gi = np.abs(np.fft.ifft2(Gi))

plt.imshow(gi, cmap='gray')
plt.axis('off')
plt.show()
