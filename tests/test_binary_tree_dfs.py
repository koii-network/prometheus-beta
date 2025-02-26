import pytest
from src.binary_tree_dfs import TreeNode, dfs_ascending_order

def test_empty_tree():
    """Test that an empty tree returns an empty list."""
    assert dfs_ascending_order(None) == []

def test_single_node_tree():
    """Test a tree with a single node."""
    root = TreeNode(5)
    assert dfs_ascending_order(root) == [5]

def test_simple_balanced_tree():
    """Test a simple balanced binary tree."""
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

def test_unbalanced_tree():
    """Test an unbalanced tree with only left or right children."""
    #   5
    #  /
    # 3
    #  \
    #   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    
    assert dfs_ascending_order(root) == [3, 4, 5]

def test_invalid_input():
    """Test that invalid input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a TreeNode or None"):
        dfs_ascending_order("not a tree")
    
    with pytest.raises(TypeError, match="Input must be a TreeNode or None"):
        dfs_ascending_order(42)

def test_large_tree():
    """Test a larger tree to ensure correct ascending order."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)
    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(4)
    
    assert dfs_ascending_order(root) == [1, 3, 4, 5, 7, 10, 12, 15, 18]