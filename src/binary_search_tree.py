class Node:
    """
    Represents a node in a Binary Search Tree.
    
    Attributes:
        key: The value stored in the node
        left: Reference to the left child node (smaller values)
        right: Reference to the right child node (larger values)
    """
    def __init__(self, key):
        """
        Initialize a new node with the given key.
        
        Args:
            key: The value to be stored in the node
        """
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Binary Search Tree implementation with insertion method.
    
    Ensures BST properties:
    1. Left subtree contains only nodes with keys less than the node's key
    2. Right subtree contains only nodes with keys greater than the node's key
    3. Both left and right subtrees are binary search trees
    """
    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        """
        self.root = None
    
    def insert(self, key):
        """
        Insert a new key into the Binary Search Tree.
        
        Args:
            key: The value to be inserted
        
        Returns:
            Node: The newly inserted node
        
        Raises:
            ValueError: If the key is None
        """
        # Validate input
        if key is None:
            raise ValueError("Cannot insert None as a key")
        
        # If tree is empty, create root
        if self.root is None:
            self.root = Node(key)
            return self.root
        
        # Start at the root
        current = self.root
        
        while True:
            # If key is less than current node, go left
            if key < current.key:
                if current.left is None:
                    # Insert as left child if no left child exists
                    current.left = Node(key)
                    return current.left
                current = current.left
            
            # If key is greater than or equal to current node, go right
            else:
                if current.right is None:
                    # Insert as right child if no right child exists
                    current.right = Node(key)
                    return current.right
                current = current.right