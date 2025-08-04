# AI Internship Tasks – Codsoft

This repository contains 4 AI-based projects developed as part of the **Codsoft Internship Program**. Each project demonstrates a core concept in Artificial Intelligence including rule-based logic, search algorithms, computer vision, NLP, and recommendation systems.

---

##  Project List

1. **Rule-Based Chatbot**
2. **Tic-Tac-Toe AI using Minimax Algorithm**
3. **Image Captioning**
4. **Movie Recommendation System**

---

## 1.  Rule-Based Chatbot

A basic chatbot that replies to simple user queries using hardcoded keyword-based rules.

### Technologies Used:
- Python
- Regular Expressions (`re`)
- Flask (for web interface)

### How to Run:
```bash
cd Rule-Based-Chatbot
python chatbot.py
```

To run the web version:
```bash
python app.py
```

Then open your browser at `http://127.0.0.1:5000/`

---

## 2.  Tic-Tac-Toe AI using Minimax Algorithm

A command-line Tic-Tac-Toe game where the AI uses the Minimax algorithm to make unbeatable decisions.

### Technologies Used:
- Python
- Minimax Algorithm
- Terminal-based interaction

### How to Run:
```bash
cd TicTacToe-AI
python tic_tac_toe.py
```

Follow the terminal prompts to play against the AI.

---

## 3. Image Captioning

This app takes an input image and generates a descriptive caption using a CNN-RNN pipeline. The CNN (InceptionV3) extracts features, and the RNN (LSTM) generates the sentence.

### Technologies Used:
- Python
- TensorFlow/Keras
- Flask (for web interface)
- Pre-trained InceptionV3
- LSTM for language generation
- Pillow, NumPy

### How to Run:
```bash
cd Image-Captioning
pip install -r requirements.txt
python app.py
```

Then open your browser:
```
http://127.0.0.1:5000/
```

Upload an image, and it will generate a caption for it.

---

## 4.  Movie Recommendation System

A content-based recommendation system that suggests movies similar to a user’s preferences using cosine similarity on movie overviews.

### Technologies Used:
- Python
- Pandas
- Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
- Flask
- CSV dataset (`movies.csv`)

### How to Run:
```bash
cd recommendation_system
pip install -r requirements.txt
python app.py
```

Then go to:
```
http://127.0.0.1:5000/
```

Type a movie name to get similar movie recommendations.

---

##  Requirements Installation

Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If `venv` is not installed, use:
```bash
sudo apt install python3-venv
```

---

##  Suggested Folder Structure

```
Codsoft/
├── Rule-Based-Chatbot/
│   ├── chatbot.py
│   └── app.py
├── TicTacToe-AI/
│   └── tic_tac_toe.py
├── Image-Captioning/
│   ├── app.py
│   ├── cnn_encoder.py
│   ├── model.py
│   ├── utils.py
│   └── caption_generator.py
├── recommendation_system/
│   ├── app.py
│   ├── movies.csv
│   └── recommender.py
├── requirements.txt
└── README.md
```

---

## ✅ Internship Completion Note

Each project was implemented, tested, and demonstrated successfully as part of the internship deliverables.

---
