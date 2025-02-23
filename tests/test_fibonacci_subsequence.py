import pytest
from src.fibonacci_subsequence import fibonacci_subsequence

def test_fibonacci_subsequence_standard_cases():
    # Test various standard subsequence lengths
    assert fibonacci_subsequence(1) == [0]
    assert fibonacci_subsequence(2) == [0, 1]
    assert fibonacci_subsequence(3) == [0, 1, 1]
    assert fibonacci_subsequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_subsequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_subsequence_error_cases():
    # Test error cases
    with pytest.raises(ValueError, match="Length must be a positive integer"):
        fibonacci_subsequence(0)
    
    with pytest.raises(ValueError, match="Length must be a positive integer"):
        fibonacci_subsequence(-1)

def test_fibonacci_subsequence_type_error():
    # Test type error cases
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_subsequence(3.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_subsequence("3")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_subsequence(None)