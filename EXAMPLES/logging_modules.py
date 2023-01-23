import logging

logging.basicConfig(level=logging.DEBUG, filename="../TEMP/modules.log")

logger = logging.getLogger(__name__)

from apple import apple
from banana import banana
from cherry import cherry

def main():
    logger.info("Starting main script")
    apple()
    banana()
    cherry()
    logger.info("Ending main script")

if __name__ == '__main__':
    main()
