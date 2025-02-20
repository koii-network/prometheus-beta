import pytest
from src.linked_list import ListNode, reverse_linked_list

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

def list_to_array(head):
    """Helper function to convert linked list to array for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_reverse_empty_list():
    """Test reversing an empty list"""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node"""
    head = ListNode(1)
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [1]

def test_reverse_multiple_nodes():
    """Test reversing a list with multiple nodes"""
    # Create original list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Check the reversed list
    assert list_to_array(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_two_node_list():
    """Test reversing a list with two nodes"""
    head = create_linked_list([10, 20])
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [20, 10]