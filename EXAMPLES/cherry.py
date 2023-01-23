"""
Demonstrate logging from modules
"""
import logging
logger = logging.getLogger(__name__)

def cherry():
    logger.warning("ciao bello")
    logger.info("Cartesian")
    logger.error("cobblestones")
    logger.debug("Function cherry()")
