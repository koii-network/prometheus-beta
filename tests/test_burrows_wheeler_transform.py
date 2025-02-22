import pytest
from src.burrows_wheeler_transform import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform_basic():
    # Test a simple string
    text = "banana"
    bwt_result, original_index = burrows_wheeler_transform(text)
    assert isinstance(bwt_result, str)
    assert isinstance(original_index, int)

def test_burrows_wheeler_transform_round_trip():
    # Test that we can recover the original text
    text = "banana"
    bwt_result, original_index = burrows_wheeler_transform(text)
    recovered_text = inverse_burrows_wheeler_transform(bwt_result, original_index)
    assert recovered_text == text

def test_empty_string():
    # Test empty string input
    text = ""
    bwt_result, original_index = burrows_wheeler_transform(text)
    assert bwt_result == ""
    assert original_index == 0

def test_single_character():
    # Test single character input
    text = "a"
    bwt_result, original_index = burrows_wheeler_transform(text)
    recovered_text = inverse_burrows_wheeler_transform(bwt_result, original_index)
    assert recovered_text == text

def test_repeated_characters():
    # Test string with repeated characters
    text = "aabbaabb"
    bwt_result, original_index = burrows_wheeler_transform(text)
    recovered_text = inverse_burrows_wheeler_transform(bwt_result, original_index)
    assert recovered_text == text

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        burrows_wheeler_transform(123)
    
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform(123, 0)
    
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform("text", "index")

def test_complex_string():
    # Test a more complex string
    text = "hello world!"
    bwt_result, original_index = burrows_wheeler_transform(text)
    recovered_text = inverse_burrows_wheeler_transform(bwt_result, original_index)
    assert recovered_text == text