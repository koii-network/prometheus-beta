import pytest
from src.consecutive_char_sum import max_consecutive_char_sum

def test_max_consecutive_char_sum_basic():
    assert max_consecutive_char_sum('abcde') == 495  # a(97) + b(98) + c(99) + d(100) + e(101)
    assert max_consecutive_char_sum('abc') == 294    # a(97) + b(98) + c(99)

def test_max_consecutive_char_sum_multiple_sequences():
    assert max_consecutive_char_sum('abcmnpqr') == 216  # p(112) + q(113) + r(114)
    assert max_consecutive_char_sum('abcxyzpqr') == 216  # p(112) + q(113) + r(114)

def test_max_consecutive_char_sum_single_char():
    assert max_consecutive_char_sum('a') == 97
    assert max_consecutive_char_sum('z') == 122

def test_max_consecutive_char_sum_edge_cases():
    # Assert that only truly consecutive characters are counted
    assert max_consecutive_char_sum('acbde') == 101  # single e(101)
    assert max_consecutive_char_sum('axbycz') == 122  # just z(122)

def test_max_consecutive_char_sum_error_cases():
    with pytest.raises(TypeError):
        max_consecutive_char_sum(123)
    
    with pytest.raises(ValueError):
        max_consecutive_char_sum('')