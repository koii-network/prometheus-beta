import pytest
import random
from src.sponge_case import to_sponge_case

def test_sponge_case_basic():
    """Test basic sponge case conversion."""
    text = "hello world"
    result = to_sponge_case(text)
    assert len(result) == len(text)
    assert result.lower() == text.lower()

def test_sponge_case_empty_string():
    """Test conversion of an empty string."""
    assert to_sponge_case("") == ""

def test_sponge_case_reproducibility():
    """Test that given the same input, the function produces the same result."""
    text = "test string"
    random.seed(len(text))
    result1 = to_sponge_case(text)
    
    random.seed(len(text))
    result2 = to_sponge_case(text)
    
    assert result1 == result2

def test_sponge_case_type_error():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        to_sponge_case(123)
    with pytest.raises(TypeError):
        to_sponge_case(None)

def test_sponge_case_special_characters():
    """Test sponge case conversion with special characters."""
    text = "hello, world! 123"
    result = to_sponge_case(text)
    assert len(result) == len(text)
    assert result.lower() == text.lower()