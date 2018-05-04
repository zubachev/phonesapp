import pickle
from flask import Flask, render_template, request
from sentiment_classifier import SentimentClassifier

app = Flask(__name__)

classifier = SentimentClassifier()

@app.route("/", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        print (text)
        prediction_message = classifier.get_prediction_message(text)
        print (prediction_message)
    return render_template('index.html', text=text, prediction_message=prediction_message)

if __name__ == "__main__":
    app.run()
