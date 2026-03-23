# 🚀 Placement Predictor

A simple and clean **Machine Learning + Web App** that predicts a student's placement chances based on academic performance.

---

## 🧠 How It Works

* User enters:

  * 10th Percentage
  * 12th Percentage
  * UG CGPA
  * Master CGPA

* The model processes input using **Logistic Regression**

* Outputs:

  * 🎯 Placement Probability (%)
  * 📊 Visual Graph (Donut Chart)
  * 💡 Improvement Suggestions

---

## ⚙️ Tech Stack

* **Frontend:** HTML, CSS (Neon UI)
* **Backend:** Flask (Python)
* **ML Model:** Scikit-learn (Logistic Regression)
* **Visualization:** Chart.js

---

## 📁 Project Structure

```
project/
│── app.py
│── train.py
│── model.pkl
│── templates/
│     ├── index.html
│     └── result.html
│── static/
│── requirements.txt (optional)
```

---

## ▶️ How to Run

### 1. Clone the repo

```
git clone <your-repo-link>
cd project
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install flask scikit-learn pandas
```

### 4. Train model

```
python train.py
```

### 5. Run app

```
python app.py
```

### 6. Open in browser

```
http://127.0.0.1:5000
```

---

## 🎯 Features

* Minimal + Neon UI (Responsive)
* Real-time prediction
* Visual donut chart
* Smart suggestions
* Aesthetic glowing watermark

---

## 🧠 Model Info

* Algorithm: Logistic Regression
* Type: Binary Classification
* Output: Placement Probability

---

## 🚀 Future Improvements

* Use real-world datasets
* Add more features (skills, internships)
* Improve model accuracy
* Deploy online

---

## 👤 Author

**AJ**

---

## ⭐ Note

This project is built for learning and demonstration purposes.
