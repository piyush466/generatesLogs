import inspect
import logging


class Baseclasses:

    def get_logger(self):
        # loggername = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('generate.log')
        formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")

        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)

        return logger

