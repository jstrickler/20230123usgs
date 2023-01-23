
import logging

logging.basicConfig(
    format='%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(message)s', # format log entry
    datefmt="%Y:%M:%S::%X",  # set date/time format
    filename='../TEMP/loggers.log',
    level=logging.INFO,
)

logger_one = logging.getLogger(__name__ + "-1") # unique logger names
logger_two = logging.getLogger(__name__ + "-2")

logger_one.info("this is information")  # use logger 1
logger_two.warning("this is a warning")  # use logger 2
logger_one.info("this is information")
logger_two.critical("this is critical")
