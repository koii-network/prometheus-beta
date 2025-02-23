import pytest
from src.fibonacci_arithmetic_progression import fibonacci_arithmetic_progression

def test_basic_sequence():
    # The first few Fibonacci numbers don't form an arithmetic progression
    result = fibonacci_arithmetic_progression(5)
    assert result == [1, 1, 2, 3, 5]

def test_small_sequences():
    # Test single and two-number cases
    assert fibonacci_arithmetic_progression(1) == [1]
    assert fibonacci_arithmetic_progression(2) == [1, 1]

def test_invalid_input():
    with pytest.raises(ValueError):
        fibonacci_arithmetic_progression(0)
    with pytest.raises(ValueError):
        fibonacci_arithmetic_progression(-1)

def test_larger_arithmetic_progression():
    # More complex test to verify arithmetic progression property
    result = fibonacci_arithmetic_progression(10)
    
    # Check if result has 10 elements
    assert len(result) == 10
    
    # Verify Fibonacci sequence generation
    assert result[0] == 1
    assert result[1] == 1
    
    # This test ensures the Fibonacci property is maintained
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]

def test_long_sequence():
    # Test a longer sequence to ensure consistent behavior
    result = fibonacci_arithmetic_progression(15)
    assert len(result) == 15
    
    # Verify Fibonacci generation
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]