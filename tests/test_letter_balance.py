import pytest
from src.letter_balance import check_letter_balance

def test_balanced_strings():
    assert check_letter_balance("AbCdEfG") == 'Balanced'
    assert check_letter_balance("Hello World") == 'Balanced'
    assert check_letter_balance("aA") == 'Balanced'

def test_unbalanced_strings():
    assert check_letter_balance("Hello") == 'Not Balanced'
    assert check_letter_balance("WORLD") == 'Not Balanced'
    assert check_letter_balance("Python") == 'Not Balanced'

def test_edge_cases():
    assert check_letter_balance("") == 'Not Balanced'
    assert check_letter_balance("123!@#") == 'Not Balanced'
    assert check_letter_balance(" ") == 'Not Balanced'

def test_mixed_strings():
    assert check_letter_balance("aA!@#") == 'Balanced'
    assert check_letter_balance("Hello WORLD!") == 'Not Balanced'
    assert check_letter_balance("Python LANGUAGE 123") == 'Not Balanced'