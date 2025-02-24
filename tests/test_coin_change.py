import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2], 3) == -1  # Cannot make 3 with only 2-cent coins
    assert min_coins([1], 100) == 100  # 100 1-cent coins

def test_zero_amount():
    """Test zero amount edge case"""
    assert min_coins([1, 2, 5], 0) == 0

def test_single_coin():
    """Test scenarios with a single coin denomination"""
    assert min_coins([1], 5) == 5
    assert min_coins([2], 6) == 3

def test_multiple_coin_change():
    """Test various coin denomination combinations"""
    assert min_coins([1, 5, 10, 25], 67) == 5  # Example: 25 + 25 + 10 + 5 + 2

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError, match="Coins must be a list of integers"):
        min_coins("not a list", 10)
    
    with pytest.raises(TypeError, match="Amount must be an integer"):
        min_coins([1, 2, 5], "10")
    
    with pytest.raises(ValueError, match="Coin list cannot be empty"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([0, 1, 2], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([-1, 2, 5], 10)

def test_large_amount():
    """Test large amount scenarios"""
    assert min_coins([1, 5, 10, 25], 100) == 10  # 10 * 10-cent coins
    assert min_coins([1, 5, 10, 25], 99) == 9  # Example optimal combination