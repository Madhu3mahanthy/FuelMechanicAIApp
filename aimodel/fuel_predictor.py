# fuel_predictor.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Dummy Dataset
data = {
    "fuel_type": ["Petrol", "Diesel", "Petrol", "Diesel", "Petrol"],
    "distance": [10, 20, 15, 25, 30],
    "amount_needed": [5, 8, 7, 10, 12]
}
df = pd.DataFrame(data)

# 2. Encode fuel_type
le = LabelEncoder()
df['fuel_type_encoded'] = le.fit_transform(df['fuel_type'])

# 3. Features and target
X = df[['fuel_type_encoded', 'distance']]
y = df['amount_needed']

# 4. Train model
model = LinearRegression()
model.fit(X, y)

# 5. Save model in this directory
joblib.dump(model, 'fuel_predictor_model.pkl')
print("✅ Model trained and saved as fuel_predictor_model.pkl")
