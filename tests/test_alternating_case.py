import pytest
from src.alternating_case import to_alternating_lower_case

def test_alternating_lower_case():
    # Test basic functionality
    assert to_alternating_lower_case("hello") == "hElLo"
    assert to_alternating_lower_case("world") == "wOrLd"
    
    # Test empty string
    assert to_alternating_lower_case("") == ""
    
    # Test with existing mixed case
    assert to_alternating_lower_case("HeLLo") == "hElLo"
    
    # Test with numbers and special characters
    assert to_alternating_lower_case("hello123") == "hElLo123"
    
    # Test error handling
    with pytest.raises(TypeError):
        to_alternating_lower_case(123)
    with pytest.raises(TypeError):
        to_alternating_lower_case(None)