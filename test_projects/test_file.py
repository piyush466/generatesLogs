import pytest

from test_projects.test_logging import Test_newlogging


@pytest.mark.usefixtures('datatest')

class TestHello(Test_newlogging):

    def test_high(self, datatest):
        log = self.get_loggerrr()
        log.info(datatest[1])
        print(datatest[1])



