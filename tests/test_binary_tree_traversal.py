import pytest
from src.binary_tree_traversal import Node, in_order_traversal, pre_order_traversal, post_order_traversal

def test_empty_tree():
    """Test traversals on an empty tree (None)"""
    assert in_order_traversal(None) == []
    assert pre_order_traversal(None) == []
    assert post_order_traversal(None) == []

def test_single_node_tree():
    """Test traversals on a tree with a single node"""
    root = Node(1)
    assert in_order_traversal(root) == [1]
    assert pre_order_traversal(root) == [1]
    assert post_order_traversal(root) == [1]

def test_complete_binary_tree():
    """Test traversals on a complete binary tree"""
    # Tree structure:
    #        4
    #      /   \
    #     2     6
    #    / \   / \
    #   1   3 5   7
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    
    # In-order: Left -> Root -> Right
    assert in_order_traversal(root) == [1, 2, 3, 4, 5, 6, 7]
    
    # Pre-order: Root -> Left -> Right
    assert pre_order_traversal(root) == [4, 2, 1, 3, 6, 5, 7]
    
    # Post-order: Left -> Right -> Root
    assert post_order_traversal(root) == [1, 3, 2, 5, 7, 6, 4]

def test_unbalanced_tree():
    """Test traversals on an unbalanced tree"""
    # Tree structure:
    #    1
    #     \
    #      2
    #       \
    #        3
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    
    # In-order: Left -> Root -> Right
    assert in_order_traversal(root) == [1, 2, 3]
    
    # Pre-order: Root -> Left -> Right
    assert pre_order_traversal(root) == [1, 2, 3]
    
    # Post-order: Left -> Right -> Root
    assert post_order_traversal(root) == [3, 2, 1]