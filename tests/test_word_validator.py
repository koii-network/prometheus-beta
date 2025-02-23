import pytest
from src.word_validator import Queue, is_word_valid

def test_queue_basic_operations():
    """Test basic Queue operations."""
    q = Queue()
    
    # Test initial state
    assert q.is_empty() == True
    assert q.size() == 0
    
    # Test enqueue
    q.enqueue(1)
    assert q.is_empty() == False
    assert q.size() == 1
    
    # Test dequeue
    assert q.dequeue() == 1
    assert q.is_empty() == True
    
    # Test multiple enqueue and dequeue
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.size() == 3
    assert q.dequeue() == 10
    assert q.size() == 2

def test_queue_error_handling():
    """Test Queue error handling."""
    q = Queue()
    
    # Test dequeue from empty queue
    with pytest.raises(IndexError, match="Cannot dequeue from an empty queue"):
        q.dequeue()

def test_is_word_valid_basic():
    """Test basic word validation."""
    # No rules - always valid
    assert is_word_valid("hello", []) == True
    
    # Simple length rule
    def length_rule(word):
        return len(word) >= 3
    
    assert is_word_valid("hi", [length_rule]) == False
    assert is_word_valid("hello", [length_rule]) == True

def test_is_word_valid_multiple_rules():
    """Test validation with multiple rules."""
    # Rule for minimum length
    def min_length_rule(word):
        return len(word) >= 3
    
    # Rule for containing only alphabets
    def alpha_rule(word):
        return word.isalpha()
    
    # Rule for starting with a capital letter
    def capital_rule(word):
        return word[0].isupper()
    
    rules = [min_length_rule, alpha_rule, capital_rule]
    
    # Should pass all rules
    assert is_word_valid("Hello", rules) == True
    
    # Fails length rule
    assert is_word_valid("Hi", rules) == False
    
    # Fails alphabet rule
    assert is_word_valid("Hello123", rules) == False
    
    # Fails capitalization rule
    assert is_word_valid("hello", rules) == False

def test_is_word_valid_error_handling():
    """Test error handling for invalid inputs."""
    # Invalid word type
    with pytest.raises(TypeError, match="Word must be a string"):
        is_word_valid(123, [])
    
    # Invalid rules type
    with pytest.raises(TypeError, match="Rules must be a list of functions"):
        is_word_valid("hello", "not a list")
    
    # Invalid rule (not callable)
    with pytest.raises(TypeError, match="Each rule must be a callable function"):
        is_word_valid("hello", [1, 2, 3])

def test_is_word_valid_edge_cases():
    """Test edge cases for word validation."""
    # Empty string
    def non_empty_rule(word):
        return len(word) > 0
    
    assert is_word_valid("", [non_empty_rule]) == False
    assert is_word_valid("", []) == True
    
    # Complex rule
    def contains_vowel_rule(word):
        return any(char in 'aeiouAEIOU' for char in word)
    
    assert is_word_valid("rhythm", [contains_vowel_rule]) == False
    assert is_word_valid("hello", [contains_vowel_rule]) == True