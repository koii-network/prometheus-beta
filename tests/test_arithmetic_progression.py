import pytest
from src.arithmetic_progression import check_arithmetic_progression

def test_valid_arithmetic_progression():
    # Test cases where an arithmetic progression exists
    assert check_arithmetic_progression([1, 2, 3]) == True
    assert check_arithmetic_progression([1, 3, 5]) == True
    assert check_arithmetic_progression([2, 4, 6, 8, 10]) == True
    assert check_arithmetic_progression([5, 7, 9, 1, 2, 3]) == True

def test_no_arithmetic_progression():
    # Test cases where no arithmetic progression exists
    assert check_arithmetic_progression([1, 2, 4]) == False
    assert check_arithmetic_progression([1, 3, 6]) == False
    assert check_arithmetic_progression([5, 7, 8, 9, 10]) == False

def test_edge_cases():
    # Test edge cases
    assert check_arithmetic_progression([]) == False
    assert check_arithmetic_progression([1, 2]) == False
    assert check_arithmetic_progression([5]) == False

def test_invalid_input():
    # Test invalid input
    with pytest.raises(ValueError, match="Input must be a list"):
        check_arithmetic_progression("not a list")
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        check_arithmetic_progression([1, 2, -3])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        check_arithmetic_progression([1, 'a', 3])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        check_arithmetic_progression([0, 1, 2])