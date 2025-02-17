import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_mixed_string():
    assert extract_numbers("I have 42 apples and 3.14 oranges") == [42, 3.14]

def test_extract_numbers_negative_decimals():
    assert extract_numbers("Temperature: -5.6 degrees") == [-5.6]

def test_extract_numbers_multiple_formats():
    assert extract_numbers("Version 2.0 update -1 patch") == [2.0, -1]

def test_extract_numbers_no_numbers():
    assert extract_numbers("No numbers here") == []

def test_extract_numbers_edge_cases():
    assert extract_numbers("0 and 00 and -00.5") == [0, 0, -0.5]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        extract_numbers(123)
        
def test_extract_numbers_complex_string():
    assert extract_numbers("Price: $45.99, Quantity: -3") == [45.99, -3]