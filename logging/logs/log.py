import logging

logging.basicConfig(
    filename = 'app.log',  # Log messages will be written to this file
    filemode = 'w',  # Overwrite the log file on each run
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
)
