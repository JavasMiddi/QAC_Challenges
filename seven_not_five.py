import pytest
def snotf():
    final = []
    for x in range(2000, 3201):
        if x % 7 == 0:
            if x % 5 != 0:
                list1.append(x)
    return str(final).strip('[]')