import pytest
from src.longest_parity_subsequence import longest_parity_subsequence

def test_mixed_parity_array():
    """Test a mixed parity array with multiple subsequences"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = longest_parity_subsequence(arr)
    assert result == [2, 4, 6, 8, 10]

def test_all_even_array():
    """Test an array with all even numbers"""
    arr = [2, 4, 6, 8, 10]
    result = longest_parity_subsequence(arr)
    assert result == [2, 4, 6, 8, 10]

def test_all_odd_array():
    """Test an array with all odd numbers"""
    arr = [1, 3, 5, 7, 9]
    result = longest_parity_subsequence(arr)
    assert result == [1, 3, 5, 7, 9]

def test_empty_array():
    """Test an empty array"""
    arr = []
    result = longest_parity_subsequence(arr)
    assert result == []

def test_single_even_number():
    """Test an array with a single even number"""
    arr = [2]
    result = longest_parity_subsequence(arr)
    assert result == [2]

def test_single_odd_number():
    """Test an array with a single odd number"""
    arr = [1]
    result = longest_parity_subsequence(arr)
    assert result == [1]

def test_various_even_odd_subsequences():
    """Test array with various subsequences"""
    arr = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9]
    result = longest_parity_subsequence(arr)
    assert result == [4, 4, 6, 6, 8]

def test_invalid_input():
    """Test with invalid input"""
    with pytest.raises(ValueError):
        longest_parity_subsequence("not a list")
    with pytest.raises(ValueError):
        longest_parity_subsequence(None)