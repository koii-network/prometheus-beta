import pytest
from src.tim_sort import tim_sort, insertion_sort, merge

def test_insertion_sort():
    # Test basic insertion sort
    arr = [5, 2, 9, 1, 7, 6]
    assert insertion_sort(arr.copy()) == sorted(arr)
    
    # Test already sorted array
    arr_sorted = [1, 2, 3, 4, 5]
    assert insertion_sort(arr_sorted.copy()) == arr_sorted
    
    # Test reverse sorted array
    arr_reverse = [5, 4, 3, 2, 1]
    assert insertion_sort(arr_reverse.copy()) == sorted(arr_reverse)
    
    # Test with partial array
    arr_partial = [5, 2, 9, 1, 7, 6]
    assert insertion_sort(arr_partial.copy(), 1, 3) == [5, 1, 2, 9, 7, 6]

def test_merge():
    # Test basic merge
    arr = [1, 3, 5, 2, 4, 6]
    merge(arr, 0, 2, 5)
    assert arr == [1, 2, 3, 4, 5, 6]
    
    # Test merge with different sized subarrays
    arr = [1, 3, 5, 2, 4]
    merge(arr, 0, 2, 4)
    assert arr == [1, 2, 3, 4, 5]

def test_tim_sort():
    # Test empty array
    assert tim_sort([]) == []
    
    # Test single element array
    assert tim_sort([1]) == [1]
    
    # Test already sorted array
    arr_sorted = [1, 2, 3, 4, 5]
    assert tim_sort(arr_sorted.copy()) == arr_sorted
    
    # Test reverse sorted array
    arr_reverse = [5, 4, 3, 2, 1]
    assert tim_sort(arr_reverse.copy()) == sorted(arr_reverse)
    
    # Test random array
    arr_random = [5, 2, 9, 1, 7, 6, 3, 8, 4]
    assert tim_sort(arr_random.copy()) == sorted(arr_random)
    
    # Test array with duplicates
    arr_duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tim_sort(arr_duplicates.copy()) == sorted(arr_duplicates)
    
    # Test large array
    arr_large = list(range(1000, 0, -1))
    assert tim_sort(arr_large.copy()) == sorted(arr_large)

def test_tim_sort_stability():
    # Test stability by sorting complex objects
    data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 25},
        {'name': 'David', 'age': 30}
    ]
    
    # Sort by age first
    sorted_by_age = sorted(data, key=lambda x: x['age'])
    tim_sorted = tim_sort(data.copy())
    
    # Check if relative order of equal age elements is preserved
    assert [x['name'] for x in sorted_by_age] == [x['name'] for x in tim_sorted]