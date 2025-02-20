import pytest
from src.valid_sequence import is_valid_increasing_sequence

def test_valid_increasing_sequence():
    # Test valid sequences
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True
    
    # Test invalid sequences
    assert is_valid_increasing_sequence([]) == False  # Empty array
    assert is_valid_increasing_sequence([1]) == True  # Single element is valid
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False  # Decreasing order
    assert is_valid_increasing_sequence([1, 1, 2, 3]) == False  # Duplicate elements
    assert is_valid_increasing_sequence([1, 2, 2, 3]) == False  # Duplicate elements
    
    # Test edge cases
    assert is_valid_increasing_sequence([-5, -4, -3, -2, -1]) == True  # Negative numbers
    assert is_valid_increasing_sequence([1, 3, 2, 4]) == False  # Not strictly increasing
    assert is_valid_increasing_sequence([1, 1]) == False  # No duplicates allowed