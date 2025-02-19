import pytest
from src.binary_tree_traversal import TreeNode, traverse_tree

def test_empty_tree():
    """Test traversal of an empty tree"""
    root = None
    result = traverse_tree(root)
    assert result == {
        'pre_order': [],
        'in_order': [],
        'post_order': []
    }

def test_single_node_tree():
    """Test traversal of a tree with a single node"""
    root = TreeNode(1)
    result = traverse_tree(root)
    assert result == {
        'pre_order': [1],
        'in_order': [1],
        'post_order': [1]
    }

def test_complete_binary_tree():
    """Test traversal of a complete binary tree"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    result = traverse_tree(root)
    
    assert result == {
        'pre_order': [1, 2, 4, 5, 3, 6, 7],
        'in_order': [4, 2, 5, 1, 6, 3, 7],
        'post_order': [4, 5, 2, 6, 7, 3, 1]
    }

def test_skewed_tree():
    """Test traversal of a skewed binary tree"""
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    
    result = traverse_tree(root)
    
    assert result == {
        'pre_order': [1, 2, 3, 4],
        'in_order': [1, 2, 3, 4],
        'post_order': [4, 3, 2, 1]
    }