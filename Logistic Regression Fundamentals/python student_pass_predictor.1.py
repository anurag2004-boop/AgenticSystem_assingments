import numpy as np
from numpy.random import default_rng
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

rng = default_rng(seed=99)
n = 500

study_hours        = rng.uniform(1, 10, size=n)       # daily study hours
attendance_percent = rng.uniform(40, 100, size=n)     # class attendance %
assignments_done   = rng.uniform(0, 10, size=n)       # assignments submitted (out of 10)

scores = (
    20
    + 5.5  * study_hours
    + 0.4  * attendance_percent
    + 3.0  * assignments_done
    + rng.normal(0, 8, size=n)
)

# Label: 1 = Pass, 0 = Fail
y = (scores >= 70).astype(int)
X = np.column_stack([study_hours, attendance_percent, assignments_done])
df = pd.DataFrame(X, columns=["study_hours", "attendance_percent", "assignments_done"])
df["passed"] = y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# 1. Extract P(Pass) for all test students
y_prob = model.predict_proba(X_test)[:, 1]

thresholds = [0.5, 0.7]

for t in thresholds:
    # 2. Apply threshold manually
    predictions = (y_prob >= t).astype(int)
    
    num_pass = np.sum(predictions == 1)
    num_fail = np.sum(predictions == 0)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"--- Threshold: {t} ---")
    print(f"Predicted Pass: {num_pass}")
    print(f"Predicted Fail: {num_fail}")
    print(f"Overall Accuracy: {accuracy:.4f}\n")