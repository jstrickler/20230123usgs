"""
Demonstrate logging from modules
"""
import logging
logger = logging.getLogger(__name__)

def apple():
    logger.warning("ambergris")
    logger.info("arrivederci")
    logger.error("aspiration")
    logger.debug("Function apple()")
