import pytest
from src.coin_change import coin_change

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert coin_change([2], 3) == -1  # Cannot make 3 with only 2-cent coins
    assert coin_change([1], 0) == 0  # Zero amount

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    # Single coin denomination
    assert coin_change([1], 5) == 5
    assert coin_change([2], 4) == 2
    
    # Large amount
    assert coin_change([1, 5, 10, 25], 100) == 4  # 25 + 25 + 25 + 25
    
    # Tricky denominations
    assert coin_change([1, 3, 4], 6) == 2  # 3 + 3

def test_input_validation():
    """Test input validation and error handling"""
    # Empty coins list
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        coin_change([], 10)
    
    # Non-positive coin values
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        coin_change([0, 1, 2], 5)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        coin_change([-1, 2, 3], 10)

def test_impossible_amounts():
    """Test scenarios where the amount cannot be made"""
    assert coin_change([2], 3) == -1
    assert coin_change([5, 10], 7) == -1

def test_various_coin_sets():
    """Test with different coin denomination sets"""
    # US coin denominations
    assert coin_change([1, 5, 10, 25], 67) == 5  # Expected solution
    
    # International coin denominations
    assert coin_change([1, 2, 5, 10, 20, 50, 100], 123) == 4  # 100 + 20 + 2 + 1

def test_negative_amount():
    """Ensure negative amounts raise TypeError"""
    with pytest.raises(TypeError):
        coin_change([1, 2, 5], -10)

def test_non_integer_amount():
    """Ensure non-integer amounts raise TypeError"""
    with pytest.raises(TypeError):
        coin_change([1, 2, 5], 10.5)
    
    with pytest.raises(TypeError):
        coin_change([1, 2, 5], "10")