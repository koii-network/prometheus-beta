import pytest
from ..src.random_case_converter import convert_to_alternating_random_case

def test_convert_to_alternating_random_case_basic():
    """Test basic string conversion"""
    result = convert_to_alternating_random_case("hello")
    assert len(result) == 5
    assert result.lower() == "hello"

def test_convert_to_alternating_random_case_empty_string():
    """Test empty string input"""
    result = convert_to_alternating_random_case("")
    assert result == ""

def test_convert_to_alternating_random_case_non_string():
    """Test non-string input raises TypeError"""
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(123)

def test_convert_to_alternating_random_case_special_chars():
    """Test string with special characters"""
    result = convert_to_alternating_random_case("Hello, World! 123")
    assert len(result) == 17
    assert result.replace(' ', '').replace(',', '').replace('!', '').lower() == "hello,world!123"

def test_convert_to_alternating_random_case_randomness():
    """Test that multiple calls can produce different results"""
    input_str = "hello"
    results = set()
    for _ in range(100):
        results.add(convert_to_alternating_random_case(input_str))
    
    # With 100 attempts, we should get more than one unique result
    assert len(results) > 1