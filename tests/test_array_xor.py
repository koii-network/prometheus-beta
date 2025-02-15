import pytest
from src.array_xor import xor_array_elements

def test_xor_array_single_element():
    assert xor_array_elements([5]) == 5

def test_xor_array_multiple_elements():
    assert xor_array_elements([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0
    assert xor_array_elements([10, 20, 30]) == 20  # 10 ^ 20 ^ 30 = 20

def test_xor_array_large_numbers():
    assert xor_array_elements([100, 200, 300]) == 200

def test_xor_array_with_zero():
    assert xor_array_elements([0, 5, 10]) == 15

def test_xor_array_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array_elements([])

def test_xor_array_invalid_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array_elements("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array_elements(123)