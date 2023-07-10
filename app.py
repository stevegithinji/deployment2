# Flask is the overall web framework
from flask import Flask, request, jsonify
# joblib is used to unpickle the model
import joblib
# json is used to prepare the result
import json
import numpy

# helper function here
def news_classification(text):
    # Load the model from the file
    with open("model.pkl", "rb") as f:
        baseline_model = joblib.load(f)

    # Load the vectorizer from the file
    with open("vectorizer.pkl", "rb") as f:
        tfidf = joblib.load(f)

    # Vectorize the new text using the same vectorizer
    new_text_vectorized = tfidf.transform([text])  # Wrap the text in a list

    # Make predictions using the trained model
    predicted_label = baseline_model.predict(new_text_vectorized)[0]  # Extract the label from the array

    return {"predicted_label": predicted_label}

@app.route('/', methods=['GET'])
def index():
    return 'Heyy!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.json
    text = data['text']

    # Perform the prediction
    prediction = news_classification(text)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})