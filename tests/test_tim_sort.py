import pytest
from src.tim_sort import tim_sort

def test_tim_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert tim_sort(arr) == []

def test_tim_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [5]
    assert tim_sort(arr) == [5]

def test_tim_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tim_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_tim_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, 3, -2, 0, 7, -1, 10]
    assert tim_sort(arr) == [-5, -2, -1, 0, 3, 7, 10]

def test_tim_sort_mixed_types():
    """Test sorting a list with different numeric types."""
    arr = [5, 3.14, 2, -1, 0, 7]
    assert tim_sort(arr) == [-1, 0, 2, 3.14, 5, 7]

def test_tim_sort_large_list():
    """Test sorting a large list to simulate real-world scenario."""
    import random
    random.seed(42)  # For reproducibility
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    sorted_arr = tim_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_tim_sort_performance():
    """Ensure Tim Sort is reasonably performant."""
    import random
    import time
    
    # Create a large list for performance testing
    random.seed(42)
    arr = [random.randint(-10000, 10000) for _ in range(10000)]
    
    # Measure sorting time
    start_time = time.time()
    tim_sort(arr)
    end_time = time.time()
    
    # Ensure sorting takes less than 1 second
    assert end_time - start_time < 1.0