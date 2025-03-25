import inspect
import logging
import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandlar = logging.FileHandler('../CustomerLogin/logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        fileHandlar.setFormatter(formatter)

        logger.addHandler(fileHandlar)  # file handle object
        logger.setLevel(logging.DEBUG)
        return logger