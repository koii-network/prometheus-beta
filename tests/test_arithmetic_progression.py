import pytest
from src.arithmetic_progression import has_arithmetic_progression

def test_basic_arithmetic_progression():
    """Test basic arithmetic progression scenarios."""
    assert has_arithmetic_progression([1, 2, 3]) == True
    assert has_arithmetic_progression([1, 3, 5]) == True
    assert has_arithmetic_progression([2, 4, 6]) == True

def test_no_arithmetic_progression():
    """Test cases without an arithmetic progression."""
    assert has_arithmetic_progression([1, 2, 4]) == False
    assert has_arithmetic_progression([1, 3, 6]) == False
    assert has_arithmetic_progression([1, 2, 4, 8, 16]) == False

def test_longer_arrays_with_progression():
    """Test longer arrays containing arithmetic progressions."""
    assert has_arithmetic_progression([1, 2, 3, 4, 5]) == True
    assert has_arithmetic_progression([5, 7, 9, 11, 13]) == True
    assert has_arithmetic_progression([10, 7, 4, 1]) == True

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    assert has_arithmetic_progression([]) == False
    assert has_arithmetic_progression([1, 2]) == False
    assert has_arithmetic_progression([1]) == False

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a list"):
        has_arithmetic_progression(123)
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        has_arithmetic_progression([1, 2, -3])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        has_arithmetic_progression([1, 2, 3.5])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        has_arithmetic_progression([1, 'a', 3])

def test_multiple_progressions():
    """Test arrays with multiple possible progressions."""
    assert has_arithmetic_progression([1, 2, 3, 4, 5, 7]) == True
    assert has_arithmetic_progression([1, 3, 5, 2, 4, 6]) == True