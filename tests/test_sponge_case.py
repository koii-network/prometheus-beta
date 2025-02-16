import pytest
from src.sponge_case import to_sponge_case

def test_to_sponge_case_type():
    """Test that the function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        to_sponge_case(123)
    with pytest.raises(TypeError):
        to_sponge_case(None)

def test_to_sponge_case_empty_string():
    """Test conversion of an empty string."""
    result = to_sponge_case("")
    assert result == ""

def test_to_sponge_case_single_character():
    """Test conversion of a single character."""
    result = to_sponge_case("a")
    assert result in ["a", "A"]

def test_to_sponge_case_multiple_characters():
    """Test that the function returns a string of the same length."""
    input_text = "hello world"
    result = to_sponge_case(input_text)
    
    # Check that result is same length as input
    assert len(result) == len(input_text)
    
    # Check that result contains only characters from input
    assert set(result.lower()) == set(input_text.lower())

def test_to_sponge_case_randomness():
    """Test that multiple calls produce different results."""
    input_text = "hello world"
    results = set()
    
    # Generate multiple results
    for _ in range(10):
        results.add(to_sponge_case(input_text))
    
    # With randomness, we expect at least some variation
    assert len(results) > 1