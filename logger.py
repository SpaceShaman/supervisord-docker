import logging
import os
import sys


def get_logger(
        logs_dir: str = '/var/log/supervisor/',
        log_format: str = '%(asctime)s @%(name)s [%(levelname)s]:    %(message)s'
) -> logging.Logger:
    """ Return an object Logger for logging to logs_dir directory.

    Args:
        logs_dir (str, optional): Folder where the logs are to be saved.
        log_format (str, optional): Log format.

    Returns:
        logging.Logger: Object of the Logger class for saving logs from the program.
    """
    script_name = sys.argv[0][sys.argv[0].rfind('/') + 1:-3]
    logs_path = f'{logs_dir}/{script_name}.log'

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
    logger.info('Start loging.')

    return logger
