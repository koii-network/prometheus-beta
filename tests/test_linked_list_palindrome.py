import pytest
from src.linked_list_palindrome import ListNode, is_palindrome_linked_list

def create_linked_list(values):
    """
    Helper function to create a linked list from a list of values.
    
    Args:
        values (list): List of values to create the linked list.
    
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

def test_palindrome_list_even_length():
    """Test palindrome linked list with even number of elements."""
    head = create_linked_list([1, 2, 2, 1])
    assert is_palindrome_linked_list(head) == True

def test_palindrome_list_odd_length():
    """Test palindrome linked list with odd number of elements."""
    head = create_linked_list([1, 2, 3, 2, 1])
    assert is_palindrome_linked_list(head) == True

def test_non_palindrome_list():
    """Test non-palindrome linked list."""
    head = create_linked_list([1, 2, 3, 4])
    assert is_palindrome_linked_list(head) == False

def test_single_element_list():
    """Test single element list (always a palindrome)."""
    head = create_linked_list([1])
    assert is_palindrome_linked_list(head) == True

def test_empty_list():
    """Test empty list (considered a palindrome)."""
    head = create_linked_list([])
    assert is_palindrome_linked_list(head) == True

def test_two_element_palindrome():
    """Test two-element palindrome list."""
    head = create_linked_list([5, 5])
    assert is_palindrome_linked_list(head) == True

def test_two_element_non_palindrome():
    """Test two-element non-palindrome list."""
    head = create_linked_list([5, 6])
    assert is_palindrome_linked_list(head) == False

def test_longer_non_palindrome():
    """Test a longer non-palindrome list."""
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    assert is_palindrome_linked_list(head) == False

def test_multiple_digit_values():
    """Test palindrome with multi-digit values."""
    head = create_linked_list([11, 22, 33, 22, 11])
    assert is_palindrome_linked_list(head) == True