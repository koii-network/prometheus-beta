import pytest
from src.alternating_dot_case import convert_to_alternating_dot_case

def test_basic_conversion():
    assert convert_to_alternating_dot_case("hello") == 'h.e.l.l.o'
    assert convert_to_alternating_dot_case("Python") == 'P.y.t.h.o.n'

def test_multiple_words():
    assert convert_to_alternating_dot_case("hello world") == 'h.e.l.l.o. .w.o.r.l.d'

def test_empty_string():
    assert convert_to_alternating_dot_case("") == ''

def test_single_character():
    assert convert_to_alternating_dot_case("a") == 'a'

def test_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(None)