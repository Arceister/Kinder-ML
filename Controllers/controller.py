from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def api_hit_response():
  return {"Message": "API Accessed!"}

def predict_image():
  model = load_model('../Models/keras_model.h5')
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = Image.open('../Image/apel_example.jpg')
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.ANTIALIAS)

  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
  data[0] = normalized_image_array

  prediction = model.predict(data)
  return {"Prediction": prediction}