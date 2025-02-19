class Queue:
    def __init__(self):
        """
        Initialize an empty queue using a list.
        """
        self._items = []
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item in the queue
        
        Raises:
            IndexError: If the queue is empty
        """
        if not self._items:
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: Number of items in the queue
        """
        return len(self._items)

def is_word_valid(word, rules):
    """
    Determine if a given word is valid based on a set of rules.
    
    Args:
        word (str): The word to validate
        rules (list): A list of validation rules to apply
    
    Returns:
        bool: True if the word is valid, False otherwise
    
    Rules:
    - Minimum length: Minimum number of characters
    - Maximum length: Maximum number of characters
    - Required characters: List of characters that must be in the word
    - Forbidden characters: List of characters that cannot be in the word
    - Case sensitivity: Whether uppercase/lowercase matters
    """
    # Validate input types
    if not isinstance(word, str) or not isinstance(rules, list):
        return False
    
    # Default rules if not specified
    min_length = rules.get('min_length', 1)
    max_length = rules.get('max_length', float('inf'))
    required_chars = rules.get('required_chars', [])
    forbidden_chars = rules.get('forbidden_chars', [])
    case_sensitive = rules.get('case_sensitive', True)
    
    # Handle case sensitivity
    if not case_sensitive:
        word = word.lower()
        required_chars = [c.lower() for c in required_chars]
        forbidden_chars = [c.lower() for c in forbidden_chars]
    
    # Length validation
    if len(word) < min_length or len(word) > max_length:
        return False
    
    # Required characters validation
    for char in required_chars:
        if char not in word:
            return False
    
    # Forbidden characters validation
    for char in forbidden_chars:
        if char in word:
            return False
    
    return True