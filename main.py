'''
https://medium.com/data-hackers/t%C3%A9cnicas-de-processamento-digital-de-imagens-no-python-com-matem%C3%A1tica-154eae204447
'''

import numpy as np
import matplotlib.pyplot as plt 
from skimage import data
import math

image = data.coffee()
plt.imshow(image, cmap='gray')

plt.show()