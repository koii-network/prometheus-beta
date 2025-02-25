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
        
        def edge_length(self):
            """
            Calculate the length of the edge label.
            
            Returns:
                int: Length of the edge label
            """
            return self.end - self.start + 1
    
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
        Construct the Suffix Tree using explicit extension algorithm.
        
        Implements O(m^2) construction with simpler implementation.
        """
        for i in range(len(self.text)):
            self._insert_suffix(i)
    
    def _insert_suffix(self, start_index):
        """
        Insert a suffix into the tree.
        
        Args:
            start_index (int): Starting index of the suffix to insert
        """
        current = self.root
        j = start_index
        
        while j < len(self.text):
            current_char = self.text[j]
            
            # If no child with current character, create leaf
            if current_char not in current.children:
                new_leaf = self.Node(start=j, end=len(self.text)-1)
                current.children[current_char] = new_leaf
                break
            
            # Follow the edge that starts with current character
            child = current.children[current_char]
            edge_length = child.edge_length()
            edge_start = child.start
            
            # Compare characters along the edge
            k = 0
            while k < edge_length and j + k < len(self.text) and self.text[edge_start + k] == self.text[j + k]:
                k += 1
            
            # If we've fully matched the edge
            if k == edge_length:
                current = child
                j += k
            else:
                # Split the edge
                split_node = self.Node(start=edge_start, end=edge_start + k - 1)
                current.children[current_char] = split_node
                
                # Update original child
                child.start = edge_start + k
                split_node.children[self.text[child.start]] = child
                
                # Create new leaf
                new_leaf = self.Node(start=j + k, end=len(self.text)-1)
                split_node.children[self.text[j + k]] = new_leaf
                break
    
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
        i = 0
        
        while i < len(pattern):
            # Find the child corresponding to the current character
            if pattern[i] not in current.children:
                return []  # Pattern not found
            
            # Follow the appropriate edge
            child = current.children[pattern[i]]
            edge_start = child.start
            edge_end = child.end
            edge_index = edge_start
            
            # Compare characters along the edge
            while edge_index <= edge_end and i < len(pattern):
                if self.text[edge_index] != pattern[i]:
                    return []  # Pattern does not match
                
                edge_index += 1
                i += 1
            
            # If we fully traversed the pattern
            if i == len(pattern):
                return self._collect_leaf_indices(child)
            
            # Move to the next node
            current = child
        
        return []
    
    def _collect_leaf_indices(self, node):
        """
        Collect all leaf indices under a given node.
        
        Args:
            node (Node): Starting node to collect indices from
        
        Returns:
            list: List of starting indices of suffixes
        """
        indices = []
        
        # If it's a leaf, return its index (original text index)
        if not node.children:
            return [node.start]
        
        # Recursively collect indices from children
        for child in node.children.values():
            indices.extend(self._collect_leaf_indices(child))
        
        return sorted(set(index for index in indices if index < len(self.text) - 1))