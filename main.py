from __future__ import division
import numpy
import scipy
from numpy import *
from scipy import *
from pylab import *

I = imread("car.png")[:,:,0] # The image is already in black & white, so we can just read one color channel (here red)
# I is a N1 x N2 array such that I[i,j], between 0 and 1, codes the intensity of light at pixel (i,j).
# Careful: i is the vertical index and j is the horizontal one! (check it)

figure()
imshow(I, cmap="Greys_r") # Greys_r to display 0 as black and 1 and white

# useful functions: fft2 (not fft!), ifft2 (not ifft!), conj
figure()
imshow(log10(abs(fft2(I))), cmap="Greys_r") # Greys_r to display 0 as black and 1 and white
colorbar()

show()
