import pytest
from src.binary_tree_traversal import TreeNode, binary_tree_traversals

def test_empty_tree():
    """Test traversals on an empty tree"""
    result = binary_tree_traversals(None)
    assert result == {'preorder': [], 'inorder': [], 'postorder': []}

def test_single_node_tree():
    """Test traversals on a single node tree"""
    root = TreeNode(1)
    result = binary_tree_traversals(root)
    assert result == {'preorder': [1], 'inorder': [1], 'postorder': [1]}

def test_full_binary_tree():
    """Test traversals on a full binary tree"""
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
    
    result = binary_tree_traversals(root)
    
    assert result['preorder'] == [1, 2, 4, 5, 3, 6, 7]
    assert result['inorder'] == [4, 2, 5, 1, 6, 3, 7]
    assert result['postorder'] == [4, 5, 2, 6, 7, 3, 1]

def test_unbalanced_tree():
    """Test traversals on an unbalanced tree"""
    #        1
    #       /
    #      2
    #     /
    #    3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    
    result = binary_tree_traversals(root)
    
    assert result['preorder'] == [1, 2, 3]
    assert result['inorder'] == [3, 2, 1]
    assert result['postorder'] == [3, 2, 1]