import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    # Basic scenario with standard coins
    assert min_coins([1, 5, 10, 25], 11) == 2  # 10 + 1
    assert min_coins([1, 5, 10, 25], 30) == 2  # 25 + 5
    assert min_coins([1, 5, 10, 25], 37) == 4  # 25 + 10 + 1 + 1

def test_impossible_change():
    # Scenario where exact change is impossible
    assert min_coins([2, 5], 3) == -1

def test_single_coin_denomination():
    # Scenario with only one coin denomination
    assert min_coins([1], 5) == 5
    assert min_coins([2], 6) == 3

def test_zero_amount():
    # Amount is zero
    assert min_coins([1, 5, 10], 0) == 0

def test_large_amount():
    # Large amount to test performance
    assert min_coins([1, 5, 10, 25], 100) == 4  # 25 * 4

def test_input_validation():
    # Test error cases
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([0, 1, 2], 5)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([-1, 2, 3], 5)