"""
Test suite for string reversal function.

This module contains comprehensive tests for the string_reversal module,
covering various reversal methods, edge cases, and error conditions.
"""

import pytest
from src.string_reversal import reverse_string

def test_manual_reverse():
    """Test manual reversal method."""
    assert reverse_string("hello", method='manual') == "olleh"
    assert reverse_string("", method='manual') == ""
    assert reverse_string("a", method='manual') == "a"

def test_reversed_method():
    """Test reversed() method."""
    assert reverse_string("world", method='reversed') == "dlrow"
    assert reverse_string("", method='reversed') == ""
    assert reverse_string("python", method='reversed') == "nohtyp"

def test_slicing_method():
    """Test slicing method."""
    assert reverse_string("coding", method='slicing') == "gnidoc"
    assert reverse_string("", method='slicing') == ""
    assert reverse_string("test", method='slicing') == "tset"

def test_splitjoin_method():
    """Test split/reverse/join method."""
    assert reverse_string("algorithm", method='splitjoin') == "mhtirogla"
    assert reverse_string("", method='splitjoin') == ""
    assert reverse_string("data", method='splitjoin') == "atad"

def test_recursive_method():
    """Test recursive reversal method."""
    assert reverse_string("recursion", method='recursive') == "noisrucer"
    assert reverse_string("", method='recursive') == ""
    assert reverse_string("a", method='recursive') == "a"

def test_all_methods():
    """Test all methods simultaneously."""
    result = reverse_string("test")
    assert isinstance(result, dict)
    assert len(result) == 5
    for method, reversed_str in result.items():
        assert reversed_str == "tset"

def test_invalid_method():
    """Test invalid method raises ValueError."""
    with pytest.raises(ValueError, match="Invalid method"):
        reverse_string("test", method='invalid')

def test_non_string_input():
    """Test non-string input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["list"])