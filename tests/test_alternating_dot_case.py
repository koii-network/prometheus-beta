import pytest
from src.alternating_dot_case import convert_to_alternating_dot_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert convert_to_alternating_dot_case("hello") == 'h.E.l.L.o'
    assert convert_to_alternating_dot_case("world") == 'w.O.r.L.d'

def test_multiple_words():
    """Test conversion of multiple words."""
    assert convert_to_alternating_dot_case("hello world") == 'h.E.l.L.o. .W.o.R.l.D'

def test_mixed_case_input():
    """Test input with mixed case."""
    assert convert_to_alternating_dot_case("PytHon") == 'p.Y.t.H.o.N'

def test_empty_string():
    """Test empty string input."""
    assert convert_to_alternating_dot_case("") == ""

def test_single_character():
    """Test single character input."""
    assert convert_to_alternating_dot_case("a") == 'a'
    assert convert_to_alternating_dot_case("Z") == 'z'

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(None)

def test_special_characters():
    """Test conversion with special characters."""
    assert convert_to_alternating_dot_case("hello-world!") == 'h.E.l.L.o.-.W.o.R.l.D.!'

def test_numbers_and_symbols():
    """Test conversion with numbers and symbols."""
    assert convert_to_alternating_dot_case("123 abc") == '1.2.3. .A.b.C'