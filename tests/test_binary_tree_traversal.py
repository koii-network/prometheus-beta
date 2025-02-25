import pytest
from src.binary_tree_traversal import TreeNode, tree_traversals

def test_empty_tree():
    """Test traversals on an empty tree"""
    root = None
    result = tree_traversals(root)
    assert result == {
        'pre_order': [],
        'in_order': [],
        'post_order': []
    }

def test_single_node_tree():
    """Test traversals on a single-node tree"""
    root = TreeNode(1)
    result = tree_traversals(root)
    assert result == {
        'pre_order': [1],
        'in_order': [1],
        'post_order': [1]
    }

def test_full_binary_tree():
    """Test traversals on a full binary tree"""
    # Create the following tree:
    #        1
    #      /   \
    #     2     3
    #   /  \   / \
    #  4    5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    result = tree_traversals(root)
    
    # Pre-order: root, left, right
    assert result['pre_order'] == [1, 2, 4, 5, 3, 6, 7]
    
    # In-order: left, root, right
    assert result['in_order'] == [4, 2, 5, 1, 6, 3, 7]
    
    # Post-order: left, right, root
    assert result['post_order'] == [4, 5, 2, 6, 7, 3, 1]

def test_unbalanced_tree():
    """Test traversals on an unbalanced tree"""
    # Create the following unbalanced tree:
    #        1
    #       /
    #      2
    #     /
    #    3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    
    result = tree_traversals(root)
    
    # Pre-order: root, left, right
    assert result['pre_order'] == [1, 2, 3]
    
    # In-order: left, root, right
    assert result['in_order'] == [3, 2, 1]
    
    # Post-order: left, right, root
    assert result['post_order'] == [3, 2, 1]