import pytest
from rectangleClass import Rectangle

def test_area():
    rectangle = Rectangle(2,5)
    assert rectangle.area() == 10