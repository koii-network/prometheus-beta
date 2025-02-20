import pytest
import math
from src.fibonacci_extended import fibonacci_extended, fibonacci_interpolate

def test_positive_fibonacci():
    assert fibonacci_extended(5) == [0, 1, 1, 2, 3]
    assert fibonacci_extended(7) == [0, 1, 1, 2, 3, 5, 8]

def test_negative_fibonacci():
    assert fibonacci_extended(-5) == [5, -3, 2, -1, 1]
    assert fibonacci_extended(-6) == [8, -5, 3, -2, 1, -1]

def test_zero_fibonacci():
    assert fibonacci_extended(0) == []

def test_interpolate_integer_indices():
    assert fibonacci_interpolate(0) == 0
    assert fibonacci_interpolate(1) == 1
    assert fibonacci_interpolate(5) == 5

def test_interpolate_float_indices():
    # Check linear interpolation
    half_index_value = fibonacci_interpolate(1.5)
    assert math.isclose(half_index_value, 1.5, rel_tol=1e-9)

def test_error_handling():
    with pytest.raises(TypeError):
        fibonacci_extended("not an int")
    
    with pytest.raises(TypeError):
        fibonacci_interpolate("not a number")

def test_negative_interpolation():
    # Test interpolation for negative indices
    assert math.isclose(fibonacci_interpolate(-1.5), -0.5, rel_tol=1e-9)

def test_large_sequence():
    # Test a larger sequence generation
    large_seq = fibonacci_extended(10)
    assert len(large_seq) == 10
    assert large_seq[-1] == 34  # 9th Fibonacci number

def test_precise_float_indices():
    # More precise float index tests
    precise_value = fibonacci_interpolate(4.25)
    assert isinstance(precise_value, float)
    assert precise_value > 3 and precise_value < 5