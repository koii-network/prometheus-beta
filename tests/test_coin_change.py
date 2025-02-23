import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios."""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2], 3) == -1  # Cannot make exact change
    assert min_coins([1], 100) == 100  # All 1-cent coins

def test_zero_amount():
    """Test when amount is zero."""
    assert min_coins([1, 2, 5], 0) == 0

def test_single_coin():
    """Test scenarios with a single coin denomination."""
    assert min_coins([1], 5) == 5
    assert min_coins([5], 10) == 2

def test_multiple_solutions():
    """Test scenarios with multiple possible coin combinations."""
    assert min_coins([1, 3, 4], 6) == 2  # Can be 3+3 or 4+2

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([1, -2, 5], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([0], 10)

def test_edge_cases():
    """Test various edge cases."""
    assert min_coins([2], 4) == 2  # Even amount
    assert min_coins([2], 7) == -1  # Odd amount with even coin
    assert min_coins([186, 419, 83, 408], 6249) > 0  # Large amount