import pytest
from src.custom_stack import CustomStack

def test_custom_stack_initialization():
    stack = CustomStack()
    assert len(stack) == 0
    assert stack.is_empty() == True

def test_custom_stack_push():
    stack = CustomStack()
    stack.push(1)
    assert len(stack) == 1
    assert stack.is_empty() == False
    stack.push("hello")
    assert len(stack) == 2

def test_custom_stack_pop():
    stack = CustomStack()
    stack.push(42)
    popped_item = stack.pop()
    assert popped_item == 42
    assert len(stack) == 0
    assert stack.is_empty() == True

def test_custom_stack_peek():
    stack = CustomStack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert len(stack) == 2  # Peek should not remove the item

def test_custom_stack_multiple_data_types():
    stack = CustomStack()
    stack.push(1)
    stack.push("string")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})
    assert len(stack) == 4

def test_custom_stack_capacity():
    stack = CustomStack(capacity=3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    with pytest.raises(OverflowError):
        stack.push(4)

def test_custom_stack_empty_pop():
    stack = CustomStack()
    with pytest.raises(IndexError):
        stack.pop()

def test_custom_stack_empty_peek():
    stack = CustomStack()
    with pytest.raises(IndexError):
        stack.peek()

def test_custom_stack_invalid_capacity():
    with pytest.raises(ValueError):
        CustomStack(capacity=0)
    
    with pytest.raises(ValueError):
        CustomStack(capacity=-1)