import pytest
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test that the function works with a basic string."""
    result = convert_to_random_case("hello")
    assert isinstance(result, str)
    assert len(result) == 5

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_whitespace():
    """Test conversion of a string with whitespace."""
    result = convert_to_random_case("hello world")
    assert isinstance(result, str)
    assert len(result) == 11

def test_convert_to_random_case_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_distribution():
    """
    Test that over multiple runs, each character has a chance 
    of being upper or lower case.
    """
    test_string = "abcdefg"
    
    # Collect results from multiple runs
    results = [convert_to_random_case(test_string) for _ in range(100)]
    
    # Check that at least some variations exist
    upper_counts = [sum(1 for char in result if char.isupper()) for result in results]
    
    # Ensure there's variation in uppercase count
    assert min(upper_counts) < len(test_string)
    assert max(upper_counts) > 0