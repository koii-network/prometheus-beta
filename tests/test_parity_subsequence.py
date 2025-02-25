import pytest
from src.parity_subsequence import find_longest_parity_subsequence

def test_mixed_list_even_longer():
    """Test a mixed list where the even subsequence is longer"""
    result = find_longest_parity_subsequence([1, 2, 3, 4, 5, 6, 7, 8])
    assert result == [2, 4, 6, 8]

def test_mixed_list_odd_longer():
    """Test a mixed list where the odd subsequence is longer"""
    result = find_longest_parity_subsequence([1, 2, 3, 4, 5, 6, 7, 9])
    assert result == [1, 3, 5, 7, 9]

def test_single_even_number():
    """Test with a single even number"""
    result = find_longest_parity_subsequence([4])
    assert result == [4]

def test_single_odd_number():
    """Test with a single odd number"""
    result = find_longest_parity_subsequence([3])
    assert result == [3]

def test_all_even_numbers():
    """Test a list of all even numbers"""
    result = find_longest_parity_subsequence([2, 4, 6, 8, 10])
    assert result == [2, 4, 6, 8, 10]

def test_all_odd_numbers():
    """Test a list of all odd numbers"""
    result = find_longest_parity_subsequence([1, 3, 5, 7, 9])
    assert result == [1, 3, 5, 7, 9]

def test_alternating_parity():
    """Test an alternating parity list"""
    result = find_longest_parity_subsequence([1, 2, 3, 4, 5, 6])
    assert result == [2, 4, 6]

def test_equal_length_subsequences():
    """Test case where even and odd subsequences are equal length"""
    result = find_longest_parity_subsequence([1, 2, 3, 4])
    assert result == [2, 4]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        find_longest_parity_subsequence("not a list")

def test_empty_list():
    """Test that ValueError is raised for empty list"""
    with pytest.raises(ValueError):
        find_longest_parity_subsequence([])