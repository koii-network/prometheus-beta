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
    """Helper function to convert linked list to list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_reverse_empty_list():
    """Test reversing an empty list"""
    head = None
    reversed_head = reverse_linked_list(head)
    assert reversed_head is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node"""
    head = ListNode(42)
    reversed_head = reverse_linked_list(head)
    assert reversed_head.val == 42
    assert reversed_head.next is None

def test_reverse_multiple_node_list():
    """Test reversing a list with multiple nodes"""
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == list(reversed(values))

def test_verify_in_place_reversal():
    """Verify that the reversal is done in-place"""
    values = [10, 20, 30, 40]
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)
    
    # Check values are reversed
    assert linked_list_to_list(reversed_head) == list(reversed(values))
    
    # Check that nodes are the same objects, just relinked
    first_node = reversed_head
    second_node = first_node.next
    assert first_node.val == 40
    assert second_node.val == 30