from db_writer import SQL_connection
from log import logger

def read_data(sql):
    """
    Read the database with an SQL query.
    fuel_price: 'id', 'fuel_type', 'last_updated', 'price', 'station_code'
    station: 'code', 'name', 'address', 'brand', 'loc_latitude', 'loc_longitude'
    """
    try:
        with SQL_connection() as connection:
            logger.debug('Begin reading from DB - creating cursor')
            cursor = connection.cursor()
            logger.debug('Executing cursor')
            cursor.execute(sql)
            logger.debug('Fetching results from cursor')
            result = cursor.fetchall()        
            logger.debug('Finished reading from database, returning results')
        return result
    except Exception:
        logger.error('Error encountered while reading from file', exc_info=False)