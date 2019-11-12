# Fuel Price Download

### Introduction
`fuelprice_download` is a Python project that is able to download fuel price data from the NSW Government website using their API (https://api.nsw.gov.au/fuel-price-check/apis)

The primary application of this is to collect fuel price data on an hourly basis for the purpose of analysis and visualisation (for the analysis and visualisation portion, see my `fuelprice` project).

### Overview
1. An API key was set up with the NSW government. The API key and secret are in a file called `private.py` (hidden with .gitignore but the underlying structure can be found in `private_template.py`. but is imported by `settings.py`. 
2. The following helper scripts were set up:
    - `db_writer.py`: Sets up an SQL connection with the database, allowing the user to read and write data using this established connection
    - `read_db.py`: Contains the function `read_data` which takes in an SQL query to read data from the database
    - `write_to_db`: Contains the function `write_data` which takes in an SQL query to write data to the database
    - `log.py`: Logging capabilities for debugging
3. The first script to run is `get_initial_fuel_price.py`. It sends a request to the API to get an initial data request which gets all the most recent fuel prices from each station. This data is formatted to an SQL friendly array and written into the SQL database.
4. Every subsequent request from here onwards uses `get_fuel_price.py` to write any new fuel prices. These requests are sent every hour and likewise are formatted and written into the SQL database.
5. If data is to be updated for the `fuelprice` project, then `download_data_from_database.py` can be used to run a data dump from the SQL database to the local machine as a .csv file.