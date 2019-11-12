# Import packages
from read_db import read_data
import pandas as pd

# Get price data
prices = read_data('SELECT * FROM fuel_price')
prices = pd.DataFrame(prices, columns=['id', 'fuel_type', 'last_updated', 'price', 'station_code'])

# Get stations data
stations = read_data("SELECT * FROM station")
stations = pd.DataFrame(stations, columns=['code', 'name', 'address', 'brand', 'loc_latitude', 'loc_longitude'])

# Merge data
all_data = pd.merge(prices, stations, how='left', left_on='station_code', right_on='code')

# Output data
all_data.to_csv('server_data.csv', index=False)