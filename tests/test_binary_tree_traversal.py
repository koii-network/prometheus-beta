import pytest
from src.binary_tree_traversal import Node, traverse_in_order, traverse_pre_order, traverse_post_order

def test_empty_tree():
    """Test traversals on an empty tree (None)"""
    assert traverse_in_order(None) == []
    assert traverse_pre_order(None) == []
    assert traverse_post_order(None) == []

def test_single_node_tree():
    """Test traversals on a tree with only a root node"""
    root = Node(1)
    assert traverse_in_order(root) == [1]
    assert traverse_pre_order(root) == [1]
    assert traverse_post_order(root) == [1]

def test_complete_binary_tree():
    """Test traversals on a complete binary tree"""
    #     1
    #   /   \
    #  2     3
    # / \   / \
    #4   5 6   7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    # In-order should be: 4, 2, 5, 1, 6, 3, 7
    assert traverse_in_order(root) == [4, 2, 5, 1, 6, 3, 7]
    
    # Pre-order should be: 1, 2, 4, 5, 3, 6, 7
    assert traverse_pre_order(root) == [1, 2, 4, 5, 3, 6, 7]
    
    # Post-order should be: 4, 5, 2, 6, 7, 3, 1
    assert traverse_post_order(root) == [4, 5, 2, 6, 7, 3, 1]

def test_left_skewed_tree():
    """Test traversals on a left-skewed tree"""
    #   1
    #  /
    # 2
    #/
    #3
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    
    # In-order should be: 3, 2, 1
    assert traverse_in_order(root) == [3, 2, 1]
    
    # Pre-order should be: 1, 2, 3
    assert traverse_pre_order(root) == [1, 2, 3]
    
    # Post-order should be: 3, 2, 1
    assert traverse_post_order(root) == [3, 2, 1]

def test_right_skewed_tree():
    """Test traversals on a right-skewed tree"""
    # 1
    #  \
    #   2
    #    \
    #     3
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    
    # In-order should be: 1, 2, 3
    assert traverse_in_order(root) == [1, 2, 3]
    
    # Pre-order should be: 1, 2, 3
    assert traverse_pre_order(root) == [1, 2, 3]
    
    # Post-order should be: 3, 2, 1
    assert traverse_post_order(root) == [3, 2, 1]