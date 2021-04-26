import main
import pytest


def test_sales_tax():
    x = main.get_state()
    print(x)
    assert x == 4


def test_Wic_total():
    y = main.get_wic()
    print(y)
    assert y == 23


def test():
    print("test")

