import pytest
from src.list_reverser import reverse_list_with_stack, Stack

def test_reverse_list_normal():
    """Test reversing a standard list of integers"""
    input_list = [1, 2, 3, 4, 5]
    assert reverse_list_with_stack(input_list) == [5, 4, 3, 2, 1]

def test_reverse_list_empty():
    """Test reversing an empty list"""
    assert reverse_list_with_stack([]) == []

def test_reverse_list_single_element():
    """Test reversing a list with a single element"""
    input_list = [42]
    assert reverse_list_with_stack(input_list) == [42]

def test_stack_implementation():
    """Test the Stack data structure implementation"""
    stack = Stack()
    
    # Test pushing and popping elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    
    # Test is_empty method
    assert stack.is_empty() == True
    
    # Test popping from empty stack raises IndexError
    with pytest.raises(IndexError):
        stack.pop()

def test_reverse_list_with_duplicates():
    """Test reversing a list with duplicate elements"""
    input_list = [1, 2, 2, 3, 3, 1]
    assert reverse_list_with_stack(input_list) == [1, 3, 3, 2, 2, 1]