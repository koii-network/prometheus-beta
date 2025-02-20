import pytest
from src.custom_stack import CustomStack

def test_push_and_pop():
    """Test basic push and pop operations."""
    stack = CustomStack()
    stack.push(1)
    stack.push("hello")
    stack.push(3.14)
    
    assert stack.pop() == 3.14
    assert stack.pop() == "hello"
    assert stack.pop() == 1

def test_peek():
    """Test peek operation."""
    stack = CustomStack()
    stack.push(42)
    assert stack.peek() == 42
    assert stack.peek() == 42  # Peek should not remove the item
    assert stack.size() == 1

def test_is_empty():
    """Test is_empty method."""
    stack = CustomStack()
    assert stack.is_empty() == True
    
    stack.push(10)
    assert stack.is_empty() == False
    
    stack.pop()
    assert stack.is_empty() == True

def test_stack_capacity():
    """Test stack capacity limit."""
    stack = CustomStack(capacity=3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    with pytest.raises(ValueError):
        stack.push(4)  # Should raise ValueError when stack is full

def test_pop_empty_stack():
    """Test popping from an empty stack raises an IndexError."""
    stack = CustomStack()
    with pytest.raises(IndexError):
        stack.pop()

def test_peek_empty_stack():
    """Test peeking an empty stack raises an IndexError."""
    stack = CustomStack()
    with pytest.raises(IndexError):
        stack.peek()

def test_mixed_data_types():
    """Test stack with mixed data types."""
    stack = CustomStack()
    stack.push(1)
    stack.push("string")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})
    
    assert stack.pop() == {"key": "value"}
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "string"
    assert stack.pop() == 1
    assert stack.is_empty()