import pytest
from src.coin_change import min_coins

def test_standard_coin_change():
    """Test typical coin change scenarios"""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2], 3) == -1  # Cannot make 3 with only 2-cent coins
    assert min_coins([1, 5, 10, 25], 30) == 2  # 25 + 5

def test_edge_cases():
    """Test edge case scenarios"""
    assert min_coins([1], 0) == 0  # Zero amount
    assert min_coins([1], 1) == 1  # Single coin exact match
    assert min_coins([2], 1) == -1  # Impossible amount

def test_various_coin_sets():
    """Test different coin denomination sets"""
    assert min_coins([1, 3, 4], 6) == 2  # 3 + 3 or 4 + 2
    assert min_coins([2, 3, 5], 8) == 2  # 3 + 5 or 2 + 2 + 2 + 2

def test_input_validation():
    """Test input validation"""
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="Coin denominations must be positive"):
        min_coins([1, -2, 5], 10)
    
    with pytest.raises(ValueError, match="Coin denominations must be positive"):
        min_coins([0], 10)