from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        news_text = data.get("text", "")

        if not news_text.strip():
            return jsonify({"prediction": "⚠️ Please enter some text."})

        # Transform input and predict
        text_vector = vectorizer.transform([news_text])
        prediction = model.predict(text_vector)[0]

        result = "TRUE NEWS ✅" if prediction == 1 else "FAKE NEWS"
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"prediction": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)