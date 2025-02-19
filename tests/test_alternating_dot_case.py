import pytest
from src.alternating_dot_case import to_alternating_dot_case

def test_alternating_dot_case_normal_string():
    assert to_alternating_dot_case("hello") == 'h.e.l.l.o'

def test_alternating_dot_case_multiple_words():
    assert to_alternating_dot_case("hello world") == 'h.e.l.l.o. .w.o.r.l.d'

def test_alternating_dot_case_empty_string():
    assert to_alternating_dot_case("") == ''

def test_alternating_dot_case_single_character():
    assert to_alternating_dot_case("a") == 'a'

def test_alternating_dot_case_with_numbers_and_symbols():
    assert to_alternating_dot_case("hello123!") == 'h.e.l.l.o.1.2.3.!'