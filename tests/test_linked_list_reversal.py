import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_reverse_linked_list_multiple_elements():
    """Test reversing a linked list with multiple elements"""
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_linked_list_single_element():
    """Test reversing a linked list with a single element"""
    head = create_linked_list([42])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [42]

def test_reverse_linked_list_empty():
    """Test reversing an empty linked list"""
    head = create_linked_list([])
    reversed_head = reverse_linked_list(head)
    assert reversed_head is None

def test_reverse_linked_list_two_elements():
    """Test reversing a linked list with two elements"""
    head = create_linked_list([10, 20])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [20, 10]