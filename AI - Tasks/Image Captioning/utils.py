# utils.py

import string
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def clean_caption(caption):
    """
    Clean and normalize a caption string.
    """
    caption = caption.lower()
    caption = caption.translate(str.maketrans('', '', string.punctuation))
    caption = caption.strip()
    return caption

def create_tokenizer(captions_list):
    """
    Create and fit a tokenizer on the captions.
    """
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(captions_list)
    return tokenizer

def max_caption_length(captions_list):
    """
    Get the maximum length of all captions.
    """
    return max(len(caption.split()) for caption in captions_list)

def encode_caption(caption, tokenizer, max_length):
    """
    Encode a single caption into integer tokens and pad it.
    """
    seq = tokenizer.texts_to_sequences([caption])[0]
    padded = pad_sequences([seq], maxlen=max_length, padding='post')
    return padded[0]

def create_sequences(tokenizer, max_length, image_features, captions, vocab_size):
    """
    Create input-output sequence pairs for model training.
    """
    X1, X2, y = [], [], []
    for img_id, caption_list in captions.items():
        for caption in caption_list:
            caption = 'startseq ' + caption + ' endseq'
            seq = tokenizer.texts_to_sequences([caption])[0]
            for i in range(1, len(seq)):
                in_seq, out_seq = seq[:i], seq[i]
                in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
                out_seq = np.zeros(vocab_size)
                out_seq[out_seq] = 1.0
                X1.append(image_features[img_id])
                X2.append(in_seq)
                y.append(out_seq)
    return np.array(X1), np.array(X2), np.array(y)

