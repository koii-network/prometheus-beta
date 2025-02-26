import pytest
from src.binary_tree_dfs import TreeNode, dfs_ascending_order

def test_empty_tree():
    """Test that an empty tree (None) returns an empty list."""
    assert dfs_ascending_order(None) == []

def test_single_node_tree():
    """Test a tree with a single node."""
    root = TreeNode(5)
    assert dfs_ascending_order(root) == [5]

def test_balanced_binary_search_tree():
    """Test a balanced binary search tree."""
    #       4
    #     /   \
    #    2     6
    #   / \   / \
    #  1   3 5   7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    
    assert dfs_ascending_order(root) == [1, 2, 3, 4, 5, 6, 7]

def test_skewed_tree():
    """Test a right-skewed tree."""
    #   1
    #    \
    #     2
    #      \
    #       3
    #        \
    #         4
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    
    assert dfs_ascending_order(root) == [1, 2, 3, 4]

def test_invalid_input():
    """Test that an invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        dfs_ascending_order("not a tree")
    
    with pytest.raises(TypeError):
        dfs_ascending_order(42)

def test_duplicate_values():
    """Test a tree with duplicate values."""
    #       4
    #     /   \
    #    2     4
    #   / \   / \
    #  2   3 4   5
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    assert dfs_ascending_order(root) == [2, 2, 3, 4, 4, 4, 5]