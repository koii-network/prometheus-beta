import pytest
from src.zigzag_traversal import TreeNode, zigzag_level_order

def test_empty_tree():
    """Test zigzag traversal of an empty tree."""
    assert zigzag_level_order(None) == []

def test_single_node_tree():
    """Test zigzag traversal of a tree with a single node."""
    root = TreeNode(1)
    assert zigzag_level_order(root) == [[1]]

def test_simple_zigzag_tree():
    """Test a simple tree with multiple levels in zigzag order."""
    # Tree structure:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    expected = [[3], [20, 9], [15, 7]]
    assert zigzag_level_order(root) == expected

def test_complex_zigzag_tree():
    """Test a more complex tree with multiple levels in zigzag order."""
    # Tree structure:
    #           1
    #         /   \
    #        2     3
    #       / \   / \
    #      4   5 6   7
    #     /   /   \   \
    #    8   9    10   11
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.right.left = TreeNode(9)
    root.right.left.right = TreeNode(10)
    root.right.right.right = TreeNode(11)
    
    expected = [[1], [3, 2], [4, 5, 6, 7], [11, 10, 9, 8]]
    assert zigzag_level_order(root) == expected