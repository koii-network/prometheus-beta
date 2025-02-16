import pytest
from src.alternating_pascal_case import to_alternating_pascal_case

def test_alternating_pascal_case_basic():
    assert to_alternating_pascal_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_pascal_case("python programming") == "PyThOn PrOgRaMmInG"

def test_alternating_pascal_case_single_word():
    assert to_alternating_pascal_case("hello") == "HeLlO"
    assert to_alternating_pascal_case("WORLD") == "WoRlD"

def test_alternating_pascal_case_multiple_words():
    assert to_alternating_pascal_case("this is a test") == "ThIs Is A TeSt"

def test_alternating_pascal_case_empty_string():
    assert to_alternating_pascal_case("") == ""

def test_alternating_pascal_case_mixed_case():
    assert to_alternating_pascal_case("MiXeD CaSe") == "MiXeD CaSe"

def test_alternating_pascal_case_with_numbers():
    assert to_alternating_pascal_case("hello 123 world") == "HeLlO 123 WoRlD"