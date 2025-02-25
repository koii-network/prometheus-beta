import pytest
from src.list_product_pairs import calculate_product_pairs

def test_normal_list():
    """Test calculation of product pairs for a normal list."""
    result = calculate_product_pairs([1, 2, 3])
    assert set(result) == set([2, 3, 6])

def test_empty_list():
    """Test handling of an empty list."""
    assert calculate_product_pairs([]) is None

def test_single_element_list():
    """Test handling of a list with a single element."""
    assert calculate_product_pairs([5]) is None

def test_negative_numbers():
    """Test calculation with negative numbers."""
    result = calculate_product_pairs([-1, -2, 3])
    assert set(result) == set([2, -3, -6])

def test_zero_in_list():
    """Test calculation of product pairs with zero."""
    result = calculate_product_pairs([0, 1, 2])
    assert set(result) == set([0, 0, 2])

def test_invalid_input_type():
    """Test raising TypeError for non-integer inputs."""
    with pytest.raises(TypeError):
        calculate_product_pairs([1, 2, 'three'])

def test_invalid_input_none():
    """Test handling of None input."""
    with pytest.raises(TypeError):
        calculate_product_pairs(None)