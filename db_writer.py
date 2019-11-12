import mysql.connector
import logging
import settings

logger = logging.getLogger('main')

class SQL_connection(object):
    def __enter__(self):
        try:
            logger.debug('Connecting to the database - using context')
            self.conn = mysql.connector.connect(host=settings.HOST, user=settings.USER, 
                                                passwd=settings.PASSWD, database=settings.DATABASE, 
                                                auth_plugin=settings.AUTH_PLUGIN)
            logger.debug('Connected to the database')
            return self.conn
        except Exception:
            logger.exception('Unable to create connection to the database', exc_info=False)
    
    def __exit__(self, type, value, traceback):
        try:
            self.conn.close()
        except Exception:
            logger.Exception('Unable to close connection')
            
        
