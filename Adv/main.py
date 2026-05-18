import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)

# s, m, h, d, midnight, w0
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('hello. World!')
    time.sleep(5)