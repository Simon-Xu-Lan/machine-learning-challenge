import numpy as np
from test_data import dataURL
from divide_img import divide_img
from array_to_img import transfer_nparray_to_img

imgA, imgB = divide_img(dataURL)


print(imgA)
print(imgB)



