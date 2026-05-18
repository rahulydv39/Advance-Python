import logging

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')


"""logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')"""

"""import helper"""

## using logger rules through config file
import logging.config
logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')


## try catch error with logging
"""
try:
    a=[1,2,3]
    val=a[4]
except IndexError as e:
    logging.error(e, exe_info = True)"""

## try catch error with logging but without telling error type
import traceback
try:
    a=[1,2,3]
    val=a[4]
except IndexError as e:
    logging.error("The error is %s", traceback.format_exc())