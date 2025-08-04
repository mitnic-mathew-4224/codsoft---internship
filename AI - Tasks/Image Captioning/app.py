# app.py

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np

from cnn_encoder import extract_features
from generate_caption import generate_caption
from load_model_tokenizer import model, tokenizer, max_length

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    caption = ''
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No file uploaded', 400
        file = request.files['image']
        if file.filename == '':
            return 'No selected file', 400
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Extract features
            image = Image.open(file_path)
            image = image.convert('RGB')
            feature = extract_features(image)

            # Generate caption
            caption = generate_caption(model, tokenizer, feature, max_length)

            return render_template('index.html', caption=caption, image=filename)
    return render_template('index.html', caption=caption)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f"/{UPLOAD_FOLDER}/{filename}"


if __name__ == '__main__':
    app.run(debug=True)

