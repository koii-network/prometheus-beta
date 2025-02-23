import pytest
from src.binary_tree_traversals import Node, inorder_traversal, preorder_traversal, postorder_traversal

def test_empty_tree():
    """Test traversals on an empty tree (None)."""
    assert inorder_traversal(None) == []
    assert preorder_traversal(None) == []
    assert postorder_traversal(None) == []

def test_single_node_tree():
    """Test traversals on a single node tree."""
    root = Node(5)
    assert inorder_traversal(root) == [5]
    assert preorder_traversal(root) == [5]
    assert postorder_traversal(root) == [5]

def test_complete_binary_tree():
    """Test traversals on a complete binary tree."""
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Verify inorder traversal (left -> root -> right)
    assert inorder_traversal(root) == [4, 2, 5, 1, 6, 3, 7]

    # Verify preorder traversal (root -> left -> right)
    assert preorder_traversal(root) == [1, 2, 4, 5, 3, 6, 7]

    # Verify postorder traversal (left -> right -> root)
    assert postorder_traversal(root) == [4, 5, 2, 6, 7, 3, 1]

def test_unbalanced_tree():
    """Test traversals on an unbalanced tree."""
    #       1
    #      /
    #     2
    #    /
    #   3
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)

    # Verify inorder traversal
    assert inorder_traversal(root) == [3, 2, 1]

    # Verify preorder traversal
    assert preorder_traversal(root) == [1, 2, 3]

    # Verify postorder traversal
    assert postorder_traversal(root) == [3, 2, 1]