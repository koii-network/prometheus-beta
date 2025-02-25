import pytest
from src.list_reverser import reverse_list_with_stack, Stack


def test_stack_basic_operations():
    """Test basic Stack data structure operations."""
    stack = Stack()
    
    # Test is_empty on new stack
    assert stack.is_empty() is True
    
    # Test push and pop
    stack.push(1)
    assert stack.is_empty() is False
    assert stack.pop() == 1
    assert stack.is_empty() is True
    
    # Test multiple push and pop
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty() is True


def test_reverse_list_with_stack():
    """Test list reversal with various input scenarios."""
    # Test normal list
    assert reverse_list_with_stack([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    
    # Test empty list
    assert reverse_list_with_stack([]) == []
    
    # Test single element list
    assert reverse_list_with_stack([42]) == [42]
    
    # Test list with different types
    mixed_list = [1, "hello", True, 3.14]
    assert reverse_list_with_stack(mixed_list) == [3.14, True, "hello", 1]


def test_reverse_list_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list_with_stack("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list_with_stack(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list_with_stack(None)


def test_stack_pop_empty_error():
    """Test popping from an empty stack raises an IndexError."""
    stack = Stack()
    with pytest.raises(IndexError, match="Cannot pop from an empty stack"):
        stack.pop()