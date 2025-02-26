import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert min_coins(11, [1, 2, 5]) == 3  # 5 + 5 + 1
    assert min_coins(10, [2, 5, 10]) == 1  # 10
    assert min_coins(7, [1, 3, 4]) == 2  # 3 + 4

def test_impossible_change():
    """Test scenarios where change cannot be made"""
    assert min_coins(3, [2]) == -1  # Cannot make 3 with only 2-cent coins
    assert min_coins(7, [5]) == -1  # Cannot make 7 with only 5-cent coins

def test_zero_amount():
    """Test zero amount scenario"""
    assert min_coins(0, [1, 2, 5]) == 0  # 0 coins needed for 0 amount

def test_single_coin():
    """Test scenarios with single coin denomination"""
    assert min_coins(5, [5]) == 1  # 5
    assert min_coins(10, [2]) == 5  # 2 + 2 + 2 + 2 + 2

def test_edge_cases():
    """Test various edge cases"""
    # Large amount
    assert min_coins(100, [1, 5, 10, 25]) == 4  # 25 + 25 + 25 + 25
    
    # Single coin that exactly matches amount
    assert min_coins(10, [10]) == 1

def test_input_validation():
    """Test input validation"""
    with pytest.raises(ValueError, match="Amount must be non-negative"):
        min_coins(-1, [1, 2, 5])
    
    with pytest.raises(ValueError, match="Coins list cannot be empty"):
        min_coins(10, [])