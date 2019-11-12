import settings
import pandas as pd
import sys
import datetime
from db_writer import SQL_connection
from log import logger

def write_data(sql, val):
    try:
        with SQL_connection() as connection:
            logger.debug('Begin writing to DB - creating cursor')
            cursor = connection.cursor()
            logger.debug('Executing cursor')
            cursor.executemany(sql, val)
            connection.commit()            
        logger.debug('Finished context with writer - commit')
        logger.debug('Finished writing to db')
    except Exception:
        logger.exception('Error encountered while writing to file', exc_info=False)