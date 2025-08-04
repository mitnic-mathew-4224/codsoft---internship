import pandas as pd
import json
import os

class MovieRecommender:
    def __init__(self, movies_path, users_path):
        self.movies_path = movies_path
        self.users_path = users_path
        self.movies = pd.read_csv(movies_path)
        self.load_users()

    def load_users(self):
        if os.path.exists(self.users_path):
            with open(self.users_path, 'r') as f:
                self.users = json.load(f)
        else:
            self.users = {}

    def save_users(self):
        with open(self.users_path, 'w') as f:
            json.dump(self.users, f, indent=4)

    def add_user(self, username, preferences):
        self.users[username] = preferences
        self.save_users()

    def recommend(self, username, top_n=5):
        if username not in self.users:
            return ["User not found"]

        preferences = self.users[username]["genres"]
        filtered = self.movies[self.movies['genres'].str.contains('|'.join(preferences), case=False, na=False)]
        recommended = filtered.sort_values(by="rating", ascending=False).head(top_n)
        return recommended[["title", "genres", "rating"]].values.tolist()
