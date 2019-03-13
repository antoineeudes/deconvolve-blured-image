from __future__ import division
import numpy as np
import scipy
from numpy import *
from scipy import *
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage


I = imread("car.png")[:,:,1] # The image is already in black & white, so we can just read one color channel (here red)
# I is a N1 x N2 array such that I[i,j], between 0 and 1, codes the intensity of light at pixel (i,j).
# Careful: i is the vertical index and j is the horizontal one! (check it)
figure()
imshow(I, cmap="Greys_r") # Greys_r to display 0 as black and 1 and white

# useful functions: fft2 (not fft!), ifft2 (not ifft!), conj
figure()
imshow(log10(abs(fft2(I))), cmap="Greys_r") # Greys_r to display 0 as black and 1 and white
colorbar()


L = 15
mu = 0.005 # without this term, the noises will be emphasized by the fourier transformation
height, width = I.shape
h = np.zeros((height, width))


for j in range(0, 2*L):
    h[0, j]=1./(2*L)


g_hat = fft2(I)
h_hat = fft2(h)

square_h_hat = h_hat*h_hat

f_hat = g_hat*np.conjugate(h_hat)/(abs(square_h_hat)+mu)

figure()
imshow(np.real(ifft2(f_hat)), cmap="Greys_r")
show()
