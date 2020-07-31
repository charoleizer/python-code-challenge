import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from core import calculator


def test_sum_custom_positive():

    if not (int(calculator.sum_custom("1,4,7,88,2,5")) == 107):
        raise AssertionError()


def test_sum_custom_negative():

    if not (int(calculator.sum_custom("-1,-4,-7,-88,-2,-5")) == -107):
        raise AssertionError()


def test_sum_custom_mix():

    if not (int(calculator.sum_custom("1,4,7,-88,-2,-5,-32,12")) == -103):
        raise AssertionError()


def test_substract_custom_positive():

    if not (int(calculator.substract_custom("1,4,7,88,2,5")) == -105):
        raise AssertionError()


def test_substract_custom_negative():

    if not (int(calculator.substract_custom("-1,-4,-7,-88,-2,-5")) == 105):
        raise AssertionError()


def test_substract_custom_mix():

    if not (int(calculator.substract_custom("1,4,7,-88,-2,-5,-32,12")) == 105):
        raise AssertionError()
