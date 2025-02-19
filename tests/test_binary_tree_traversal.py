import pytest
from src.binary_tree_traversal import TreeNode, tree_traversals

def test_empty_tree():
    """Test traversals on an empty tree"""
    result = tree_traversals(None)
    assert result == {'pre_order': [], 'in_order': [], 'post_order': []}

def test_single_node_tree():
    """Test traversals on a single node tree"""
    root = TreeNode(1)
    result = tree_traversals(root)
    assert result == {
        'pre_order': [1],
        'in_order': [1],
        'post_order': [1]
    }

def test_simple_binary_tree():
    """Test traversals on a small binary tree"""
    #       1
    #     /   \
    #    2     3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    result = tree_traversals(root)
    assert result == {
        'pre_order': [1, 2, 3],
        'in_order': [2, 1, 3],
        'post_order': [2, 3, 1]
    }

def test_complex_binary_tree():
    """Test traversals on a more complex binary tree"""
    #        4
    #      /   \
    #     2     6
    #    / \   / \
    #   1   3 5   7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    
    result = tree_traversals(root)
    assert result == {
        'pre_order': [4, 2, 1, 3, 6, 5, 7],
        'in_order': [1, 2, 3, 4, 5, 6, 7],
        'post_order': [1, 3, 2, 5, 7, 6, 4]
    }

def test_unbalanced_tree():
    """Test traversals on an unbalanced tree"""
    #    1
    #     \
    #      2
    #       \
    #        3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    
    result = tree_traversals(root)
    assert result == {
        'pre_order': [1, 2, 3],
        'in_order': [1, 2, 3],
        'post_order': [3, 2, 1]
    }