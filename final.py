import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2
import joblib

# Constants for transportation speeds (in km/h)
TRANSPORTATION_SPEEDS = {
    'truck': 60,  # Average truck speed on roads
    'train': 80,  # Average train speed on railways
    'ship': 25    # Average ship speed on waterways
}

# Function to calculate the transportation time in hours
def calculate_transportation_time(distance, mode):
    speed = TRANSPORTATION_SPEEDS.get(mode, 60)  # Default to truck speed if mode is not found
    return distance / speed

# Function to calculate the distance between two geographical points using the Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of the Earth in kilometers
    return distance

# Load the trained models
trained_models = joblib.load('trained_models.pkl')

# Read supplier data from CSV
supplier_df = pd.read_csv('suppliers.csv')

# Function to find the best supplier based on cost and distance for a specific material
def find_best_supplier(material, construction_site_lat, construction_site_lon, quantity, supplier_df):
    min_cost = float('inf')
    best_supplier = None
    for index, row in supplier_df.iterrows():
        if row[f'{material}_Price'] != 'Not Available':
            supplier_cost = row[f'{material}_Price']
            supplier_lat = row['Latitude']
            supplier_lon = row['Longitude']
            distance = calculate_distance(construction_site_lat, construction_site_lon, supplier_lat, supplier_lon)
            transportation_cost = row['Average_Transportation_Cost']
            total_cost = supplier_cost * quantity + distance * transportation_cost  # Including transportation cost and quantity
            if total_cost < min_cost:
                min_cost = total_cost
                best_supplier = row['Supplier']
                supplier_distance = distance
    return best_supplier, min_cost, supplier_distance

# Function to predict material price for the future date
def predict_material_price(material, future_month, future_year):
    model_filename = trained_models[material]
    model = joblib.load(model_filename)
    return model.predict([[future_month, future_year]])[0]

# Sample construction site location (you should replace this with actual coordinates)
construction_site_lat = 37.7749
construction_site_lon = -122.4194

# Input material, quantity, and future date
material = input("Enter the material: ")
quantity = float(input("Enter the quantity needed (in metric tonns): "))
future_month = int(input("Enter the future month (1-12): "))
future_year = int(input("Enter the future year: "))

# Predict material price
predicted_material_price = predict_material_price(material, future_month, future_year)

# Select the best supplier for the material
best_supplier, total_cost, supplier_distance = find_best_supplier(material, construction_site_lat, construction_site_lon, quantity, supplier_df)

# Calculate the transportation time for each mode of transportation
transportation_times = {}
for mode in TRANSPORTATION_SPEEDS:
    transportation_time = calculate_transportation_time(supplier_distance, mode)
    transportation_times[mode] = transportation_time

print(f"Predicted price of {material} for {future_month}/{future_year}: ${predicted_material_price:.2f} per unit")
print(f"Best {material} supplier: {best_supplier}")
print(f"Total Cost for {quantity} units from {best_supplier}: ${total_cost:.2f}")
print(f"Distance to {best_supplier}: {supplier_distance:.2f} kilometers")
