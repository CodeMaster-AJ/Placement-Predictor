import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
data = pd.read_csv("placement.csv")

# -------- SELECT IMPORTANT FEATURES --------
features = ['ssc_p', 'hsc_p', 'degree_p', 'mba_p']
target = 'status'   # Placed / Not Placed

data = data[features + [target]].dropna()

# Encode target
le = LabelEncoder()
data[target] = le.fit_transform(data[target])  # Placed=1, Not Placed=0

# Split
X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(le, open("encoder.pkl", "wb"))

print("✅ Real model trained")