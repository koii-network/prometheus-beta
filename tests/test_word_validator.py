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

def test_queue_dequeue_error():
    """Test dequeuing from an empty queue raises an error."""
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()

def test_queue_multiple_operations():
    """Test multiple enqueue and dequeue operations."""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.size() == 1

def test_is_word_valid_basic():
    """Test basic word validation scenarios."""
    # Minimum length rule
    assert is_word_valid("hello", ["min_length:4"]) == True
    assert is_word_valid("hi", ["min_length:4"]) == False
    
    # Maximum length rule
    assert is_word_valid("hello", ["max_length:5"]) == True
    assert is_word_valid("hello world", ["max_length:5"]) == False
    
    # Contains letter rule
    assert is_word_valid("hello", ["contains:h"]) == True
    assert is_word_valid("world", ["contains:h"]) == False
    
    # Starts with rule
    assert is_word_valid("hello", ["starts_with:he"]) == True
    assert is_word_valid("world", ["starts_with:he"]) == False
    
    # Ends with rule
    assert is_word_valid("hello", ["ends_with:lo"]) == True
    assert is_word_valid("world", ["ends_with:lo"]) == False

def test_is_word_valid_case_rules():
    """Test case-based validation rules."""
    assert is_word_valid("hello", ["lowercase"]) == True
    assert is_word_valid("HELLO", ["lowercase"]) == False
    
    assert is_word_valid("HELLO", ["uppercase"]) == True
    assert is_word_valid("hello", ["uppercase"]) == False

def test_is_word_valid_multiple_rules():
    """Test multiple rules applied together."""
    assert is_word_valid("hello", ["min_length:4", "contains:h", "ends_with:lo"]) == True
    assert is_word_valid("hello", ["min_length:4", "contains:x", "ends_with:lo"]) == False

def test_is_word_valid_input_validation():
    """Test input validation for is_word_valid function."""
    assert is_word_valid(None, []) == False
    assert is_word_valid("", []) == False
    assert is_word_valid("hello", None) == False