import pytest
from src.string_transform import string_transform

def test_basic_transformation():
    """Test basic string transformation."""
    assert string_transform("Hello World") == 'dlrow*h'

def test_uppercase_input():
    """Test input with uppercase letters."""
    assert string_transform("PYTHON Programming") == 'gnimm*rorp*p'

def test_multiple_spaces():
    """Test input with multiple spaces."""
    assert string_transform("  Hello   World  ") == 'dlrow*h'

def test_string_with_numbers():
    """Test input with numbers and letters."""
    assert string_transform("Hello 123 World") == 'dlrow*321h'

def test_empty_string():
    """Test transformation of an empty string."""
    assert string_transform("") == ''

def test_string_with_only_spaces():
    """Test transformation of a string with only spaces."""
    assert string_transform("   ") == ''

def test_string_with_multiple_as():
    """Test replacement of multiple 'a' letters."""
    assert string_transform("Apple and Banana") == '*nn*b*p*lp*'