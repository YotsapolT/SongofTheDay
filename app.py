from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import time

# NLP Packages
import nltk
from transformers import BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import pickle
nltk.download("stopwords")

with open("assets/files/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("assets/files/song_vectors.pkl", "rb") as f:
    song_vectors = pickle.load(f)

data = pd.read_csv("assets/files/spotify_taylorswift.csv", usecols=["name", "link"])

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyse", methods=["POST"])
def analyse():
    start = time.time()
    if request.method == "POST":
        rawtext = request.form["rawtext"]
        #  analyse untion
        input_text_vector = input_def(rawtext)

        # Compute the cosine similarity between the new text and each song vector
        similarities = cosine_similarity([input_text_vector], song_vectors)[0]

        # Find the index of the most similar song
        # most_similar_index = similarities.argmax()
        # print(most_similar_index)
        # print(data.loc[most_similar_index])

        # top 5
        top_indices = similarities.argsort()[::-1][:5]
        songs = []

        for index in top_indices:
            songs.append(data.loc[index])

    end = time.time()
    final_time = end - start

    return render_template(
        "index.html",
        received_text=rawtext,
        summary=songs,
        final_time=final_time,
    )


def input_def(input_text):
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    # Preprocess the text and generate a vector representation
    input_text_words = tokenizer.tokenize(input_text.lower())

    stop_words = set(stopwords.words("english"))
    input_text_words = [word for word in input_text_words if not word in stop_words]

    input_text_vector = model.infer_vector(input_text_words)
    return input_text_vector


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
