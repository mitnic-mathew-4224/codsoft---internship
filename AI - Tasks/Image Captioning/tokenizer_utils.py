
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class TokenizerUtils:
    def __init__(self, num_words=None, oov_token='<unk>'):
        self.tokenizer = Tokenizer(num_words=num_words, oov_token=oov_token)
        self.max_length = 0

    def fit(self, captions_list):
        self.tokenizer.fit_on_texts(captions_list)
        sequences = self.tokenizer.texts_to_sequences(captions_list)
        self.max_length = max(len(seq) for seq in sequences)

    def texts_to_sequences(self, captions_list):
        return self.tokenizer.texts_to_sequences(captions_list)

    def pad_sequence(self, sequence):
        return pad_sequences([sequence], maxlen=self.max_length, padding='post')[0]

    def sequence_to_text(self, sequence):
        reverse_word_map = dict(map(reversed, self.tokenizer.word_index.items()))
        return ' '.join([reverse_word_map.get(idx, '') for idx in sequence if idx > 0])

    def save(self, path='tokenizer.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(self.tokenizer, f)

    def load(self, path='tokenizer.pkl'):
        with open(path, 'rb') as f:
            self.tokenizer = pickle.load(f)

