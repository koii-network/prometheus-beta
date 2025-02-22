import pytest
from src.fibonacci_subsequence import fibonacci_subsequence

def test_fibonacci_subsequence_base_cases():
    assert fibonacci_subsequence(1) == [0]
    assert fibonacci_subsequence(2) == [0, 1]

def test_fibonacci_subsequence_longer_sequences():
    assert fibonacci_subsequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_subsequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_subsequence_invalid_inputs():
    with pytest.raises(TypeError):
        fibonacci_subsequence("3")
    
    with pytest.raises(TypeError):
        fibonacci_subsequence(3.5)
    
    with pytest.raises(ValueError):
        fibonacci_subsequence(0)
    
    with pytest.raises(ValueError):
        fibonacci_subsequence(-1)

def test_fibonacci_subsequence_large_n():
    result = fibonacci_subsequence(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]