import pytest
from src.arithmetic_progression import has_arithmetic_progression

def test_has_arithmetic_progression():
    # Test cases with arithmetic progression
    assert has_arithmetic_progression([1, 2, 3]) == True  # Basic arithmetic progression
    assert has_arithmetic_progression([1, 3, 5]) == True  # Basic arithmetic progression
    assert has_arithmetic_progression([3, 5, 7]) == True  # Arithmetic progression
    assert has_arithmetic_progression([1, 2, 3, 4, 5]) == True  # Progression in middle
    assert has_arithmetic_progression([10, 7, 4, 1]) == True  # Decreasing progression

def test_no_arithmetic_progression():
    # Test cases without arithmetic progression
    assert has_arithmetic_progression([1, 2, 4]) == False  # Not a progression
    assert has_arithmetic_progression([1, 3, 6]) == False  # Not a progression
    assert has_arithmetic_progression([1, 1, 1]) == False  # Same numbers, not a real progression

def test_edge_cases():
    # Edge cases
    assert has_arithmetic_progression([1, 1, 1, 2, 3]) == True  # Progression later
    assert has_arithmetic_progression([]) == False  # Empty list
    assert has_arithmetic_progression([1]) == False  # Single element
    assert has_arithmetic_progression([1, 2]) == False  # Two elements

def test_input_validation():
    # Input validation tests
    with pytest.raises(ValueError, match="Input must be a list"):
        has_arithmetic_progression(123)
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        has_arithmetic_progression([1, 2, -3])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        has_arithmetic_progression([1, 2, 3.5])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        has_arithmetic_progression([1, 'a', 3])