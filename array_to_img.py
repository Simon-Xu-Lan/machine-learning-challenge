import base64
import cv2
import numpy as np

def transfer_nparray_to_img(img_np_arr):
   
    # The input numpy array shape is (28, 28, 1), representing a grayscale image
    # Transfer the numpy array into (28, 28, 3), representing a RGB image
    img_rgb = np.zeros((28,28, 3))
    for index, value in np.ndenumerate(img_np_arr):
        if value > 0.99:
            img_rgb[index[0], index[1]] = [255, 255, 255]

    # Transfer np arry into base64 format
    retval, buffer = cv2.imencode('.png', img_rgb)
    pic_str = base64.b64encode(buffer)
    pic_str = pic_str.decode()

    img_URL = f"data:image/png;base64,{pic_str}"
    
    return img_URL