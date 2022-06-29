import logging
import os
import sys
import time

# INIT LOGGING
script_name = sys.argv[0][sys.argv[0].rfind('/') + 1:-3]
logs_dir = 'log/'
logs_path = f'{logs_dir}/{script_name}.log'
log_format = '%(asctime)s @%(name)s [%(levelname)s]:    %(message)s'

try:
    open(logs_path)
except IOError:
    os.makedirs(os.path.dirname(logs_dir), exist_ok=True)
    file = open(logs_path, 'x')
    file.close()

logging.basicConfig(filename=logs_path,
                    filemode="a",
                    format=log_format,
                    level=logging.INFO)

logger = logging.getLogger()

logger.info('Start loging')

if __name__ == '__main__':
    try:
        logger.info('Custom service started')
        while True:
            # here for the sake of example, actually doing real stuff here
            time.sleep(2)
    finally:
        logger.info('Custom service stopped')
