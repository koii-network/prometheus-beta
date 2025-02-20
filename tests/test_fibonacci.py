import pytest
from src.fibonacci import fibonacci_sequence

def test_fibonacci_sequence_zero():
    """Test generating 0 elements."""
    assert fibonacci_sequence(0) == []

def test_fibonacci_sequence_one():
    """Test generating 1 element."""
    assert fibonacci_sequence(1) == [0]

def test_fibonacci_sequence_two():
    """Test generating 2 elements."""
    assert fibonacci_sequence(2) == [0, 1]

def test_fibonacci_sequence_multiple():
    """Test generating multiple Fibonacci sequence elements."""
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_sequence_large_n():
    """Test generating a larger sequence."""
    sequence = fibonacci_sequence(10)
    assert len(sequence) == 10
    assert sequence == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_sequence_invalid_input():
    """Test handling of invalid inputs."""
    with pytest.raises(TypeError):
        fibonacci_sequence("not an integer")
    
    with pytest.raises(ValueError):
        fibonacci_sequence(-1)

def test_fibonacci_sequence_performance():
    """Quick performance test to ensure reasonable performance."""
    import timeit
    
    def measure_fibonacci():
        fibonacci_sequence(20)
    
    execution_time = timeit.timeit(measure_fibonacci, number=1000)
    assert execution_time < 1.0  # Should complete 1000 runs under 1 second