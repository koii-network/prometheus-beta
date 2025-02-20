import pytest
from src.factor_counter import count_factors

def test_count_factors_basic():
    """Test basic scenarios of factor counting."""
    assert count_factors(1) == 1
    assert count_factors(4) == 3  # 1, 2, 4
    assert count_factors(12) == 6  # 1, 2, 3, 4, 6, 12
    assert count_factors(16) == 5  # 1, 2, 4, 8, 16
    assert count_factors(25) == 3  # 1, 5, 25

def test_count_factors_prime():
    """Test prime numbers have exactly 2 factors."""
    assert count_factors(2) == 2
    assert count_factors(3) == 2
    assert count_factors(7) == 2
    assert count_factors(11) == 2

def test_count_factors_edge_cases():
    """Test edge cases and boundary conditions."""
    assert count_factors(100) == 9  # 1, 2, 4, 5, 10, 20, 25, 50, 100

def test_count_factors_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        count_factors(0)
    with pytest.raises(ValueError):
        count_factors(-5)
    with pytest.raises(ValueError):
        count_factors(3.14)
    with pytest.raises(ValueError):
        count_factors("not a number")