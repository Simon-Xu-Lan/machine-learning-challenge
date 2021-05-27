import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from base64 import b64decode

model = load_model("mnist_trained.h5")

def predict_image():
    filepath = "./images/simon2.png"
    image_size = (28, 28)
    im = image.load_img(filepath, target_size=image_size, color_mode="grayscale")
    img = img_to_array(im)
    # Scale the image pixels by 255 (or use a scaler from sklearn here)
    img /= 255

    # Flatten into a 1x28*28 array 
    img = img.flatten().reshape(-1, 28*28)

    img = 1 - img

    result = model.predict_classes(img)

    print(result)


def predict_imgURL(dataURL):
    header, encoded = dataURL.split(",", 1)
    data = b64decode(encoded)

    image = tf.io.decode_image(data, channels=3)

    # resize image
    image_size = (28, 28)
    image_28x28 = tf.image.resize(image, 
                            method="bilinear", 
                            size=image_size,
                        )
    
    image_grayscaled = tf.image.rgb_to_grayscale(image_28x28)

    # convert tensorflow.python.framework.ops.EagerTensor into numpy array
    image_np_arr = image_grayscaled.numpy()

    # Scale the image pixels by 255 (or use a scaler from sklearn here)
    image_np_arr /= 255

    # Flatten into a 1x28*28 array 
    image_flatten = image_np_arr.flatten().reshape(-1, 28*28)
    # Invert the pixel values to match the data input of model
    img = 1 - image_flatten

    # predict the image
    result = model.predict_classes(img)
    
    # print(result[0])
    return result[0]

