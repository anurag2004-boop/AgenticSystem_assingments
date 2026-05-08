import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=21)
n_samples = 400
study_hours = rng.uniform(1, 10, size=n_samples)
exam_score = 40 + 7.5 * study_hours + rng.normal(0, 6, size=n_samples)

df = pd.DataFrame({"study_hours": study_hours, "exam_score": exam_score})
print(df.head())
import matplotlib.pyplot as plt

plt.scatter(df["study_hours"], df["exam_score"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Relationship between Study Hours and Exam Score")
plt.show()
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split    
X = df[["study_hours"]]
y = df["exam_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Actual vs Predicted Exam Scores")
plt.legend()
plt.show()


def regression_metrics_from_df(df, y_col: str, y_pred_col: str) -> dict:
    """
    Return a dict with keys: 'mae', 'rmse', 'r2'
    using sklearn.metrics (numpy only for sqrt of MSE).
    """
    ...
def regression_metrics_from_df(df, y_col: str, y_pred_col: str) -> dict:
    """
    Return a dict with keys: 'mae', 'rmse', 'r2'
    using sklearn.metrics (numpy only for sqrt of MSE).
    """
    ...
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    mae = mean_absolute_error(df[y_col], df[y_pred_col])
    rmse = np.sqrt(mean_squared_error(df[y_col], df[y_pred_col]))
    r2 = r2_score(df[y_col], df[y_pred_col])    
    return {"mae": mae, "rmse": rmse, "r2": r2}
df_test = X_test.copy()
df_test["exam_score"] = y_test  
df_test["predicted_exam_score"] = y_pred
metrics = regression_metrics_from_df(df_test, y_col="exam_score", y_pred_col="predicted_exam_score")
print(metrics)

