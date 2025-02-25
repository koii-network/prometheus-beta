import pytest
from src.letter_case_balance import check_letter_case_balance

def test_balanced_simple():
    """Test a simple balanced case"""
    assert check_letter_case_balance('aBcD') == 'Balanced'

def test_balanced_with_spaces_and_punctuation():
    """Test a balanced case with spaces and punctuation"""
    assert check_letter_case_balance('aB cD! eF?') == 'Balanced'

def test_not_balanced_more_uppercase():
    """Test a case with more uppercase letters"""
    assert check_letter_case_balance('aaBCD') == 'Not Balanced'

def test_not_balanced_more_lowercase():
    """Test a case with more lowercase letters"""
    assert check_letter_case_balance('AABcd') == 'Not Balanced'

def test_only_uppercase():
    """Test a case with only uppercase letters"""
    assert check_letter_case_balance('ABCD') == 'Not Balanced'

def test_only_lowercase():
    """Test a case with only lowercase letters"""
    assert check_letter_case_balance('abcd') == 'Not Balanced'

def test_no_letters_raises_error():
    """Test that strings without letters raise a ValueError"""
    with pytest.raises(ValueError, match="Input string must contain at least one letter"):
        check_letter_case_balance('123 !@#')

def test_mixed_complex_not_balanced():
    """Test a more complex not balanced case"""
    assert check_letter_case_balance('Hello, World!') == 'Not Balanced'

def test_mixed_complex_balanced():
    """Test a more complex balanced case"""
    assert check_letter_case_balance('HeLlo, WoRld!') == 'Not Balanced'