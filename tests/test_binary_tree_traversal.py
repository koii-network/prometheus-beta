import pytest
from src.binary_tree_traversal import TreeNode, traverse_tree

def test_empty_tree():
    """Test traversal of an empty tree"""
    result = traverse_tree(None)
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

def test_full_binary_tree():
    """Test traversal of a full binary tree"""
    #     1
    #   /   \
    #  2     3
    # / \   / \
    #4   5 6   7
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

def test_left_skewed_tree():
    """Test traversal of a left-skewed tree"""
    #   1
    #  /
    # 2
    #/
    #3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    
    result = traverse_tree(root)
    
    assert result == {
        'pre_order': [1, 2, 3],
        'in_order': [3, 2, 1],
        'post_order': [3, 2, 1]
    }

def test_right_skewed_tree():
    """Test traversal of a right-skewed tree"""
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    
    result = traverse_tree(root)
    
    assert result == {
        'pre_order': [1, 2, 3],
        'in_order': [1, 2, 3],
        'post_order': [3, 2, 1]
    }