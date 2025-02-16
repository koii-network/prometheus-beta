import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    assert to_sponge_case("hello world") == "hElLo WoRlD"
    assert to_sponge_case("python") == "pYtHoN"

def test_empty_string():
    assert to_sponge_case("") == ""

def test_single_character():
    assert to_sponge_case("a") == "a"
    assert to_sponge_case("B") == "b"

def test_mixed_case_input():
    assert to_sponge_case("PrOgRaMmInG") == "pRoGrAmMiNg"

def test_special_characters():
    assert to_sponge_case("hello123world!") == "hElLo123WoRlD!"

def test_whitespace():
    assert to_sponge_case("   spacey   ") == "   sPaCeY   "