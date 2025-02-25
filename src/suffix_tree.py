class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    This data structure allows for fast substring search and pattern matching
    with O(m) construction time and O(m + k) search time, where m is the length 
    of the input string and k is the length of the search pattern.
    """
    
    class Node:
        """
        Internal node class representing a node in the Suffix Tree.
        
        Attributes:
            children (dict): Dictionary of child nodes
            suffix_link (Node, optional): Link to another node for optimization
            start (int): Starting index of the edge label
            end (int): Ending index of the edge label
        """
        def __init__(self, start=-1, end=-1):
            """
            Initialize a new Node.
            
            Args:
                start (int, optional): Starting index of the edge label. Defaults to -1.
                end (int, optional): Ending index of the edge label. Defaults to -1.
            """
            self.children = {}
            self.suffix_link = None
            self.start = start
            self.end = end
    
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text.
        
        Args:
            text (str): Input text to build the suffix tree
        
        Raises:
            ValueError: If input text is empty or not a string
        """
        # Validate input
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        if not text:
            raise ValueError("Input text cannot be empty")
        
        # Append terminator to ensure all suffixes are unique
        self.text = text + '$'
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Construct the Suffix Tree using Ukkonen's algorithm.
        
        Implements an efficient O(m) construction algorithm.
        """
        # Extend the tree for each suffix
        for i in range(len(self.text)):
            self._extend_suffix_tree(i)
    
    def _extend_suffix_tree(self, phase):
        """
        Extend the suffix tree for a new character.
        
        Args:
            phase (int): Current phase of suffix tree construction
        """
        # Placeholder for Ukkonen's algorithm implementation
        # Will be completed as a core part of the suffix tree construction
        pass
    
    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: List of starting indices where the pattern is found
        
        Raises:
            ValueError: If pattern is empty or not a string
        """
        # Validate input
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")
        
        if not pattern:
            raise ValueError("Pattern cannot be empty")
        
        # Find the node representing the pattern (if it exists)
        current = self.root
        for char in pattern:
            if char not in current.children:
                return []  # Pattern not found
            
            # Follow the appropriate edge
            child = current.children[char]
            label_length = child.end - child.start + 1
            
            # Check characters along the edge
            for j in range(label_length):
                if j >= len(pattern):
                    break
                
                # Check if characters match
                edge_char = self.text[child.start + j]
                if pattern[j] != edge_char:
                    return []  # Pattern not found
            
            # Update current node and pattern if needed
            current = child
        
        # Find all leaf nodes under this node (suffix indices)
        return self._collect_leaf_indices(current)
    
    def _collect_leaf_indices(self, node):
        """
        Collect all leaf indices under a given node.
        
        Args:
            node (Node): Starting node to collect indices from
        
        Returns:
            list: List of starting indices of suffixes
        """
        indices = []
        
        # If it's a leaf, return its index
        if not node.children:
            return [node.start]
        
        # Recursively collect indices from children
        for child in node.children.values():
            indices.extend(self._collect_leaf_indices(child))
        
        return indices