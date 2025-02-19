import pytest
from src.alternating_header_case import alternating_header_case

def test_alternating_header_case():
    # Test basic conversion
    assert alternating_header_case("hello world") == "HeLlO WoRlD"
    
    # Test single characters
    assert alternating_header_case("a") == "A"
    assert alternating_header_case("b") == "B"
    
    # Test empty string
    assert alternating_header_case("") == ""
    
    # Test strings with spaces
    assert alternating_header_case("python programming") == "PyThOn PrOgRaMmInG"
    
    # Test strings with mixed case
    assert alternating_header_case("PYTHON") == "PyThOn"
    assert alternating_header_case("python") == "PyThOn"
    
    # Test strings with special characters
    assert alternating_header_case("hello, world!") == "HeLlO, WoRlD!"
    
    # Verify that the function doesn't modify the original string
    original = "test string"
    result = alternating_header_case(original)
    assert result == "TeSt StRiNg"
    assert original == "test string"