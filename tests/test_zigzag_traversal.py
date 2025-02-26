import pytest
from src.zigzag_traversal import TreeNode, zigzag_level_order

def test_empty_tree():
    """Test zigzag traversal of an empty tree."""
    assert zigzag_level_order(None) == []

def test_single_node_tree():
    """Test zigzag traversal of a single node tree."""
    root = TreeNode(1)
    assert zigzag_level_order(root) == [[1]]

def test_simple_tree():
    """Test zigzag traversal of a simple binary tree."""
    # Tree structure:
    #        3
    #      /   \
    #     9    20
    #         /  \
    #        15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    expected = [[3], [20, 9], [15, 7]]
    assert zigzag_level_order(root) == expected

def test_unbalanced_tree():
    """Test zigzag traversal of an unbalanced tree."""
    # Tree structure:
    #        1
    #      /   \
    #     2     3
    #    /       \
    #   4         5
    #  /           \
    # 6             7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    
    expected = [[1], [3, 2], [4, 5], [7, 6]]
    assert zigzag_level_order(root) == expected

def test_perfect_binary_tree():
    """Test zigzag traversal of a perfect binary tree."""
    # Tree structure:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    expected = [[1], [3, 2], [4, 5, 6, 7]]
    assert zigzag_level_order(root) == expected