'''
https://medium.com/data-hackers/t%C3%A9cnicas-de-processamento-digital-de-imagens-no-python-com-matem%C3%A1tica-154eae204447

Detectar face:
https://web.dio.me/course/redes-de-sensores-sem-fio-para-iot/learning/22dc25e1-8f64-4aa3-a738-d3f3b5ff1bf7?back=/track/formacao-iot-specialist&tab=path&moduleId=fee2cba2-2738-41f5-94a1-e7625e86fdaa

https://academiapme-my.sharepoint.com/personal/nubia_dio_me/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fnubia%5Fdio%5Fme%2FDocuments%2FSlides%2DDIO%2FInternet%20of%20Things%20%28IoT%29%20Specialist%2FRedes%20de%20Sensores%20sem%20Fio%20para%20IoT&ga=1
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
from skimage import data
import math

image = data.coffee()
plt.imshow(image, cmap='gray')

plt.show()

