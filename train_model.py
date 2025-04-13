import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
 
 # Load the dataset
df = pd.read_csv("heart.csv")

# View the first few rows of the dataset to verify the columns
print(df.head())


# Define the features (X) and target (y)
X = df.drop("output", axis=1)  # 'output' is the target variable
y = df["output"]  # Target variable (1 = disease, 0 = no disease)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)


# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model to a file (model.pkl)
joblib.dump(model, "model.pkl")
