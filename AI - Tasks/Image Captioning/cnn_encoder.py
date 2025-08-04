
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
import numpy as np

class CNN_Encoder:
    def __init__(self):
        base_model = ResNet50(weights='imagenet', include_top=False)
        self.model = Model(inputs=base_model.input, outputs=base_model.output)

    def encode(self, img_path):
        # Load image and resize to 224x224
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Get feature map
        features = self.model.predict(img_array)
        features = np.reshape(features, (-1, features.shape[-1]))  # Flatten
        return features

