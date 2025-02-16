import pytest
from src.alternating_dot_case import to_alternating_dot_case

def test_basic_alternating_dot_case():
    assert to_alternating_dot_case("hello") == "h.E.l.L.o"
    assert to_alternating_dot_case("world") == "w.O.r.L.d"

def test_mixed_case_input():
    assert to_alternating_dot_case("HelloWorld") == "h.E.l.L.o.W.o.R.l.D"

def test_with_numbers_and_special_chars():
    assert to_alternating_dot_case("hello123world!") == "h.E.l.L.o1.2.3.W.o.R.l.D!"

def test_empty_string():
    assert to_alternating_dot_case("") == ""

def test_non_string_input():
    with pytest.raises(TypeError):
        to_alternating_dot_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_dot_case(None)