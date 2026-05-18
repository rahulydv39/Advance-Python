import logging
logger = logging.getLogger(__name__)
# to don't log anything
"""logger.propagate = False"""

"""
logger.info('hello from helper')"""

### to create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level of the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')