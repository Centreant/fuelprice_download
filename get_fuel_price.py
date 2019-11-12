import requests
import pandas as pd
import settings
import os.path
import write_to_db
import datetime
from log import logger

# Get current time
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Request data from API
response = requests.get('https://api.onegov.nsw.gov.au/FuelPriceCheck/v1/fuel/prices/new', headers=settings.headers)
if response.status_code == 200:
    logger.debug(f'Response code: {response.status_code}')
else:
    logger.critical(f'Response code: {response.status_code}')
    exit()

# Convert data to JSON file
data = response.json()
stations = pd.DataFrame(data['stations'])
prices = pd.DataFrame(data['prices'])

# Stop the program if there's no data
if prices.empty:
    logger.debug('No new prices found')
    exit()

# Set date type as datetime
prices['lastupdated'] = prices['lastupdated'].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'))

# Write data to csv in the /output for recording purposes
stations.to_csv(f'output/{current_time}_Stations.csv', index=False)
prices.to_csv(f'output/{current_time}_Prices.csv', index=False)

# Format station data
stations['loc_latitude'] = stations['location'].apply(lambda x: x['latitude'])
stations['loc_longitude'] = stations['location'].apply(lambda x: x['longitude'])
stations = stations.loc[:, ['code', 'name', 'address', 'brand', 'loc_latitude', 'loc_longitude']]
stations['code'] = stations['code'].astype(pd.np.int64)

# Merge stations data and fuelprice data
all_data = pd.merge(prices, stations, how='left', left_on='stationcode', right_on='code')

# Write data to database
write_to_db.write_data('INSERT INTO fuel_price (fuel_type, last_updated, price, station_code) VALUES (%s, %s, %s, %s)', prices.values.tolist())
