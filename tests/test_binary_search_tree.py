import pytest
from src.binary_search_tree import BinarySearchTree, Node

def test_insert_to_empty_tree():
    """Test inserting into an empty tree creates root node."""
    bst = BinarySearchTree()
    node = bst.insert(5)
    
    assert bst.root is not None
    assert bst.root.key == 5
    assert bst.root.left is None
    assert bst.root.right is None

def test_insert_multiple_nodes():
    """Test inserting multiple nodes maintains BST properties."""
    bst = BinarySearchTree()
    
    # Insert values that create a balanced-ish tree
    values = [5, 3, 7, 1, 4, 6, 8]
    for val in values:
        bst.insert(val)
    
    # Verify root
    assert bst.root.key == 5
    
    # Verify left subtree
    assert bst.root.left.key == 3
    assert bst.root.left.left.key == 1
    assert bst.root.left.right.key == 4
    
    # Verify right subtree
    assert bst.root.right.key == 7
    assert bst.root.right.left.key == 6
    assert bst.root.right.right.key == 8

def test_insert_duplicate_values():
    """Test inserting duplicate values goes to the right subtree."""
    bst = BinarySearchTree()
    
    bst.insert(5)
    bst.insert(5)
    
    assert bst.root.key == 5
    assert bst.root.right is not None
    assert bst.root.right.key == 5
    assert bst.root.left is None

def test_insert_raises_on_none():
    """Test inserting None raises a ValueError."""
    bst = BinarySearchTree()
    
    with pytest.raises(ValueError, match="Cannot insert None as a key"):
        bst.insert(None)

def test_large_dataset():
    """Test inserting a large number of nodes."""
    bst = BinarySearchTree()
    values = list(range(1, 1001))  # 1 to 1000
    
    # Insert all values
    for val in values:
        bst.insert(val)
    
    # Verify root and some properties
    assert bst.root.key == 1
    assert bst.root.left is None
    
    # Verify the rightmost node is 1000
    current = bst.root
    while current.right:
        current = current.right
    
    assert current.key == 1000