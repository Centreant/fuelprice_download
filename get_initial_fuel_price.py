import requests
import pandas as pd
import settings
import write_to_db
import datetime

from write_to_db import write_data

# Request data from API
response = requests.get('https://api.onegov.nsw.gov.au/FuelPriceCheck/v1/fuel/prices', headers=settings.headers)
data = response.json()
stations = pd.DataFrame(data['stations'])
prices = pd.DataFrame(data['prices'])

# Set date type as datetime
prices['lastupdated'] = prices['lastupdated'].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'))

# Write data as csv
stations.to_csv('Master_Stations.csv', index=False)
prices.to_csv('Master_Prices.csv', index=False)

# Write data to database
write_data('INSERT INTO fuel_price (fuel_type, last_updated, price, station_code) VALUES (%s, %s, %s, %s)', prices.values.tolist())