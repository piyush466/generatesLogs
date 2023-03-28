# import logging
#
# def test_logging():
#     logger = logging.getLogger(__name__)
#
#     filehandler = logging.FileHandler("logfile.log")
#     formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#     filehandler.setFormatter(formatter)
#
#     logger.addHandler(filehandler)
#
#     logger.setLevel(logging.DEBUG)
#     logger.debug("This is a debug")
#     logger.info("This is a info")
#     logger.warning('this is a warning')
#     logger.error('This is a error')
#     logger.critical("this is a critical")



import logging

class Test_newlogging:
    def get_loggerrr(self):
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('generate.log')
        formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")

        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        logger.debug("this is debuggg")
        logger.error("this is debuggg")
        logger.info("this is debuggg")
        logger.critical("this is debuggg")
        logger.warning("this is debuggg")


























