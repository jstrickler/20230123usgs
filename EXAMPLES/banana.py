"""
Demonstrate logging from modules
"""
import logging
logger = logging.getLogger(__name__)

def banana():
    logger.warning("bravo")
    logger.info("Barbarella")
    logger.error("broccoli")
    logger.debug("banana()")
