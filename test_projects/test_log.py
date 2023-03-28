import logging

def test_log():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logtest.log')
    formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")

    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    logger.setLevel(logging.DEBUG)

    logger.debug("this is a debug issue")
    logger.info("This is a info issue")
    logger.error("this is a eroor")
    logger.warning("this is a warning")
    logger.critical("this is a critical")


