# import pytest
#
#
# def test_piyushtesting():
#     print("good test ")
#
#
# @pytest.mark.regression
# def test_akashtesting():
#     print('new test')
#
#
# @pytest.mark.regression
# def test_good():
#     print('this is good test')
import pytest

from test_projects.BaseClass import Baseclasses


# @pytest.mark.usefixtures('datatest')
class Test_Example(Baseclasses):
    def test_oneandonly(self, datatest):
        log = self.get_logger()
        log.info(datatest[1])
        log.info(datatest[0])
        print(datatest[2])

        print("good test ")

