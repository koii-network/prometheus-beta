import pytest
from src.factor_counter import count_factors

def test_count_factors_basic():
    """Test basic factor counting."""
    assert count_factors(1) == 1
    assert count_factors(6) == 4  # 1, 2, 3, 6
    assert count_factors(10) == 4  # 1, 2, 5, 10
    assert count_factors(16) == 5  # 1, 2, 4, 8, 16

def test_count_factors_prime():
    """Test factor counting for prime numbers."""
    assert count_factors(2) == 2  # 1, 2
    assert count_factors(17) == 2  # 1, 17
    assert count_factors(29) == 2  # 1, 29

def test_count_factors_perfect_square():
    """Test factor counting for perfect squares."""
    assert count_factors(25) == 3  # 1, 5, 25

def test_count_factors_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(0)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(-5)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(3.14)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors("10")