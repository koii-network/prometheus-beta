class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search and pattern matching 
    with a time complexity of O(m) for search, where m is the length of the pattern.
    """
    
    def __init__(self, text):
        """
        Initialize the Suffix Tree with the given text.
        
        Args:
            text (str): The input text to build the suffix tree from.
        
        Raises:
            ValueError: If the input text is not a non-empty string.
        """
        if not isinstance(text, str) or not text:
            raise ValueError("Input must be a non-empty string")
        
        self.text = text + '$'  # Append termination symbol
        self.root = self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Build the suffix tree using Ukkonen's algorithm.
        
        Returns:
            dict: The root node of the suffix tree.
        """
        root = {}
        for i in range(len(self.text)):
            self._add_suffix(root, i)
        return root
    
    def _add_suffix(self, node, suffix_start):
        """
        Add a suffix to the tree.
        
        Args:
            node (dict): Current node in the tree.
            suffix_start (int): Starting index of the suffix.
        """
        current = node
        for i in range(suffix_start, len(self.text)):
            current_char = self.text[i]
            
            # If the character doesn't exist, create a new edge
            if current_char not in current:
                current[current_char] = {
                    'end': len(self.text),
                    'start': i
                }
                break
            
            # Traverse or split the existing edge
            edge = current[current_char]
            edge_length = edge['end'] - edge['start']
            
            # Check characters along the edge
            match_length = 0
            for j in range(edge['start'], edge['end']):
                if i + match_length >= len(self.text) or \
                   self.text[i + match_length] != self.text[j]:
                    break
                match_length += 1
            
            # If we need to split the edge
            if match_length < edge_length:
                split_node = {
                    self.text[j]: {
                        'end': edge['end'],
                        'start': j
                    }
                }
                edge['end'] = edge['start'] + match_length
                current[current_char] = split_node
                current = split_node
            
            # Move to the next character
            i += match_length
            if i >= len(self.text):
                break
    
    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): The pattern to search for.
        
        Returns:
            list: Indices where the pattern is found in the text.
        
        Raises:
            ValueError: If the pattern is not a non-empty string.
        """
        if not isinstance(pattern, str) or not pattern:
            raise ValueError("Pattern must be a non-empty string")
        
        # Find the node corresponding to the pattern
        current = self.root
        for char in pattern:
            if char not in current:
                return []  # Pattern not found
            current = current[char]
        
        # Collect all indices where the pattern occurs
        return self._collect_indices(current)
    
    def _collect_indices(self, node):
        """
        Collect all indices where a substring occurs.
        
        Args:
            node (dict): The node to start collecting indices from.
        
        Returns:
            list: Indices of substring occurrences.
        """
        indices = []
        stack = [node]
        
        while stack:
            current = stack.pop()
            
            # If the node represents a leaf (suffix)
            if isinstance(current, dict) and 'start' in current:
                indices.append(current['start'])
            
            # Explore child nodes
            for child in current.values():
                if isinstance(child, dict):
                    stack.append(child)
        
        return sorted(indices)