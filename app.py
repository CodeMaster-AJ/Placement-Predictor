from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    ssc = float(request.form["ssc"])
    hsc = float(request.form["hsc"])
    degree = float(request.form["degree"])
    mba = float(request.form["mba"])

    data = np.array([[ssc, hsc, degree, mba]])

    prob = model.predict_proba(data)[0][1]
    percent = round(prob * 100, 2)

    # suggestions
    suggestion = ""
    if ssc < 60:
        suggestion += "Improve basics. "
    if degree < 65:
        suggestion += "Focus on degree performance. "
    if mba < 60:
        suggestion += "Improve higher education score. "

    if suggestion == "":
        suggestion = "Strong profile 🚀"

    return render_template(
        "result.html",
        percent=percent,
        suggestion=suggestion
    )

if __name__ == "__main__":
    app.run(debug=True)