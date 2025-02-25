import pytest
from src.triangular_number import calculate_triangular_number

def test_triangular_number_basic():
    """Test basic triangular number calculations."""
    assert calculate_triangular_number(1) == 1
    assert calculate_triangular_number(2) == 3
    assert calculate_triangular_number(3) == 6
    assert calculate_triangular_number(4) == 10
    assert calculate_triangular_number(5) == 15

def test_triangular_number_larger_values():
    """Test triangular number calculations for larger values."""
    assert calculate_triangular_number(10) == 55
    assert calculate_triangular_number(20) == 210
    assert calculate_triangular_number(100) == 5050

def test_triangular_number_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        calculate_triangular_number(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        calculate_triangular_number(-5)

def test_triangular_number_type_errors():
    """Test type error handling."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number(None)