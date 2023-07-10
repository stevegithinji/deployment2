# Flask is the overall web framework
from flask import Flask, request, jsonify
# joblib is used to unpickle the model
import joblib
# json is used to prepare the result
import json
import numpy

# create new flask app here
app = Flask(__name__)

# helper function here

def iris_prediction(sepal_length, sepal_width, petal_length, petal_width):
    """
    Given sepal length, sepal width, petal length, and petal width,
    predict the class of iris
    """

    # Load the model from the file
    with open("model1.pkl", "rb") as f:
        model = joblib.load(f)

<<<<<<< HEAD
    # Load the vectorizer from the file
    with open("vectorizer.pkl", "rb") as f:
        tfidf = joblib.load(f)
        
    # Vectorize the new text using the same vectorizer
    new_text_vectorized = tfidf.transform([text])

    # Make predictions using the trained model
    predicted_label = baseline_model.predict(new_text_vectorized)[0]
    
    return {"predicted_label": predicted_label}
=======
    # Construct the 2D matrix of values that .predict is expecting
    X = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Get a list of predictions and select only 1st
    predictions = model.predict(X)
    prediction = int(predictions[0])

    return {"predicted_class": prediction}
>>>>>>> 3c3219a5e805feb7368224d84c0243593c582e54

# defining routes here

@app.route('/', methods=['GET'])
def index():
<<<<<<< HEAD
    return 'Heyyyy you!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.json
    text = data['text']

    # Perform the prediction
    prediction = news_classification(text)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})
=======
    return 'Hello, world!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the request data from the user in JSON format
    request_json = request.get_json()

    # We are expecting the request to look like this:
    # {"sepal_length": <x1>, "sepal_width": <x2>, "petal_length": <x3>, "petal_width": <x4>}
    # Send it to our prediction function using ** to unpack the arguments
    result = iris_prediction(**request_json)

    # Return the result as a string with JSON format
    return json.dumps(result)
>>>>>>> 3c3219a5e805feb7368224d84c0243593c582e54
