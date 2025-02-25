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
    """Helper function to convert a linked list to a list for easy comparison."""
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
    single_node = ListNode(42)
    reversed_list = reverse_linked_list(single_node)
    assert reversed_list.val == 42
    assert reversed_list.next is None

def test_reverse_multiple_nodes_list():
    """Test reversing a list with multiple nodes."""
    original_list = create_linked_list([1, 2, 3, 4, 5])
    reversed_list = reverse_linked_list(original_list)
    
    # Check the reversed list
    assert linked_list_to_list(reversed_list) == [5, 4, 3, 2, 1]

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    original_list = create_linked_list([10, 20])
    reversed_list = reverse_linked_list(original_list)
    
    # Check the reversed list
    assert linked_list_to_list(reversed_list) == [20, 10]

def test_reverse_preserves_list_length():
    """Ensure the reversal maintains the original list's length."""
    original_values = [1, 2, 3, 4, 5]
    original_list = create_linked_list(original_values)
    reversed_list = reverse_linked_list(original_list)
    
    # Count nodes in the reversed list
    count = 0
    current = reversed_list
    while current:
        count += 1
        current = current.next
    
    assert count == len(original_values)

def test_multiple_reversals():
    """Test that multiple reversals work correctly."""
    original_list = create_linked_list([1, 2, 3])
    
    # First reversal
    first_reverse = reverse_linked_list(original_list)
    assert linked_list_to_list(first_reverse) == [3, 2, 1]
    
    # Second reversal
    second_reverse = reverse_linked_list(first_reverse)
    assert linked_list_to_list(second_reverse) == [1, 2, 3]