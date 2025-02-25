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

def test_reverse_empty_list():
    """Test reversing an empty list."""
    head = None
    reversed_head = reverse_linked_list(head)
    assert reversed_head is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    head = ListNode(42)
    reversed_head = reverse_linked_list(head)
    assert reversed_head.val == 42
    assert reversed_head.next is None

def test_reverse_multiple_nodes_list():
    """Test reversing a list with multiple nodes."""
    # Test list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    
    # Check the reversed list matches expected output
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    head = create_linked_list([10, 20])
    reversed_head = reverse_linked_list(head)
    
    # Check the reversed list matches expected output
    assert linked_list_to_list(reversed_head) == [20, 10]