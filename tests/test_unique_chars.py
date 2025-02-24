import pytest
from src.unique_chars import get_unique_characters

def test_basic_unique_characters():
    """Test basic functionality of extracting unique characters."""
    assert get_unique_characters('11223344') == '1234'
    assert get_unique_characters('1010101') == '10'
    assert get_unique_characters('9876543210') == '9876543210'
    assert get_unique_characters('0000') == '0'

def test_edge_cases():
    """Test edge cases for the function."""
    assert get_unique_characters('') == ''  # Empty string
    assert get_unique_characters('000111222') == '012'  # Repeated sequences

def test_error_cases():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        get_unique_characters(12345)  # Non-string input
    
    with pytest.raises(TypeError):
        get_unique_characters(None)  # None input
    
    with pytest.raises(ValueError):
        get_unique_characters('12a34')  # Non-numeric characters
    
    with pytest.raises(ValueError):
        get_unique_characters('-1234')  # Negative sign

def test_order_preservation():
    """Ensure the order of first appearance is preserved."""
    assert get_unique_characters('54321') == '54321'
    assert get_unique_characters('123454321') == '12345'

def test_comprehensive_scenarios():
    """Test comprehensive scenarios."""
    test_cases = [
        ('123456789', '123456789'),
        ('111111111', '1'),
        ('123123123', '123'),
        ('987654321', '987654321')
    ]
    
    for input_str, expected in test_cases:
        assert get_unique_characters(input_str) == expected