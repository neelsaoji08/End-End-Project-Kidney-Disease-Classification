import numpy as np
from keras.models import load_model
import os
from PIL import Image



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename

    
    
    def predict(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))
        imagename = self.filename
        test_image = np.array(Image.open(imagename).resize((224,224)))
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]