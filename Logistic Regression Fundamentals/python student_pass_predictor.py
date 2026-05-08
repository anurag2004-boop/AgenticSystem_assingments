import numpy as np
from numpy.random import default_rng
from sklearn.metrics import confusion_matrix

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
import pandas as pd
df = pd.DataFrame(X, columns=["study_hours", "attendance_percent", "assignments_done"])
df["passed"] = y
print(df.head())

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.predict_proba(X_test)[:5])
print(f" | Study Hrs | Attendance % | Assignments | Actual | Predicted | P(Pass) | Correct?")
for i in range(5):
    study_hrs = X_test[i, 0]
    attendance = X_test[i, 1]
    assignments = X_test[i, 2]
    actual = y_test[i]
    predicted = model.predict(X_test[i].reshape(1, -1))[0]
    prob_pass = model.predict_proba(X_test[i].reshape(1, -1))[0][1]
    correct = "Yes" if predicted == actual else "No"
    print(f"{study_hrs:10.2f} | {attendance:13.2f} | {assignments:11.2f} | {actual:6d} | {predicted:9d} | {prob_pass:7.2f} | {correct}")

y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))









