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
        self.root = {}
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Build the suffix tree by adding all suffixes.
        """
        for i in range(len(self.text)):
            self._add_suffix(i)
    
    def _add_suffix(self, suffix_start):
        """
        Add a suffix to the tree.
        
        Args:
            suffix_start (int): Starting index of the suffix.
        """
        current = self.root
        suffix = self.text[suffix_start:]
        
        for j, char in enumerate(suffix):
            # If character doesn't exist, create new branch
            if char not in current:
                current[char] = {
                    'indices': [suffix_start],
                    'suffixes': {}
                }
                break
            
            # If character exists, update indices and traverse
            current[char]['indices'].append(suffix_start)
            current = current[char]['suffixes']
    
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
        
        # Special case for full text
        if pattern == self.text[:-1]:
            return [0]
        
        # Traverse the tree following the pattern
        current = self.root
        
        # Follow the pattern through the tree
        for char in pattern:
            # Skip when character not found
            if char not in current:
                return []
            
            # Get current node
            current = current[char]
        
        # Collect and return the indices
        return sorted(current.get('indices', []))