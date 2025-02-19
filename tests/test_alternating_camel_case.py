import pytest
from src.alternating_camel_case import alternating_camel_case

def test_alternating_camel_case():
    assert alternating_camel_case("hello world") == "hElLoWoRlD"
    assert alternating_camel_case("python programming") == "pYtHoNpRoGrAmMiNg"
    assert alternating_camel_case("") == ""
    assert alternating_camel_case("a") == "a"
    assert alternating_camel_case("ab") == "aB"
    assert alternating_camel_case("abc def") == "aBcDeF"
    assert alternating_camel_case("UPPERCASE TEST") == "uPpErCaSeTeSt"