import numpy as np
import tensorflow as tf
import pickle
from base64 import b64decode
from array_to_img import transfer_nparray_to_img

with open('./models/svc_model.sav', 'rb') as f:
    svc_model = pickle.load(f)

def divide_img(img_url):
    # Decode img_url
    header, encoded = img_url.split(",", 1)
    data = b64decode(encoded)

    # ===== Procssing image data =====
    # Transfer decoded dataURL into RGB number
    image = tf.io.decode_image(data, channels=3)
    # Resize image, from 400 x 400 to 28 x 28
    image_size = (28, 28)
    image_28 = tf.image.resize(image, 
                            method="bilinear", 
                            size=image_size,
                        )
    # Convert image from RGB format to grey format. That is from 3 varialbe to 1 varialbe for a point in image
    image_28_grey = tf.image.rgb_to_grayscale(image_28)
    # convert tensorflow.python.framework.ops.EagerTensor into numpy array
    image_28_grey_np = image_28_grey.numpy()
    # Scale the image pixels by 255 (or use a scaler from sklearn here)
    image_28_grey_np /= 255
    # Flatten into a 1x28*28 array 
    img = image_28_grey_np.flatten().reshape(-1, 28*28)
    # Invert the pixel values to match the original data
    img_inverted = 1 - img

    # ===== Create image coordinates data, E.g. create the coordintes(x,y) array for the black point in img_inverted =====
    coors =[]
    for index, value in np.ndenumerate(image_28_grey_np):
        point = []
        if value == 0:
            point.append(index[0])
            point.append(index[1])
            coors.append(point)
            
    coors = np.array(coors)

    # ===== Use SVC model to predict, that is, to divid the image =====
    # The "0" in predictions represents one image, The "1" in predictions represents another image
    predictions = svc_model.predict(coors)

    # ===== Divid image based on predictions =====
    # Create the first image for "0" in predictions
    # Create the second image for "1" in predictions
    imgA = []
    imgB = []
    for index, value in np.ndenumerate(predictions):
        if value == 0:
            imgB.append(coors[index[0]])
        else:
            imgA.append(coors[index[0]])

    # Transfer list into numpy array
    imgA = np.array(imgA)
    imgB = np.array(imgB)

    # ===== Resize imgA and imgB to size 28x28
    imgA_28 = np.zeros(shape=(28, 28))
    imgB_28 = np.zeros(shape=(28, 28))
    for v in imgA:
        imgA_28[v[0], v[1]] = 1

    for v in imgB:
        imgB_28[v[0], v[1]] = 1

    # ===== Transfer numpy array to image url
    # Use inversted image, to make the image be white background
    imgA_url = transfer_nparray_to_img(1-imgA_28)
    imgB_url = transfer_nparray_to_img(1-imgB_28)

    return imgA_url, imgB_url


