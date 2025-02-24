import pytest
from src.binary_tree_zigzag_traversal import TreeNode, zigzag_level_order_traversal

def test_empty_tree():
    """Test traversal of an empty tree"""
    assert zigzag_level_order_traversal(None) == []

def test_single_node_tree():
    """Test traversal of a tree with a single node"""
    root = TreeNode(1)
    assert zigzag_level_order_traversal(root) == [[1]]

def test_complete_binary_tree():
    """Test zigzag traversal of a complete binary tree"""
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    expected = [[3], [20, 9], [15, 7]]
    assert zigzag_level_order_traversal(root) == expected

def test_unbalanced_tree():
    """Test zigzag traversal of an unbalanced tree"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)
    
    expected = [[1], [3, 2], [4, 5]]
    assert zigzag_level_order_traversal(root) == expected

def test_tree_with_negative_values():
    """Test zigzag traversal with negative node values"""
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(-4)
    root.right.right = TreeNode(-5)
    
    expected = [[-1], [-3, -2], [-4, -5]]
    assert zigzag_level_order_traversal(root) == expected