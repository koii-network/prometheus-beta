import pytest
from src.string_utils import to_alternating_dot_case

def test_basic_alternating_dot_case():
    assert to_alternating_dot_case("hello world") == 'H.e.L.l.O. .W.o.R.l.D'

def test_single_word():
    assert to_alternating_dot_case("python") == 'P.y.T.h.O.n'

def test_empty_string():
    assert to_alternating_dot_case("") == ''

def test_single_character():
    assert to_alternating_dot_case("a") == 'A'

def test_error_handling():
    with pytest.raises(TypeError):
        to_alternating_dot_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_dot_case(None)

def test_mixed_case_input():
    assert to_alternating_dot_case("MiXeD cAsE") == 'M.i.X.e.D. .C.a.S.e'

def test_special_characters():
    assert to_alternating_dot_case("hello! world?") == 'H.e.L.l.O.!. .W.o.R.l.D.?'