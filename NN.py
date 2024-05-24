from PIL import Image as PILImg
from keras.api.preprocessing import image
from keras.api import models
import numpy as np


def predict(img_path):
    model_loaded = models.load_model('./mela_model.keras')
    class_names = ['доброкачественная', 'злокачественная']
    img = image.load_img(img_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, 0)

    predictions = model_loaded.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

def predict_from_binary(binary_img):
    model_loaded = models.load_model('./mela_model.keras')
    class_names = ['Доброкачественная', 'Злокачественная']
    img = PILImg.open(binary_img)
    img = img.convert('RGB')
    target_size = (256, 256)
    img = img.resize(target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, 0)

    predictions = model_loaded.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

if __name__ == "__main__":
    path = './mal.png'
    print(predict(path))

