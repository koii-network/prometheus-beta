import pytest
from src.string_reversal import reverse_string

def test_reverse_string_methods():
    # Test string for various methods
    test_string = "hello"
    expected_reversed = "olleh"
    
    # Test manual method
    assert reverse_string(test_string, 'manual') == expected_reversed
    
    # Test reversed() method
    assert reverse_string(test_string, 'reversed') == expected_reversed
    
    # Test slice method
    assert reverse_string(test_string, 'slice') == expected_reversed
    
    # Test split method
    assert reverse_string(test_string, 'split') == expected_reversed
    
    # Test recursive method
    assert reverse_string(test_string, 'recursive') == expected_reversed

def test_reverse_string_all_methods():
    test_string = "hello"
    expected_reversed = "olleh"
    
    # Test all methods at once
    all_methods = reverse_string(test_string, 'all')
    assert isinstance(all_methods, dict)
    assert all(method_result == expected_reversed for method_result in all_methods.values())

def test_reverse_string_edge_cases():
    # Empty string
    assert reverse_string('', 'manual') == ''
    assert reverse_string('', 'reversed') == ''
    assert reverse_string('', 'slice') == ''
    assert reverse_string('', 'split') == ''
    assert reverse_string('', 'recursive') == ''
    
    # Single character
    assert reverse_string('a', 'manual') == 'a'
    assert reverse_string('a', 'reversed') == 'a'
    assert reverse_string('a', 'slice') == 'a'
    assert reverse_string('a', 'split') == 'a'
    assert reverse_string('a', 'recursive') == 'a'

def test_reverse_string_invalid_method():
    with pytest.raises(ValueError):
        reverse_string("hello", 'invalid_method')

def test_reverse_string_unicode():
    # Test with unicode characters
    unicode_string = "こんにちは"
    expected_reversed = "はちにんこ"
    assert reverse_string(unicode_string, 'manual') == expected_reversed
    assert reverse_string(unicode_string, 'reversed') == expected_reversed
    assert reverse_string(unicode_string, 'slice') == expected_reversed
    assert reverse_string(unicode_string, 'split') == expected_reversed
    assert reverse_string(unicode_string, 'recursive') == expected_reversed