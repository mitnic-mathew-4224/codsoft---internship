
import os
import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tqdm import tqdm

class DatasetLoader:
    def __init__(self, image_dir, captions_file):
        self.image_dir = image_dir
        self.captions_file = captions_file
        self.image_model = self._build_image_model()

    def _build_image_model(self):
        base_model = InceptionV3(weights='imagenet')
        model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)
        return model

    def load_captions(self):
        """
        Loads image captions from file.
        Returns:
            captions_dict: {image_filename: [caption1, caption2, ...]}
        """
        captions_dict = {}
        with open(self.captions_file, 'r') as file:
            for line in file:
                tokens = line.strip().split('\t')
                if len(tokens) < 2:
                    continue
                image_name, caption = tokens[0], tokens[1]
                image_name = image_name.split('#')[0]
                captions_dict.setdefault(image_name, []).append(f'<start> {caption} <end>')
        return captions_dict

    def preprocess_image(self, img_path):
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x

    def extract_features(self):
        """
        Extracts features for each image in the directory using InceptionV3.
        Returns:
            features_dict: {image_filename: feature_vector}
        """
        features_dict = {}
        image_files = os.listdir(self.image_dir)
        for img_file in tqdm(image_files, desc="Extracting image features"):
            img_path = os.path.join(self.image_dir, img_file)
            img_tensor = self.preprocess_image(img_path)
            features = self.image_model.predict(img_tensor)
            features_dict[img_file] = features.flatten()
        return features_dict

