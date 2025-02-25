import pytest
from src.string_transform import string_transform

def test_basic_transformation():
    """Test basic string transformation."""
    assert string_transform("Hello World") == "dlrow*h*"

def test_multiple_spaces():
    """Test string with multiple spaces."""
    assert string_transform("  Python  Programming  ") == "gnimm*rgor*p"

def test_mixed_case():
    """Test string with mixed case letters."""
    assert string_transform("Awesome Project") == "tcejorp*emosw*"

def test_no_changes_needed():
    """Test string without spaces or 'a'."""
    assert string_transform("Python") == "nohtyp"

def test_empty_string():
    """Test empty string input."""
    assert string_transform("") == ""

def test_string_with_only_spaces():
    """Test string with only spaces."""
    assert string_transform("   ") == ""

def test_only_lowercase_a():
    """Test string with only lowercase 'a'."""
    assert string_transform("aaa") == "***"

def test_mixed_a_occurrences():
    """Test string with mixed 'a' cases."""
    assert string_transform("AAaaa") == "***"