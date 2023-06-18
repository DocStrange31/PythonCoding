import numpy as np
import tensorflow as tf
from PIL import Image
from numpy import *

image=Image.open('test.png')
imagedata=asarray(image)[:,:,0]
imagedata=np.invert(np.array([imagedata]))
imagedata=tf.keras.utils.normalize(imagedata,axis=1)
model=tf.keras.models.load_model('handwritten_digits_mnist')
prediction=model.predict(imagedata)
print(argmax(prediction))