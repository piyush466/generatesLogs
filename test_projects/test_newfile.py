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


@pytest.mark.smoke
def test_oneandonly():
    print("good test ")

