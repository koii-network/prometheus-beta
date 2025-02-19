import pytest
from src.list_reverser import reverse_list_with_stack, Stack

def test_stack_implementation():
    stack = Stack()
    assert stack.is_empty() == True
    
    stack.push(1)
    assert stack.is_empty() == False
    
    item = stack.pop()
    assert item == 1
    assert stack.is_empty() == True
    
    with pytest.raises(IndexError):
        stack.pop()

def test_reverse_list_with_stack():
    # Test normal list
    input_list = [1, 2, 3, 4, 5]
    result = reverse_list_with_stack(input_list)
    assert result == [5, 4, 3, 2, 1]
    
    # Test list with single element
    input_list = [42]
    result = reverse_list_with_stack(input_list)
    assert result == [42]
    
    # Test empty list
    input_list = []
    result = reverse_list_with_stack(input_list)
    assert result == []
    
    # Test list with different types of integers
    input_list = [-1, 0, 100, -50]
    result = reverse_list_with_stack(input_list)
    assert result == [-50, 100, 0, -1]

def test_reverse_list_with_stack_not_modifying_original():
    # Ensure the original list is not modified
    input_list = [1, 2, 3]
    result = reverse_list_with_stack(input_list)
    assert result == [3, 2, 1]
    assert input_list == [1, 2, 3]