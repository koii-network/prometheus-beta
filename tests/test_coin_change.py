import pytest
from src.coin_change import coin_change

def test_standard_coin_change():
    # Basic scenario with multiple coin options
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert coin_change([2], 3) == -1  # Cannot make exact change
    assert coin_change([1], 0) == 0  # Zero amount
    assert coin_change([1], 1) == 1  # Single coin exactly matches amount
    assert coin_change([1, 5, 10, 25], 30) == 2  # 25 + 5

def test_edge_cases():
    # Test edge cases
    assert coin_change([], 5) == -1  # No coins available
    assert coin_change([2], 1) == -1  # Cannot make exact change
    assert coin_change([1], 100) == 100  # Only 1-cent coins

def test_large_amount():
    # Test with larger amounts
    assert coin_change([1, 5, 10, 25], 100) == 4  # Reasonable result
    
def test_invalid_inputs():
    # Test with negative values
    with pytest.raises(ValueError):
        coin_change([1, 2, 3], -5)
    with pytest.raises(TypeError):
        coin_change(None, 10)