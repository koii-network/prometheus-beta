import pytest
from src.binary_tree_traversal import TreeNode, zigzag_level_order

def test_empty_tree():
    """Test zigzag traversal of an empty tree"""
    assert zigzag_level_order(None) == []

def test_single_node_tree():
    """Test zigzag traversal of a tree with a single node"""
    root = TreeNode(1)
    assert zigzag_level_order(root) == [[1]]

def test_simple_zigzag_tree():
    """Test a simple tree with multiple levels"""
    # Tree structure:
    #        3
    #       / \
    #      9  20
    #         / \
    #        15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    expected = [
        [3],        # Level 0: left to right
        [20, 9],    # Level 1: right to left
        [15, 7]     # Level 2: left to right
    ]
    
    assert zigzag_level_order(root) == expected

def test_unbalanced_tree():
    """Test a zigzag traversal on an unbalanced tree"""
    # Unbalanced tree with only left or right children
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)
    
    expected = [
        [1],        # Level 0: left to right
        [3, 2],     # Level 1: right to left
        [4, 5]      # Level 2: left to right
    ]
    
    assert zigzag_level_order(root) == expected