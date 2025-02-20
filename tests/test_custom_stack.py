import pytest
from src.custom_stack import CustomStack

def test_stack_initialization():
    """Test stack initialization and default capacity."""
    stack = CustomStack()
    assert len(stack) == 0
    assert stack.is_empty() == True

def test_push_and_pop():
    """Test pushing and popping items from the stack."""
    stack = CustomStack()
    
    # Push different types of items
    stack.push(10)
    stack.push("hello")
    stack.push([1, 2, 3])
    
    # Check length and peek
    assert len(stack) == 3
    assert stack.peek() == [1, 2, 3]
    
    # Pop items
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 10
    
    assert stack.is_empty() == True

def test_stack_capacity():
    """Test stack capacity limit."""
    stack = CustomStack(capacity=2)
    
    stack.push(1)
    stack.push(2)
    
    # Try to push beyond capacity
    with pytest.raises(ValueError, match="Stack is full"):
        stack.push(3)

def test_empty_stack_operations():
    """Test operations on an empty stack."""
    stack = CustomStack()
    
    # Peek on empty stack
    with pytest.raises(IndexError, match="Cannot peek an empty stack"):
        stack.peek()
    
    # Pop from empty stack
    with pytest.raises(IndexError, match="Cannot pop from an empty stack"):
        stack.pop()