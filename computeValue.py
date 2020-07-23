import pytest

def compute(a):
    a = str(a)
    n1 = a * 1
    n2 = a * 2
    n3 = a * 3
    n4 = a * 4
    n5 = int(n1)+int(n2)+int(n3)+int(n4)
    return n5

def test_compute():
    assert compute(9) == 11106
    assert compute(3) == 3702
