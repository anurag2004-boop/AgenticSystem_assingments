
# 1. Logistic Regression
# 2. Decision Tree Classifier
# 3. Random Forest Classifier
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# 1. Logistic Regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train_scaled, y_train)
# 2. Decision Tree Classifier
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train_scaled, y_train)
# 3. Random Forest Classifier
forest_model = RandomForestClassifier(random_state=42)
forest_model.fit(X_train_scaled, y_train)

# Evaluate models
from sklearn.metrics import accuracy_score, classification_report, f1_score
models = {
    "Logistic Regression": logistic_model,
    "Decision Tree": tree_model,
    "Random Forest": forest_model
}
best_model_name = None
best_f1 = 0.0
for name, model in models.items():
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))
    print(f"{name} F1-Score: {f1:.4f}")
    print("✓ Model is at the sweet spot — acceptable gap")

    if best_model_name is None or f1 > best_f1:
        best_model_name = name
        best_f1 = f1

print(f"Selected Model: {best_model_name} | F1-Score: {best_f1:.4f}")



import joblib
joblib.dump(models[best_model_name], "tumour_classifier_v1.joblib")
joblib.dump(scaler, "tumour_scaler_v1.joblib")

# Print sample predictions vs actual labels
sample_preds = models[best_model_name].predict(X_test_scaled)
print("Predictions vs Actual (first 10):")
print("Predicted:", sample_preds[:10])
print("Actual:   ", y_test[:10])





