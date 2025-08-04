

from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, Add
from tensorflow.keras.models import Model

def build_caption_model(vocab_size, max_length, embedding_dim=256, units=256):
    """
    Builds the image captioning model using an encoder-decoder architecture.

    Args:
        vocab_size: Number of words in the vocabulary.
        max_length: Maximum length of caption.
        embedding_dim: Dimension of word embeddings.
        units: Number of LSTM units.

    Returns:
        model: Compiled Keras model.
    """
    # Image feature extractor model input
    image_input = Input(shape=(2048,), name="image_features")
    img_dense = Dense(units, activation='relu')(image_input)

    # Caption input
    caption_input = Input(shape=(max_length,), name="caption_input")
    caption_embed = Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True)(caption_input)
    lstm_output = LSTM(units)(caption_embed)

    # Combine both inputs
    decoder = Add()([img_dense, lstm_output])
    decoder_output = Dense(vocab_size, activation='softmax')(decoder)

    # Model
    model = Model(inputs=[image_input, caption_input], outputs=decoder_output)
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    return model

