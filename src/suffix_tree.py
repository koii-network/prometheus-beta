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
        
        self.text = text
        self.suffixes = sorted(
            [self.text[i:] for i in range(len(self.text))]
        )
    
    def search(self, pattern):
        """
        Search for a pattern in the text.
        
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
        if pattern == self.text:
            return [0]
        
        # Find all occurrences
        indices = []
        for i in range(len(self.text)):
            if self.text[i:].startswith(pattern):
                indices.append(i)
        
        return indices