import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2], 3) == -1  # Cannot make 3 with only 2-cent coins
    assert min_coins([1], 100) == 100  # All 1-cent coins

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    assert min_coins([1, 2, 5], 0) == 0  # Zero amount
    assert min_coins([2, 3, 5], 1) == -1  # Impossible amount
    
def test_input_validation():
    """Test input validation"""
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive integers"):
        min_coins([0, 1, 2], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive integers"):
        min_coins([-1, 2, 3], 10)

def test_various_coin_sets():
    """Test different coin denomination sets"""
    assert min_coins([1, 5, 10, 25], 30) == 2  # 25 + 5
    assert min_coins([2, 3, 5], 9) == 3  # 5 + 3 + 1
    assert min_coins([186, 419, 83, 408], 6249) == 20  # Complex large number scenario

def test_large_amount():
    """Test large amount scenarios"""
    # Ensure algorithm can handle relatively large amounts efficiently
    assert min_coins([1, 5, 10, 25], 100) == 4  # 25 + 25 + 25 + 25
    assert min_coins([1, 5, 10, 25], 1000) > 0  # Should find a solution