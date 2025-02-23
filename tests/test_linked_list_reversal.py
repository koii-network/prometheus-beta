import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

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
    """Convert a linked list to a list for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    head = ListNode(1)
    reversed_head = reverse_linked_list(head)
    assert reversed_head.val == 1
    assert reversed_head.next is None

def test_reverse_multiple_nodes():
    """Test reversing a list with multiple nodes."""
    original_values = [1, 2, 3, 4, 5]
    head = create_linked_list(original_values)
    reversed_head = reverse_linked_list(head)
    reversed_values = linked_list_to_list(reversed_head)
    assert reversed_values == list(reversed(original_values))

def test_reverse_two_nodes():
    """Test reversing a list with two nodes."""
    original_values = [1, 2]
    head = create_linked_list(original_values)
    reversed_head = reverse_linked_list(head)
    reversed_values = linked_list_to_list(reversed_head)
    assert reversed_values == list(reversed(original_values))

def test_reverse_maintains_node_relationships():
    """Ensure that node relationships are correctly maintained after reversal."""
    original_values = [1, 2, 3, 4, 5]
    head = create_linked_list(original_values)
    reversed_head = reverse_linked_list(head)
    current = reversed_head
    expected_values = list(reversed(original_values))
    
    for expected_val in expected_values:
        assert current.val == expected_val
        current = current.next
    
    assert current is None  # Ensure we've reached the end of the list