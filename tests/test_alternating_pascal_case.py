import pytest
from src.alternating_pascal_case import to_alternating_pascal_case

def test_basic_conversion():
    assert to_alternating_pascal_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_pascal_case("python programming") == "PyThOn PrOgRaMmInG"

def test_single_word():
    assert to_alternating_pascal_case("python") == "PyThOn"

def test_multiple_words():
    assert to_alternating_pascal_case("hello beautiful world") == "HeLlO BeAuTiFuL WoRlD"

def test_empty_string():
    assert to_alternating_pascal_case("") == ""

def test_mixed_case_input():
    assert to_alternating_pascal_case("MiXeD CaSe InPuT") == "MiXeD CaSe InPuT"

def test_special_characters():
    assert to_alternating_pascal_case("hello-world") == "HeLlO-WoRlD"

def test_error_handling():
    with pytest.raises(TypeError):
        to_alternating_pascal_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_pascal_case(None)