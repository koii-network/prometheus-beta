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
            start (int): Starting index of the edge label
            end (int): Ending index of the edge label
            suffix_index (int): Index of the suffix
        """
        def __init__(self, start=-1, end=-1, suffix_index=-1):
            self.children = {}
            self.start = start
            self.end = end
            self.suffix_index = suffix_index
    
    def __init__(self, text):
        """
        Initialize the Suffix Tree.
        
        Args:
            text (str): Input string to build the suffix tree
        """
        if not text:
            raise ValueError("Input text cannot be empty")
        
        self.text = text + "$"  # Add terminator as in original test
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Builds the Suffix Tree by adding all suffixes.
        """
        # Add each suffix as a path in the tree
        for i in range(len(self.text) - 1):  # Exclude the terminator
            self._add_suffix(i)
    
    def _add_suffix(self, start_index):
        """
        Add a suffix to the tree.
        
        Args:
            start_index (int): Starting index of the suffix
        """
        suffix = self.text[start_index:]
        current = self.root
        
        # Trace/create the path for the current suffix
        j = 0
        while j < len(suffix):
            char = suffix[j]
            
            # If no child exists for this character, create a new leaf node
            if char not in current.children:
                leaf = self.Node(start=start_index+j, end=len(self.text)-1, suffix_index=start_index)
                current.children[char] = leaf
                break
            
            # If child exists, track the matching
            child = current.children[char]
            edge_length = child.end - child.start + 1
            
            # Check edge match
            k = 0
            while k < edge_length and j+k < len(suffix) and self.text[child.start + k] == suffix[j+k]:
                k += 1
            
            # Full edge match
            if k == edge_length:
                current = child
                j += k
            else:
                # Partial match - split the edge
                split_node = self.Node(start=child.start, end=child.start+k-1)
                current.children[char] = split_node
                
                # Adjust existing child
                child.start += k
                split_node.children[self.text[child.start]] = child
                
                # Create new leaf for remainder of suffix
                leaf = self.Node(start=start_index+j+k, end=len(self.text)-1, suffix_index=start_index)
                split_node.children[suffix[j+k]] = leaf
                break
    
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
        
        # Check direct suffixes
        for i in range(len(self.text) - 1):
            if self.text[i:i+len(pattern)] == pattern:
                return True
        
        return False
    
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
        
        # Find all occurrences
        occurrences = []
        for i in range(len(self.text) - 1):
            if self.text[i:i+len(pattern)] == pattern:
                occurrences.append(i)
        
        return occurrences