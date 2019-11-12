import logging
logging.basicConfig(filename='Fuel_Price_Log.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logging.info("")

logger = logging.getLogger('logger')
logger.debug('Finished writing to db')