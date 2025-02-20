import pytest
from src.sum_numbers import sum_numbers

def test_sum_numbers_zero():
    """Test sum for 0"""
    assert sum_numbers(0) == 0

def test_sum_numbers_small_positive():
    """Test sum for small positive numbers"""
    assert sum_numbers(5) == 15  # 1 + 2 + 3 + 4 + 5
    assert sum_numbers(10) == 55  # 1 + 2 + ... + 10

def test_sum_numbers_large_number():
    """Test sum for a large number"""
    assert sum_numbers(100) == 5050  # Known result for 1 to 100

def test_sum_numbers_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_numbers(-1)

def test_sum_numbers_time_complexity():
    """Verify the solution is truly constant time"""
    import timeit
    
    # Time the function for a small input
    small_time = timeit.timeit(lambda: sum_numbers(10), number=10000)
    
    # Time the function for a large input
    large_time = timeit.timeit(lambda: sum_numbers(1000000), number=10000)
    
    # The time should be almost the same for small and large inputs
    assert abs(small_time - large_time) < small_time * 0.1, "Solution is not constant time"