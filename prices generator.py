import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the number of data points
num_data_points = 500

# Generate random dates for the past two years
start_date = datetime.now() - timedelta(days=365 * 2)
end_date = datetime.now()
dates = pd.date_range(start=start_date, end=end_date, periods=num_data_points)

# Generate random prices for the specified materials
steel_prices = np.random.randint(80, 120, num_data_points)
coal_prices = np.random.randint(50, 90, num_data_points)
wool_prices = np.random.randint(10, 30, num_data_points)
aluminium_prices = np.random.randint(1000, 1500, num_data_points)
crude_oil_prices = np.random.randint(40, 80, num_data_points)
natural_gas_prices = np.random.randint(1, 5, num_data_points)
nickel_prices = np.random.randint(500, 800, num_data_points)
rubber_prices = np.random.randint(100, 200, num_data_points)
gold_prices = np.random.randint(1500, 2000, num_data_points)
silver_prices = np.random.randint(20, 30, num_data_points)
platinum_prices = np.random.randint(800, 1200, num_data_points)
cement_prices = np.random.randint(70, 120, num_data_points)
tiles_prices = np.random.randint(20, 40, num_data_points)
pipes_prices = np.random.randint(40, 80, num_data_points)
valves_prices = np.random.randint(30, 60, num_data_points)

# Create a DataFrame
data = {
    'Date': dates,
    'Steel_Price': steel_prices,
    'Coal_Price': coal_prices,
    'Wool_Price': wool_prices,
    'Aluminium_Price': aluminium_prices,
    'Crude_Oil_Price': crude_oil_prices,
    'Natural_Gas_Price': natural_gas_prices,
    'Nickel_Price': nickel_prices,
    'Rubber_Price': rubber_prices,
    'Gold_Price': gold_prices,
    'Silver_Price': silver_prices,
    'Platinum_Price': platinum_prices,
    'Cement_Price': cement_prices,
    'Tiles_Price': tiles_prices,
    'Pipes_Price': pipes_prices,
    'Valves_Price': valves_prices
}
prices_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
prices_df.to_csv('prices.csv', index=False)

print("prices.csv file generated successfully.")
