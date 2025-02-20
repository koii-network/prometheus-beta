import pytest
from src.binary_tree_dfs import TreeNode, dfs_ascending_order

def test_empty_tree():
    """Test DFS on an empty tree"""
    assert dfs_ascending_order(None) == []

def test_single_node_tree():
    """Test DFS on a tree with a single node"""
    root = TreeNode(5)
    assert dfs_ascending_order(root) == [5]

def test_balanced_binary_search_tree():
    """Test DFS on a balanced binary search tree"""
    # Create a balanced BST
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
    """Test DFS on an unbalanced binary search tree"""
    # Create an unbalanced BST
    #       5
    #      /
    #     3
    #    /
    #   1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    
    assert dfs_ascending_order(root) == [1, 3, 5]

def test_tree_with_duplicate_values():
    """Test DFS on a tree with duplicate values"""
    root = TreeNode(4)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    
    assert dfs_ascending_order(root) == [4, 4, 5]