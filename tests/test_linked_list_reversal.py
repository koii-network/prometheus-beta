import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def create_linked_list(values):
    """
    Helper function to create a linked list from a list of values.
    
    Args:
        values (list): List of values to create the linked list from.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """
    Convert a linked list to a list for easy comparison.
    
    Args:
        head (ListNode): Head of the linked list.
    
    Returns:
        list: Values of the linked list in order.
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_reverse_linked_list_normal():
    """Test reversing a normal linked list."""
    # Arrange
    original = create_linked_list([1, 2, 3, 4, 5])
    
    # Act
    reversed_list = reverse_linked_list(original)
    
    # Assert
    assert linked_list_to_list(reversed_list) == [5, 4, 3, 2, 1]

def test_reverse_linked_list_single_node():
    """Test reversing a linked list with a single node."""
    # Arrange
    original = create_linked_list([42])
    
    # Act
    reversed_list = reverse_linked_list(original)
    
    # Assert
    assert linked_list_to_list(reversed_list) == [42]

def test_reverse_linked_list_empty():
    """Test reversing an empty linked list."""
    # Arrange & Act
    reversed_list = reverse_linked_list(None)
    
    # Assert
    assert reversed_list is None

def test_reverse_linked_list_two_nodes():
    """Test reversing a linked list with two nodes."""
    # Arrange
    original = create_linked_list([1, 2])
    
    # Act
    reversed_list = reverse_linked_list(original)
    
    # Assert
    assert linked_list_to_list(reversed_list) == [2, 1]

def test_reverse_linked_list_preserve_integrity():
    """Ensure the reverse operation doesn't break list integrity."""
    # Arrange
    original = create_linked_list([10, 20, 30, 40, 50])
    
    # Act
    reversed_list = reverse_linked_list(original)
    
    # Assert
    current = reversed_list
    expected_values = [50, 40, 30, 20, 10]
    for expected in expected_values:
        assert current is not None
        assert current.val == expected
        current = current.next
    
    assert current is None