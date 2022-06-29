# A simple script presenting the work of the supervisord web interface.
import time

from logger import get_logger

if __name__ == '__main__':
    logger = get_logger()
    try:
        logger.info('Custom service started')
        while True:
            time.sleep(2)
    finally:
        logger.info('Custom service stopped')
