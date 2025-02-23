import pytest
from src.z_algorithm import z_algorithm

def test_basic_pattern_matching():
    """Test basic pattern matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert z_algorithm(text, pattern) == [10]

def test_multiple_occurrences():
    """Test multiple occurrences of a pattern"""
    text = "AAAAAAAA"
    pattern = "AAA"
    assert z_algorithm(text, pattern) == [0, 1, 2, 3, 4, 5]

def test_no_occurrences():
    """Test when pattern is not in text"""
    text = "ABCDEF"
    pattern = "XYZ"
    assert z_algorithm(text, pattern) == []

def test_pattern_equals_text():
    """Test when pattern is exactly the same as text"""
    text = "HELLO"
    pattern = "HELLO"
    assert z_algorithm(text, pattern) == [0]

def test_empty_text_raises_error():
    """Test that empty text raises a ValueError"""
    with pytest.raises(ValueError):
        z_algorithm("", "PATTERN")

def test_empty_pattern_raises_error():
    """Test that empty pattern raises a ValueError"""
    with pytest.raises(ValueError):
        z_algorithm("TEXT", "")

def test_non_string_input_raises_error():
    """Test that non-string inputs raise a TypeError"""
    with pytest.raises(TypeError):
        z_algorithm(123, "PATTERN")
    
    with pytest.raises(TypeError):
        z_algorithm("TEXT", 456)

def test_case_sensitivity():
    """Test case sensitivity of the algorithm"""
    text = "AbCaBcAbCaBC"
    pattern1 = "AbC"
    pattern2 = "abc"
    assert z_algorithm(text, pattern1) == [0, 6]
    assert z_algorithm(text, pattern2) == []

def test_single_character_pattern():
    """Test pattern matching with a single character"""
    text = "AAAAA"
    pattern = "A"
    assert z_algorithm(text, pattern) == [0, 1, 2, 3, 4]