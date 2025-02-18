import pytest
from src.string_utils import string_transform

def test_string_transform_basic():
    """Test basic string transformation"""
    assert string_transform("Hello World") == "dlrow*olleh"

def test_string_transform_mixed_case():
    """Test transformation with mixed case characters"""
    assert string_transform("Python Programming") == "gnimm*rgoprython"

def test_string_transform_with_numbers():
    """Test transformation with numbers"""
    assert string_transform("Test 123 ABC") == "cb*321tset"

def test_string_transform_empty_string():
    """Test transformation with empty string"""
    assert string_transform("") == ""

def test_string_transform_no_spaces():
    """Test transformation with no spaces"""
    assert string_transform("HelloWorld") == "dlrowolleh"

def test_string_transform_only_spaces():
    """Test transformation with only spaces"""
    assert string_transform("   ") == ""

def test_string_transform_with_special_chars():
    """Test transformation with special characters"""
    assert string_transform("Hello! World@") == "@dlrow!olleh"