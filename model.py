import tensorflow
from PIL import Image
import numpy as np

def prediction():
    #Carga el modelo.
    model = tensorflow.keras.models.load_model("deteccion-lunares-cnn.h5")

    img = Image.open("image.png")
    #Transforma la imagen para que coincidan con el modelo.
    img = img.convert('RGB')  
    img = img.resize((100, 100)) 
    img = np.array(img)
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)

    # Realiza la predicción.
    predictions = model.predict(img)
    value = predictions[0][0]
    return str(value)