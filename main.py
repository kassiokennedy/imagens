import numpy as np
import matplotlib.pyplot as plt 
from skimage import data
import math

image = data.coffee()
plt.imshow(image, cmap='gray')

plt.show()