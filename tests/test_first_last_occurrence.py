import pytest
from src.first_last_occurrence import find_first_last_occurrence

def test_find_first_last_occurrence():
    # Test case 1: Element exists multiple times
    arr1 = [1, 2, 2, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr1, 2) == (1, 3)
    
    # Test case 2: Element exists only once
    arr2 = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr2, 3) == (2, 2)
    
    # Test case 3: Element not in the array
    arr3 = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr3, 6) == (-1, -1)
    
    # Test case 4: Empty array
    arr4 = []
    assert find_first_last_occurrence(arr4, 1) == (-1, -1)
    
    # Test case 5: All elements are the same
    arr5 = [2, 2, 2, 2, 2]
    assert find_first_last_occurrence(arr5, 2) == (0, 4)
    
    # Test case 6: First and last elements
    arr6 = [1, 1, 2, 3, 4, 5, 5]
    assert find_first_last_occurrence(arr6, 1) == (0, 1)
    assert find_first_last_occurrence(arr6, 5) == (5, 6)

def test_edge_cases():
    # Test negative numbers
    arr_neg = [-3, -2, -2, -1, 0, 1, 2]
    assert find_first_last_occurrence(arr_neg, -2) == (1, 2)
    
    # Test large array
    arr_large = list(range(1000)) + list(range(1000, 2000)) + list(range(2000))
    assert find_first_last_occurrence(arr_large, 1500) == (1500, 1500)

def test_type_handling():
    # Test different types of elements
    arr_mixed = [1, 2, 'a', 'a', 'b']
    assert find_first_last_occurrence(arr_mixed, 'a') == (2, 3)
    
    # Uncomment to verify type safety (optional)
    # with pytest.raises(TypeError):
    #     find_first_last_occurrence([1, 2, 3], '2')