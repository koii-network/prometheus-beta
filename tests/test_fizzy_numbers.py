import pytest
from src.fizzy_numbers import generate_fizzy_numbers

def test_basic_fizzy_numbers():
    """Test basic fizzy number generation"""
    assert set(generate_fizzy_numbers(10)) == set([3, 6, 7, 9, 10])

def test_larger_range():
    """Test fizzy number generation for a larger range"""
    result = generate_fizzy_numbers(20)
    expected = [3, 6, 7, 9, 10, 12, 14, 15, 18, 20]
    assert set(result) == set(expected)

def test_single_number():
    """Test fizzy number generation for single number"""
    assert set(generate_fizzy_numbers(3)) == {3}
    assert set(generate_fizzy_numbers(7)) == {7}

def test_no_fizzy_numbers():
    """Test case with no fizzy numbers"""
    assert generate_fizzy_numbers(2) == []

def test_invalid_input():
    """Test invalid input handling"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fizzy_numbers(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fizzy_numbers(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fizzy_numbers(3.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fizzy_numbers("10")