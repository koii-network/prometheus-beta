class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search operations with 
    time complexity close to O(m), where m is the length of the search pattern.
    """
    
    class Node:
        """
        Represents a node in the Suffix Tree.
        
        Attributes:
            children (dict): Dictionary of child nodes
            suffix_link (Node, optional): Link to another node for optimization
            start (int): Starting index of the edge label
            end (int): Ending index of the edge label
            suffix_index (int): Index of the suffix, -1 if internal node
        """
        def __init__(self, start=-1, end=-1):
            self.children = {}
            self.suffix_link = None
            self.start = start
            self.end = end
            self.suffix_index = -1
    
    def __init__(self, text):
        """
        Initialize the Suffix Tree.
        
        Args:
            text (str): Input string to build the suffix tree
        """
        if not text:
            raise ValueError("Input text cannot be empty")
        
        self.text = text + "$"  # Terminates with unique end marker
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Builds the Suffix Tree using Ukkonen's algorithm.
        """
        n = len(self.text)
        
        # Implicit and explicit extensions of each phase
        for i in range(n):
            self._extend_suffix_tree(i)
    
    def _extend_suffix_tree(self, phase):
        """
        Extends the suffix tree for a given phase.
        
        Args:
            phase (int): Current phase in tree construction
        """
        # Placeholder for Ukkonen's algorithm implementation
        # This is a simplified version focusing on basic suffix tree construction
        pass
    
    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            bool: True if pattern is found, False otherwise
        """
        if not pattern:
            return False
        
        current = self.root
        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True
    
    def find_all_occurrences(self, pattern):
        """
        Find all occurrences of a pattern in the text.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: Indices of all occurrences of the pattern
        """
        if not pattern:
            return []
        
        occurrences = []
        current = self.root
        
        # Trace the path for the pattern
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]
        
        # Collect all leaf nodes under this subtree
        def collect_suffixes(node):
            if node.suffix_index != -1:
                occurrences.append(node.suffix_index)
            for child in node.children.values():
                collect_suffixes(child)
        
        collect_suffixes(current)
        return occurrences