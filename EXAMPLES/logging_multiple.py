import sys
import logging
import logging.handlers
from getpass import getpass

# logging.basicConfig(level=logging.DEBUG, format="huh??")

LOG_FILENAME = '../TEMP/multiple.log'

# set up formatting for all handlers (but could be different for each)
formatter = logging.Formatter(
    '%(levelname)-9s %(name)s %(asctime)s %(message)s',
    '%x %X',
)  # create formatter for all logs


# log to STDOUT for DEBUG and higher
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

# log to a file for all levels INFO and higher
file_handler = logging.FileHandler(LOG_FILENAME)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


# log to email for CRITICAL
smtp_password = getpass("smtp password: ")

email_handler = logging.handlers.SMTPHandler(
    ('smtp2go.com', 2525),
    f'{__name__}@pythonclass.com',
    ['jstrickler@gmail.com'],
    'ThisApplication Log Entry',
    ('pythonclass', smtp_password),
)
email_handler.setLevel(logging.CRITICAL)

testlogger = logging.getLogger('TestLogger')  # create Logger object
testlogger.propagate = False # don't use default logger

testlogger.addHandler(stream_handler)
testlogger.addHandler(file_handler)
# testlogger.addHandler(email_handler)

# list handlers
print("HANDLERS:")
for handler in testlogger.handlers:
    print(handler)
print()

testlogger.setLevel(logging.DEBUG)  # optional

testlogger.debug("alpha")
testlogger.info("beta")
testlogger.warning("gamma")
testlogger.error("delta")
testlogger.critical("epsilon")
testlogger.warning('zeta')
testlogger.warning('eta')
testlogger.critical("theta")
testlogger.debug("iota")
testlogger.error("kappa")
testlogger.warning("lambda")
testlogger.warning("mu")
testlogger.warning("nu")
testlogger.critical("rho")
