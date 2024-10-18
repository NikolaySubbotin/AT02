import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("проверка гласных") == 5

def test_no_vowels():
    assert count_vowels("рднпк") == 0


def test_mixed_strings():
    assert count_vowels("Привет") == 2


def test_empty_string():
    assert count_vowels("") == 0
