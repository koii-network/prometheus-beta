import pytest
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    # Test known perfect squares
    assert is_perfect_square(0) == True
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True
    assert is_perfect_square(100) == True

def test_non_perfect_squares():
    # Test non-perfect squares
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(7) == False
    assert is_perfect_square(15) == False
    assert is_perfect_square(99) == False

def test_edge_cases():
    # Test edge cases
    assert is_perfect_square(0) == True
    assert is_perfect_square(1) == True

def test_large_perfect_square():
    # Test a large perfect square
    assert is_perfect_square(10000) == True  # 100^2
    assert is_perfect_square(1000000) == True  # 1000^2

def test_error_handling():
    # Test error cases
    with pytest.raises(ValueError):
        is_perfect_square(-1)
    
    with pytest.raises(TypeError):
        is_perfect_square(3.14)
    
    with pytest.raises(TypeError):
        is_perfect_square("16")