import pytest
from src.linked_list import ListNode, reverse_linked_list

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a list for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_reverse_linked_list_normal():
    """Test reversing a typical linked list."""
    input_list = create_linked_list([1, 2, 3, 4, 5])
    reversed_list = reverse_linked_list(input_list)
    assert linked_list_to_list(reversed_list) == [5, 4, 3, 2, 1]

def test_reverse_linked_list_single_element():
    """Test reversing a linked list with a single element."""
    input_list = create_linked_list([42])
    reversed_list = reverse_linked_list(input_list)
    assert linked_list_to_list(reversed_list) == [42]

def test_reverse_linked_list_empty():
    """Test reversing an empty linked list."""
    input_list = None
    reversed_list = reverse_linked_list(input_list)
    assert reversed_list is None

def test_reverse_linked_list_two_elements():
    """Test reversing a linked list with two elements."""
    input_list = create_linked_list([1, 2])
    reversed_list = reverse_linked_list(input_list)
    assert linked_list_to_list(reversed_list) == [2, 1]