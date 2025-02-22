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
    """Helper function to convert a linked list to a list of values."""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

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

def test_reverse_multiple_node_list():
    """Test reversing a list with multiple nodes."""
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)
    
    # Check the list is reversed
    assert linked_list_to_list(reversed_head) == list(reversed(values))

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    values = [1, 2]
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)
    
    # Check the list is reversed
    assert linked_list_to_list(reversed_head) == list(reversed(values))

def test_in_place_reversal():
    """Verify that the reversal is done in-place."""
    values = [1, 2, 3]
    head = create_linked_list(values)
    
    # Get the original node references
    original_nodes = []
    current = head
    while current:
        original_nodes.append(current)
        current = current.next
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Check that the actual node objects are the same, just relinked
    current = reversed_head
    for node in reversed(original_nodes):
        assert current is node
        current = current.next