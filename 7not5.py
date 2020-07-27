import pytest
from random import randint
def snotf():
    list1 = []
    for x in range(2000, 3201):
        if x % 7 == 0:
            if x % 5 != 0:
                list1.append(x)
    
    return str(list1).strip('[]')
    
def test_seven():
    pass