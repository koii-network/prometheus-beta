import pytest
from src.sponge_case import to_sponge_case

def test_sponge_case_basic():
    """Test basic string conversion to sponge case."""
    result = to_sponge_case("hello")
    assert len(result) == 5
    assert result.lower() == "hello"

def test_sponge_case_empty_string():
    """Test conversion of an empty string."""
    result = to_sponge_case("")
    assert result == ""

def test_sponge_case_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_sponge_case(123)
    
    with pytest.raises(TypeError):
        to_sponge_case(None)

def test_sponge_case_mixed_input():
    """Test conversion of a mixed input string."""
    result = to_sponge_case("Hello World")
    assert len(result) == 11
    assert result.lower() == "hello world"

def test_sponge_case_randomness():
    """Test that multiple calls produce different results."""
    input_str = "test"
    results = {to_sponge_case(input_str) for _ in range(10)}
    assert len(results) > 1  # Probabilistic test of randomness