import pytest
from src.array_counter import count_element_occurrences

def test_count_element_occurrences():
    # Test basic case
    assert count_element_occurrences([1, 2, 3, 2, 2], 2) == 3
    
    # Test with string elements
    assert count_element_occurrences(['apple', 'banana', 'apple'], 'apple') == 2
    
    # Test with mixed type elements
    assert count_element_occurrences([1, '1', 1, '1'], 1) == 2
    
    # Test with empty array
    assert count_element_occurrences([], 5) == 0
    
    # Test with None input
    assert count_element_occurrences(None, 5) == 0
    
    # Test with no occurrences
    assert count_element_occurrences([1, 2, 3], 4) == 0