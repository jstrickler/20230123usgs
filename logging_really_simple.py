import logging

def spam():
    print("spam spam spam")
    logging.error("YIKES!!!")
    logging.warning("spam() called")
    logging.info("something happened")

spam()
spam()