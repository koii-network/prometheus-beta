import pytest
from src.custom_stack import CustomStack

def test_stack_initialization():
    """Test stack initialization with default and custom capacity."""
    stack = CustomStack()
    assert stack.capacity() == 10
    assert len(stack) == 0
    assert stack.is_empty() == True

    custom_stack = CustomStack(capacity=5)
    assert custom_stack.capacity() == 5

def test_push_and_pop():
    """Test pushing and popping items of different types."""
    stack = CustomStack()
    
    # Push and pop different types
    stack.push(42)
    stack.push("hello")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})
    
    assert len(stack) == 4
    assert stack.pop() == {"key": "value"}
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 42
    assert stack.is_empty() == True

def test_peek():
    """Test peek operation."""
    stack = CustomStack()
    stack.push(10)
    assert stack.peek() == 10
    assert len(stack) == 1  # Peek should not remove the item

def test_stack_capacity():
    """Test stack capacity limit."""
    stack = CustomStack(capacity=3)
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    with pytest.raises(OverflowError):
        stack.push(4)

def test_error_handling():
    """Test error handling for edge cases."""
    stack = CustomStack()
    
    # Pop from empty stack
    with pytest.raises(IndexError):
        stack.pop()
    
    # Peek empty stack
    with pytest.raises(IndexError):
        stack.peek()
    
    # Invalid capacity
    with pytest.raises(ValueError):
        CustomStack(capacity=0)
    
    with pytest.raises(ValueError):
        CustomStack(capacity=-5)