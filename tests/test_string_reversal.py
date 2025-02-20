import pytest
from src.string_reversal import recursive_string_reverse

def test_recursive_string_reverse_simple():
    assert recursive_string_reverse("hello") == "olleh"
    assert recursive_string_reverse("world") == "dlrow"

def test_recursive_string_reverse_mixed_case():
    assert recursive_string_reverse("Hello World") == "dlroW olleH"
    assert recursive_string_reverse("OpenAI") == "IAnepO"

def test_recursive_string_reverse_empty_string():
    assert recursive_string_reverse("") == ""

def test_recursive_string_reverse_single_char():
    assert recursive_string_reverse("a") == "a"
    assert recursive_string_reverse("Z") == "Z"

def test_recursive_string_reverse_with_spaces():
    assert recursive_string_reverse("  hello  ") == "  olleh  "

def test_recursive_string_reverse_invalid_input():
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_string_reverse("hello123")
    
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_string_reverse("hello!")
    
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_string_reverse("12345")