import pytest
from src.power_of_two import is_power_of_two

def test_power_of_two_positive_cases():
    """Test numbers that are powers of two."""
    assert is_power_of_two(1) == True
    assert is_power_of_two(2) == True
    assert is_power_of_two(4) == True
    assert is_power_of_two(8) == True
    assert is_power_of_two(16) == True
    assert is_power_of_two(1024) == True

def test_power_of_two_negative_cases():
    """Test numbers that are not powers of two."""
    assert is_power_of_two(0) == False
    assert is_power_of_two(3) == False
    assert is_power_of_two(5) == False
    assert is_power_of_two(7) == False
    assert is_power_of_two(15) == False

def test_power_of_two_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError):
        is_power_of_two(-1)
    with pytest.raises(ValueError):
        is_power_of_two(-8)
    
    # Test non-integer inputs
    with pytest.raises(TypeError):
        is_power_of_two(2.5)
    with pytest.raises(TypeError):
        is_power_of_two("2")
    with pytest.raises(TypeError):
        is_power_of_two([2])