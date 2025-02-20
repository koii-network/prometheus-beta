import pytest
from src.custom_stack import CustomStack

def test_stack_initialization():
    """Test stack initialization with default and custom capacity."""
    stack = CustomStack()
    assert stack.capacity() == 10
    assert stack.is_empty() is True
    assert stack.size() == 0

    custom_stack = CustomStack(capacity=5)
    assert custom_stack.capacity() == 5

def test_push_and_pop():
    """Test pushing and popping items of different types."""
    stack = CustomStack()
    
    # Push different types of items
    stack.push(10)
    stack.push("hello")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})
    
    assert stack.size() == 4
    
    # Pop items and verify order
    assert stack.pop() == {"key": "value"}
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 10
    
    assert stack.is_empty() is True

def test_peek():
    """Test peeking at the top item without removing it."""
    stack = CustomStack()
    stack.push(42)
    
    assert stack.peek() == 42
    assert stack.size() == 1  # Peek should not remove the item

def test_stack_full():
    """Test stack overflow condition."""
    stack = CustomStack(capacity=2)
    stack.push(1)
    stack.push(2)
    
    with pytest.raises(OverflowError):
        stack.push(3)

def test_empty_stack_errors():
    """Test error conditions for empty stack."""
    stack = CustomStack()
    
    with pytest.raises(IndexError):
        stack.pop()
    
    with pytest.raises(IndexError):
        stack.peek()

def test_invalid_capacity():
    """Test initialization with invalid capacity."""
    with pytest.raises(ValueError):
        CustomStack(-1)
    
    with pytest.raises(ValueError):
        CustomStack(0)
    
    with pytest.raises(ValueError):
        CustomStack("not a number")