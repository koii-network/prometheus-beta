import pytest
from src.binary_search_tree import TreeNode, insert_node, inorder_traversal

def test_insert_empty_tree():
    root = None
    root = insert_node(root, 5)
    assert root.key == 5
    assert root.left is None
    assert root.right is None

def test_insert_multiple_nodes():
    root = None
    root = insert_node(root, 5)
    root = insert_node(root, 3)
    root = insert_node(root, 7)
    
    # Check inorder traversal to verify BST properties
    assert inorder_traversal(root) == [3, 5, 7]

def test_insert_duplicate():
    root = None
    root = insert_node(root, 5)
    root = insert_node(root, 5)
    
    # Should not insert duplicate
    assert inorder_traversal(root) == [5]

def test_complex_insertion():
    root = None
    nums = [10, 5, 15, 3, 7, 12, 18]
    for num in nums:
        root = insert_node(root, num)
    
    # Verify correct insertion order
    assert inorder_traversal(root) == [3, 5, 7, 10, 12, 15, 18]

def test_large_tree():
    root = None
    nums = range(1, 11)  # 1 to 10
    for num in nums:
        root = insert_node(root, num)
    
    assert inorder_traversal(root) == list(range(1, 11))

def test_insertion_order_independence():
    # Test that insertion order doesn't affect the final tree structure
    permutations = [
        [5, 3, 7, 1, 4, 6, 8],
        [8, 6, 1, 7, 4, 3, 5],
        [1, 4, 3, 8, 6, 5, 7]
    ]
    
    for perm in permutations:
        root = None
        for num in perm:
            root = insert_node(root, num)
        
        assert inorder_traversal(root) == [1, 3, 4, 5, 6, 7, 8]