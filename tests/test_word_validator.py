import pytest
from src.word_validator import Queue, is_word_valid

# Queue tests
def test_queue_basic_operations():
    q = Queue()
    assert q.is_empty() == True
    assert q.size() == 0
    
    q.enqueue(1)
    assert q.is_empty() == False
    assert q.size() == 1
    assert q.peek() == 1
    
    item = q.dequeue()
    assert item == 1
    assert q.is_empty() == True
    assert q.size() == 0

def test_queue_multiple_items():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.size() == 3
    assert q.peek() == 1
    
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() == True

def test_queue_error_cases():
    q = Queue()
    
    with pytest.raises(IndexError):
        q.dequeue()
    
    with pytest.raises(IndexError):
        q.peek()

# is_word_valid tests
def test_word_valid_no_rules():
    assert is_word_valid("hello", []) == True
    assert is_word_valid("", []) == True

def test_word_valid_min_length():
    assert is_word_valid("hello", ["min_length:3"]) == True
    assert is_word_valid("hi", ["min_length:3"]) == False
    assert is_word_valid("hello", ["min_length:5"]) == True
    assert is_word_valid("hi", ["min_length:5"]) == False

def test_word_valid_max_length():
    assert is_word_valid("hello", ["max_length:5"]) == True
    assert is_word_valid("hello world", ["max_length:5"]) == False
    assert is_word_valid("hi", ["max_length:5"]) == True

def test_word_valid_contains():
    assert is_word_valid("hello", ["contains:h"]) == True
    assert is_word_valid("hello", ["contains:x"]) == False
    assert is_word_valid("hello", ["contains:o"]) == True

def test_word_valid_starts_with():
    assert is_word_valid("hello", ["starts_with:he"]) == True
    assert is_word_valid("hello", ["starts_with:x"]) == False
    assert is_word_valid("hello", ["starts_with:hello"]) == True

def test_word_valid_ends_with():
    assert is_word_valid("hello", ["ends_with:lo"]) == True
    assert is_word_valid("hello", ["ends_with:x"]) == False
    assert is_word_valid("hello", ["ends_with:hello"]) == True

def test_word_valid_multiple_rules():
    assert is_word_valid("hello", ["min_length:3", "max_length:5", "contains:l"]) == True
    assert is_word_valid("hello", ["min_length:6", "max_length:5"]) == False
    assert is_word_valid("hello", ["starts_with:he", "ends_with:lo"]) == True

def test_word_valid_invalid_input():
    assert is_word_valid(123, []) == False
    
    with pytest.raises(ValueError):
        is_word_valid("hello", ["invalid_rule"])
    
    with pytest.raises(ValueError):
        is_word_valid("hello", ["min_length:abc"])
    
    with pytest.raises(ValueError):
        is_word_valid("hello", [123])