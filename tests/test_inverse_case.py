import pytest
from src.inverse_case import convert_to_inverse_case

def test_basic_inverse_case():
    """Test basic string conversion to inverse case."""
    assert convert_to_inverse_case("Hello World") == "hELLO wORLD"
    assert convert_to_inverse_case("PyThOn") == "pYtHoN"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_inverse_case("") == ""

def test_special_characters():
    """Test conversion with special characters and numbers."""
    assert convert_to_inverse_case("Hello, World! 123") == "hELLO, wORLD! 123"

def test_only_uppercase():
    """Test conversion of an all uppercase string."""
    assert convert_to_inverse_case("HELLO") == "hello"

def test_only_lowercase():
    """Test conversion of an all lowercase string."""
    assert convert_to_inverse_case("hello") == "HELLO"

def test_mixed_case_with_spaces():
    """Test conversion of mixed case string with spaces."""
    assert convert_to_inverse_case("Hello World") == "hELLO wORLD"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(["Hello"])