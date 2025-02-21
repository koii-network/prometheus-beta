import pytest
import random
from src.random_case_converter import convert_to_alternating_random_case

def test_convert_to_alternating_random_case_basic():
    # Set a fixed seed for reproducible random results
    random.seed(42)
    input_str = "hello world"
    result = convert_to_alternating_random_case(input_str)
    assert len(result) == len(input_str)
    assert result.lower() == input_str.lower()

def test_convert_to_alternating_random_case_empty_string():
    random.seed(42)
    result = convert_to_alternating_random_case("")
    assert result == ""

def test_convert_to_alternating_random_case_single_char():
    random.seed(42)
    result = convert_to_alternating_random_case("a")
    assert result in ["a", "A"]

def test_convert_to_alternating_random_case_error_handling():
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(None)

def test_convert_to_alternating_random_case_randomness():
    # This test checks that multiple calls can produce different results
    input_str = "hello"
    results = set()
    for _ in range(10):
        results.add(convert_to_alternating_random_case(input_str))
    
    # With randomness, we expect multiple different results
    assert len(results) > 1