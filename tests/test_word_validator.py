import pytest
from src.word_validator import Queue, is_word_valid

def test_queue_basic_operations():
    """Test basic Queue operations."""
    queue = Queue()
    
    # Test initial state
    assert queue.is_empty() == True
    assert queue.size() == 0
    
    # Test enqueue
    queue.enqueue(1)
    assert queue.size() == 1
    assert queue.is_empty() == False
    
    # Test dequeue
    item = queue.dequeue()
    assert item == 1
    assert queue.is_empty() == True

def test_queue_error_handling():
    """Test Queue error handling."""
    queue = Queue()
    
    # Test dequeue from empty queue
    with pytest.raises(IndexError):
        queue.dequeue()

def test_is_word_valid_length_rules():
    """Test word validation length rules."""
    # Minimum length rule
    assert is_word_valid("hello", {'min_length': 5}) == True
    assert is_word_valid("hi", {'min_length': 5}) == False
    
    # Maximum length rule
    assert is_word_valid("hello", {'max_length': 5}) == True
    assert is_word_valid("helloworld", {'max_length': 5}) == False

def test_is_word_valid_character_rules():
    """Test word validation character rules."""
    # Required characters
    assert is_word_valid("hello", {'required_chars': ['h', 'e']}) == True
    assert is_word_valid("world", {'required_chars': ['h', 'e']}) == False
    
    # Forbidden characters
    assert is_word_valid("hello", {'forbidden_chars': ['x', 'y']}) == True
    assert is_word_valid("xy", {'forbidden_chars': ['x', 'y']}) == False

def test_is_word_valid_case_rules():
    """Test word validation case-sensitive rules."""
    # Uppercase rule
    assert is_word_valid("HELLO", {'case_sensitive': 'upper'}) == True
    assert is_word_valid("hello", {'case_sensitive': 'upper'}) == False
    
    # Lowercase rule
    assert is_word_valid("hello", {'case_sensitive': 'lower'}) == True
    assert is_word_valid("HELLO", {'case_sensitive': 'lower'}) == False

def test_is_word_valid_pattern_rule():
    """Test word validation pattern rule."""
    # Pattern matching
    assert is_word_valid("abc123", {'pattern': r'^[a-z]+\d+$'}) == True
    assert is_word_valid("123abc", {'pattern': r'^[a-z]+\d+$'}) == False

def test_is_word_valid_multiple_rules():
    """Test word validation with multiple rules."""
    rules = {
        'min_length': 5,
        'max_length': 10,
        'required_chars': ['a'],
        'forbidden_chars': ['x'],
        'case_sensitive': 'lower',
        'pattern': r'^[a-z]+$'
    }
    
    assert is_word_valid("abcdef", rules) == True
    assert is_word_valid("ABCDEF", rules) == False
    assert is_word_valid("abc123", rules) == False
    assert is_word_valid("abcx", rules) == False