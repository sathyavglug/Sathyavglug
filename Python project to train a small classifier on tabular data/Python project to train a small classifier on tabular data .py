

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


print("🔹 Loading the Iris dataset...")
data = sns.load_dataset("iris")
print(data.head())


X = data.drop("species", axis=1)
y = data["species"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [3, 5, 7, None]
}

model = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(model, param_grid, cv=3, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

best_model = grid_search.best_estimator_
print("\n✅ Best Parameters Found:", grid_search.best_params_)


y_pred = best_model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Model Accuracy: {accuracy:.2f}")
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))


cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, cmap="Greens", fmt="d",
            xticklabels=data['species'].unique(),
            yticklabels=data['species'].unique())
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

importances = best_model.feature_importances_
feature_names = X.columns
plt.figure(figsize=(6, 4))
sns.barplot(x=importances, y=feature_names, palette="coolwarm")
plt.title("Feature Importance")
plt.show()


joblib.dump(best_model, "iris_classifier.pkl")
joblib.dump(scaler, "scaler.pkl")
print("\n💾 Model and scaler saved successfully!")


loaded_model = joblib.load("iris_classifier.pkl")
loaded_scaler = joblib.load("scaler.pkl")


new_data = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=X.columns)
new_data_scaled = loaded_scaler.transform(new_data)
pred = loaded_model.predict(new_data_scaled)
print("\n🌸 Prediction for new sample:", pred[0])
