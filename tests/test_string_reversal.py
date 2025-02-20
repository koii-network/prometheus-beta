import pytest
from src.string_reversal import reverse_string

@pytest.mark.parametrize("method", ['manual', 'reversed', 'slicing', 'split', 'recursive'])
def test_string_reversal_standard(method):
    """Test standard string reversal for different methods"""
    assert reverse_string("hello", method) == "olleh"
    assert reverse_string("python", method) == "nohtyp"
    assert reverse_string("", method) == ""

def test_string_reversal_special_characters():
    """Test reversing strings with special characters"""
    for method in ['manual', 'reversed', 'slicing', 'split', 'recursive']:
        assert reverse_string("a!b@c#", method) == "#c@b!a"
        assert reverse_string("123!@#", method) == "#@!321"

def test_string_reversal_unicode():
    """Test reversing strings with Unicode characters"""
    for method in ['manual', 'reversed', 'slicing', 'split', 'recursive']:
        assert reverse_string("héllo", method) == "ollèh"
        assert reverse_string("こんにちは", method) == "はちにんこ"

def test_string_reversal_invalid_method():
    """Test invalid method raises ValueError"""
    with pytest.raises(ValueError, match="Invalid reversal method"):
        reverse_string("test", "invalid_method")

def test_string_reversal_invalid_input():
    """Test non-string input raises TypeError"""
    for method in ['manual', 'reversed', 'slicing', 'split', 'recursive']:
        with pytest.raises(TypeError, match="Input must be a string"):
            reverse_string(123, method)
        with pytest.raises(TypeError, match="Input must be a string"):
            reverse_string(None, method)