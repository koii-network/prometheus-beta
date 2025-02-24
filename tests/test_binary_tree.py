import pytest
from src.binary_tree import TreeNode, dfs_ascending

def test_empty_tree():
    """Test DFS on an empty tree returns an empty list."""
    assert dfs_ascending(None) == []

def test_single_node_tree():
    """Test DFS on a tree with a single node."""
    root = TreeNode(5)
    assert dfs_ascending(root) == [5]

def test_simple_balanced_tree():
    """Test DFS on a simple balanced binary search tree."""
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    
    assert dfs_ascending(root) == [1, 2, 3, 4, 5, 6, 7]

def test_unbalanced_tree():
    """Test DFS on an unbalanced tree."""
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(7)
    
    assert dfs_ascending(root) == [1, 2, 3, 5, 7]

def test_invalid_input():
    """Test that TypeError is raised for invalid input."""
    with pytest.raises(TypeError, match="Input must be a TreeNode or None"):
        dfs_ascending("not a tree")
    with pytest.raises(TypeError, match="Input must be a TreeNode or None"):
        dfs_ascending(42)

def test_duplicate_values():
    """Test tree with duplicate values."""
    root = TreeNode(4)
    root.left = TreeNode(4)
    root.right = TreeNode(4)
    
    assert dfs_ascending(root) == [4, 4, 4]