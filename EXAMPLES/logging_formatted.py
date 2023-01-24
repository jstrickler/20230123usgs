import os
import logging

LOG_FOLDER =  "../LOGS"
LOG_NAME = 'formatted.log'
os.makedirs(LOG_FOLDER, exist_ok=True)
filename = os.path.join(LOG_FOLDER, LOG_NAME)

logging.basicConfig(
    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(message)s', # set the format for log entries
    datefmt="%x::%X",
    filename=filename,
    level=logging.INFO,
)

logging.info("this is information")
logging.warning("this is a warning")
logging.info("this is information")
logging.critical("this is critical")
