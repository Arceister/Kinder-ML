from io import BytesIO
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

def api_hit_response():
  return {"Message": "API Accessed!"}

def predict_image(image_to_predict):
  model = tf.keras.models.load_model('Models/keras_model.h5')
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = Image.open(BytesIO(image_to_predict))
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.ANTIALIAS)

  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
  data[0] = normalized_image_array

  prediction = model.predict(data)
  pr = np.argmax(prediction, axis=1)

  labels = {
    0: "Apple",
    1: "Orange",
    2: "Banana",
    3: "Rotten Apple",
    4: "Rotten Orange",
    5: "Rotten Banana"
  }

  return {"Hasil": labels[int(pr[0])]}