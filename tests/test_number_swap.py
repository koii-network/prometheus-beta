import pytest
from src.number_swap import swap_numbers

def test_swap_positive_integers():
    """Test swapping positive integers."""
    a, b = 5, 10
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b
    assert swapped_b == a

def test_swap_negative_integers():
    """Test swapping negative integers."""
    a, b = -5, -10
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b
    assert swapped_b == a

def test_swap_mixed_signs():
    """Test swapping numbers with mixed signs."""
    a, b = 7, -3
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b
    assert swapped_b == a

def test_swap_zero():
    """Test swapping with zero."""
    a, b = 0, 15
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b
    assert swapped_b == a

def test_swap_floating_point():
    """Test swapping floating point numbers."""
    a, b = 3.14, 2.71
    swapped_a, swapped_b = swap_numbers(a, b)
    assert swapped_a == b
    assert swapped_b == a

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        swap_numbers("5", 10)
    
    with pytest.raises(TypeError):
        swap_numbers(5, "10")
    
    with pytest.raises(TypeError):
        swap_numbers([], {})