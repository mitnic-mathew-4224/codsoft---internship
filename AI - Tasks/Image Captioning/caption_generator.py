

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add

class CaptionGenerator:
    def __init__(self, vocab_size, max_length, embedding_dim=256):
        self.vocab_size = vocab_size
        self.max_length = max_length
        self.embedding_dim = embedding_dim

    def build_model(self):
        # Feature extractor input
        inputs1 = Input(shape=(49, 2048))
        fe1 = Dropout(0.5)(inputs1)
        fe2 = Dense(self.embedding_dim, activation='relu')(fe1)

        # Sequence processor input
        inputs2 = Input(shape=(self.max_length,))
        se1 = Embedding(self.vocab_size, self.embedding_dim, mask_zero=True)(inputs2)
        se2 = Dropout(0.5)(se1)
        se3 = LSTM(256)(se2)

        # Decoder (combine features + sequence)
        decoder1 = add([fe2, se3])
        decoder2 = Dense(256, activation='relu')(decoder1)
        outputs = Dense(self.vocab_size, activation='softmax')(decoder2)

        # Define the model
        model = Model(inputs=[inputs1, inputs2], outputs=outputs)
        return model

