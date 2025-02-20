import pytest
from src.min_path_sum import TreeNode, min_path_sum

def test_empty_tree():
    """Test minimum path sum for an empty tree"""
    assert min_path_sum(None) == float('inf')

def test_single_node_tree():
    """Test minimum path sum for a tree with only root node"""
    root = TreeNode(5)
    assert min_path_sum(root) == 5

def test_simple_tree_with_left_path():
    """Test a simple tree with only left path"""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    assert min_path_sum(root) == 18  # 10 + 5 + 3

def test_simple_tree_with_right_path():
    """Test a simple tree with only right path"""
    root = TreeNode(10)
    root.right = TreeNode(7)
    root.right.right = TreeNode(2)
    assert min_path_sum(root) == 19  # 10 + 7 + 2

def test_complex_tree():
    """Test a more complex tree with multiple paths"""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(2)
    root.right.left = TreeNode(6)
    
    # The minimum path should be: 10 + 5 + 3 = 18
    assert min_path_sum(root) == 18

def test_negative_values():
    """Test tree with negative values"""
    root = TreeNode(-10)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    root.left.left = TreeNode(-3)
    root.right.right = TreeNode(-2)
    
    # The minimum path should be: -10 + 5 + (-3) = -8
    assert min_path_sum(root) == -8