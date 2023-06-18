import os
import random
from PIL import Image
from numpy import *
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

x_train=np.zeros((21555,12600))
y_train=np.zeros((21555))
files=os.listdir("archive")
for i in range(21555):
    item=random.choice(files)
    image=Image.open(os.path.join("archive/", item))
    imagedata=asarray(image)[:,:,0]
    #imagedata = tf.image.rgb_to_grayscale(imagedata)
    #imagedata = imagedata.numpy()
    imagedata = imagedata.reshape(140 * 90)
    imagedata = np.invert(imagedata)
    x_train[i]=imagedata
    y_train[i]=int(item[0])
    files.remove(item)

x_train=tf.keras.utils.normalize(x_train,axis=1)
#x_test=tf.keras.utils.normalize(x_test,axis=1)

model=Sequential([
                  Dense(128,activation='relu'),
                  Dense(128,activation='relu'),
                  Dense(10,activation='sigmoid')],name='my_model')
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(0.001),
    metrics=['accuracy'])
model.fit(x_train,y_train,epochs=10)
model.summary()
model.save('handwritten_digits_custom3')

'''
model=tf.keras.models.load_model('handwritten_digits_custom3')
image=Image.open('test2.png')
imagedata=asarray(image)[:,:,0]
#imagedata=tf.image.rgb_to_grayscale(imagedata)
#imagedata=imagedata.numpy()
imagedata=imagedata.reshape(140*90)
x_test=np.invert(np.array([imagedata]))
x_test=tf.keras.utils.normalize(x_test,axis=1)
prediction=model.predict(x_test)
print(np.argmax(prediction))'''