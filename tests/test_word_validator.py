import pytest
from src.word_validator import Queue, is_word_valid

def test_queue_basic_operations():
    """Test basic Queue operations."""
    q = Queue()
    assert q.is_empty() == True
    assert q.size() == 0
    
    q.enqueue(1)
    assert q.is_empty() == False
    assert q.size() == 1
    
    item = q.dequeue()
    assert item == 1
    assert q.is_empty() == True
    assert q.size() == 0

def test_queue_multiple_operations():
    """Test multiple enqueue and dequeue operations."""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() == True

def test_queue_empty_dequeue():
    """Test dequeuing from an empty queue raises an IndexError."""
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()

def test_is_word_valid_basic():
    """Test basic word validation."""
    # Default rules
    assert is_word_valid("hello", {}) == True
    
    # Minimum length
    assert is_word_valid("hi", {'min_length': 3}) == False
    assert is_word_valid("hello", {'min_length': 3}) == True
    
    # Maximum length
    assert is_word_valid("hello", {'max_length': 3}) == False
    assert is_word_valid("hi", {'max_length': 3}) == True

def test_is_word_valid_required_chars():
    """Test required characters validation."""
    # Required characters
    assert is_word_valid("hello", {'required_chars': ['h', 'e']}) == True
    assert is_word_valid("hello", {'required_chars': ['x']}) == False
    
    # Multiple required characters
    assert is_word_valid("hello", {'required_chars': ['h', 'l', 'o']}) == True
    assert is_word_valid("hello", {'required_chars': ['h', 'x']}) == False

def test_is_word_valid_forbidden_chars():
    """Test forbidden characters validation."""
    # Forbidden characters
    assert is_word_valid("hello", {'forbidden_chars': ['x']}) == True
    assert is_word_valid("hello", {'forbidden_chars': ['h']}) == False
    
    # Multiple forbidden characters
    assert is_word_valid("hello", {'forbidden_chars': ['x', 'y']}) == True
    assert is_word_valid("hello", {'forbidden_chars': ['h', 'l']}) == False

def test_is_word_valid_case_sensitivity():
    """Test case sensitivity validation."""
    # Case-sensitive (default)
    assert is_word_valid("Hello", {'required_chars': ['H']}) == True
    assert is_word_valid("Hello", {'required_chars': ['h']}) == False
    
    # Case-insensitive
    assert is_word_valid("Hello", {'required_chars': ['h'], 'case_sensitive': False}) == True
    assert is_word_valid("Hello", {'forbidden_chars': ['h'], 'case_sensitive': False}) == False

def test_is_word_valid_combined_rules():
    """Test combined validation rules."""
    # Combined rules
    rules = {
        'min_length': 3,
        'max_length': 5,
        'required_chars': ['h', 'l'],
        'forbidden_chars': ['x']
    }
    assert is_word_valid("hello", rules) == True
    assert is_word_valid("hi", rules) == False
    assert is_word_valid("hellox", rules) == False
    assert is_word_valid("hey", rules) == False

def test_is_word_valid_invalid_input():
    """Test handling of invalid input types."""
    assert is_word_valid(123, {}) == False
    assert is_word_valid("hello", 123) == False