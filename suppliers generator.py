import pandas as pd
import numpy as np

# Define the number of suppliers
num_suppliers = 10

# Generate random latitude and longitude coordinates for supplier locations
latitudes = np.random.uniform(low=30, high=50, size=num_suppliers)  # Example latitude range: 30°N to 50°N
longitudes = np.random.uniform(low=-120, high=-70, size=num_suppliers)  # Example longitude range: 70°W to 120°W

# Generate random prices for the specified materials offered by suppliers
supplier_data = {
    'Supplier': [f'Supplier {i+1}' for i in range(num_suppliers)],
    'Latitude': latitudes,
    'Longitude': longitudes,
}
materials = ['Steel', 'Coal', 'Wool', 'Aluminium', 'Crude_Oil', 'Natural_Gas', 'Nickel', 'Rubber', 'Gold', 'Silver', 'Platinum', 'Cement', 'Tiles', 'Pipes', 'Valves']
for material in materials:
    material_prices = np.random.randint(50, 200, num_suppliers)  # Generate random prices for the material offered by suppliers
    supplier_data[f'{material}_Price'] = material_prices

# Generate random average transportation cost from each supplier
average_transportation_cost = np.random.uniform(low=1, high=5, size=num_suppliers)  # Example transportation cost range: $1 to $5
supplier_data['Average_Transportation_Cost'] = average_transportation_cost

# Create a DataFrame
suppliers_df = pd.DataFrame(supplier_data)

# Set NaN values for materials not offered by suppliers
suppliers_df = suppliers_df.fillna('Not Available')

# Save the DataFrame to a CSV file
suppliers_df.to_csv('suppliers.csv', index=False)

print("suppliers.csv file generated successfully.")
