import pytest
from '''name of folder''' import string_gen

def test_string_is_string():
    assert string_gen == str

def test_string_length():
    assert len(string_gen) == 5

def test_string_case():
    assert string_gen.islower == True