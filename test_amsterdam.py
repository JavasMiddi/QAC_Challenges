import pytest
from amsterdam import name
def test_amsterdam():
    assert name("Am I in Amsterdam") == 1
    assert name("I am in Amsterdam am I?") == 2
    assert name("I have been in Amsterdam") == 0
    assert name("Am I in Amsterdam I am am I") == 3