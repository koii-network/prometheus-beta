import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    """Test known perfect numbers."""
    # First few perfect numbers: 6, 28, 496, 8128
    assert is_perfect_number(6) == True
    assert is_perfect_number(28) == True
    assert is_perfect_number(496) == True
    assert is_perfect_number(8128) == True

def test_non_perfect_numbers():
    """Test some non-perfect numbers."""
    assert is_perfect_number(10) == False
    assert is_perfect_number(15) == False
    assert is_perfect_number(100) == False

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        is_perfect_number(0)
    
    with pytest.raises(ValueError):
        is_perfect_number(-5)
    
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError):
        is_perfect_number("not a number")