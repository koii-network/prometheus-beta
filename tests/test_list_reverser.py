import pytest
from src.list_reverser import reverse_list_with_stack, Stack

def test_reverse_list_with_stack():
    # Test normal list of integers
    test_list = [1, 2, 3, 4, 5]
    result = reverse_list_with_stack(test_list)
    assert result == [5, 4, 3, 2, 1], "Should reverse the list correctly"

def test_reverse_empty_list():
    # Test empty list
    test_list = []
    result = reverse_list_with_stack(test_list)
    assert result == [], "Should return an empty list"

def test_reverse_single_element_list():
    # Test list with single element
    test_list = [42]
    result = reverse_list_with_stack(test_list)
    assert result == [42], "Should return the same list"

def test_reverse_large_list():
    # Test a larger list
    test_list = list(range(1000))
    result = reverse_list_with_stack(test_list)
    assert result == list(range(999, -1, -1)), "Should reverse a large list"

def test_stack_implementation():
    # Test Stack data structure
    stack = Stack()
    
    # Test push and pop
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2, "Should pop the last added item"
    assert stack.pop() == 1, "Should pop the next item"
    
    # Test is_empty
    assert stack.is_empty(), "Stack should be empty after all items are popped"
    
    # Test pop from empty stack raises IndexError
    with pytest.raises(IndexError):
        stack.pop()