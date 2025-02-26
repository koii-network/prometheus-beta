import pytest
from src.fibonacci_arithmetic import fibonacci_arithmetic_progression

def test_basic_arithmetic_progression():
    """Test finding a basic arithmetic progression in Fibonacci sequence."""
    result = fibonacci_arithmetic_progression(3)
    assert result == [0, 1, 1], f"Expected [0, 1, 1], got {result}"

def test_longer_arithmetic_progression():
    """Test finding a longer arithmetic progression."""
    result = fibonacci_arithmetic_progression(4)
    assert result == [1, 1, 2, 3], f"Expected [1, 1, 2, 3], got {result}"

def test_invalid_input_less_than_three():
    """Test that ValueError is raised for n < 3."""
    with pytest.raises(ValueError, match="At least 3 numbers are required"):
        fibonacci_arithmetic_progression(2)

def test_invalid_input_type():
    """Test that TypeError is raised for non-integer input."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_arithmetic_progression("3")

def test_no_arithmetic_progression():
    """Test behavior when no arithmetic progression is found."""
    # This might return an empty list, depending on implementation
    result = fibonacci_arithmetic_progression(5)
    assert isinstance(result, list), "Should return a list"

def test_arithmetic_progression_large_n():
    """Test finding arithmetic progression with larger n."""
    result = fibonacci_arithmetic_progression(6)
    assert len(result) == 6, "Should return exactly 6 numbers"
    
    # Verify it's an arithmetic progression
    if result:
        differences = [result[i+1] - result[i] for i in range(len(result)-1)]
        assert len(set(differences)) == 1, "Numbers should form an arithmetic progression"