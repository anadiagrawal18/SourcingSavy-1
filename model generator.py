import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Read price data from CSV
price_df = pd.read_csv('prices.csv')

# Function to train the model for a specific material
def train_model(material):
    # Feature engineering: Extract month and year from date
    price_df['Month'] = pd.to_datetime(price_df['Date']).dt.month
    price_df['Year'] = pd.to_datetime(price_df['Date']).dt.year

    # Split data into features and target
    X = price_df[['Month', 'Year']].values
    y = price_df[f'{material}_Price'].values

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest regressor
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Save the trained model
    model_filename = f'{material.lower()}_model.pkl'
    joblib.dump(rf_model, model_filename)

    return model_filename

# List of materials from the prices.csv file
materials = ['Steel', 'Coal', 'Wool', 'Aluminium', 'Crude_Oil', 'Natural_Gas', 'Nickel', 'Rubber', 'Gold', 'Silver', 'Platinum', 'Cement', 'Tiles', 'Pipes', 'Valves']

# Train models for each material
trained_models = {}
for material in materials:
    model_filename = train_model(material)
    trained_models[material] = model_filename

# Save the trained model filenames for future use
joblib.dump(trained_models, 'trained_models.pkl')

print("Model training completed successfully.")