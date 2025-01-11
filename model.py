import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("user_behavior_dataset.csv")

df.dropna(inplace=True)

df['Depression_Risk'] = df['User Behavior Class'].apply(lambda x: 1 if x in [4, 5] else 0)
X = df[['App Usage Time (min/day)']]  
y = df['Depression_Risk'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

model = RandomForestClassifier(random_state=50)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

import joblib

# حفظ النموذج
joblib.dump(model, "depression_risk_modelf.pkl")
print("Model saved as depression_risk_modelf.pkl")
