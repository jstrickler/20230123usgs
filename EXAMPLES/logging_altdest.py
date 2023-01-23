import sys
import logging
import logging.handlers

logger = logging.getLogger('ThisApplication')  # get logger for application
logger.setLevel(logging.DEBUG)  # minimum log level

if sys.platform == 'win32':
    eventlog_handler = logging.handlers.NTEventLogHandler("Python Log Test")  # create NT event log handler
    logger.addHandler(eventlog_handler)  # install NT event handler
else:
    syslog_handler = logging.handlers.SysLogHandler()  # create syslog handler
    logger.addHandler(syslog_handler)  # install syslog handler

# note -- use your own SMTP server...
email_handler = logging.handlers.SMTPHandler(
    ('smtpcorp.com', 8025),
    'LOGGER@pythonclass.com',
    ['jstrick@mindspring.com'],
    'ThisApplication Log Entry',
    ('jstrickpython', 'python(monty)'),
)  # create email handler

logger.addHandler(email_handler)  # install email handler

logger.debug('this is debug')  # goes to all handlers
logger.critical('this is critical')  # goes to all handlers
logger.warning('this is a warning')  # goes to all handlers
