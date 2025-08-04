
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

def generate_caption(model, tokenizer, image_feature, max_length):
    """
    Generate a caption for an image using the trained model.
    
    Args:
        model: The trained image captioning model.
        tokenizer: The fitted tokenizer.
        image_feature: The encoded feature of the image (from CNN).
        max_length: Maximum length of the caption.

    Returns:
        Generated caption as a string.
    """
    in_text = 'startseq'
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([np.array([image_feature]), sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = None
        for w, index in tokenizer.word_index.items():
            if index == yhat:
                word = w
                break
        if word is None:
            break
        in_text += ' ' + word
        if word == 'endseq':
            break
    final_caption = in_text.replace('startseq', '').replace('endseq', '').strip()
    return final_caption
 
