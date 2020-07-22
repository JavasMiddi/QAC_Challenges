import pytest
from UniqueAlphaString import uas

def test_uas():
    assert uas("hello world and practice makes perfect and hello world again") == "again and hello makes perfect practice world"
    assert uas("foot red hair brown nose toes tongue foot and toenail") == "and brown foot hair nose red toenail toes tongue"
