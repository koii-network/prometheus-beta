class Queue:
    """
    A simple Queue implementation using a list.
    
    This Queue class provides basic queue operations like enqueue, dequeue,
    peek, and utility methods to check if the queue is empty or get its size.
    """
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self._items = []
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)
    
    def peek(self):
        """
        Return the first item in the queue without removing it.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty queue")
        return self._items[0]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: The number of items in the queue.
        """
        return len(self._items)

def is_word_valid(word, rules):
    """
    Determine if a given word is valid based on a set of rules.
    
    Args:
        word (str): The word to validate.
        rules (list): A list of validation rules to apply.
    
    Returns:
        bool: True if the word passes all rules, False otherwise.
    
    Raises:
        ValueError: If rules are improperly formatted.
    """
    if not isinstance(word, str):
        return False
    
    # If no rules are provided, consider the word valid
    if not rules:
        return True
    
    # Process each rule
    for rule in rules:
        # Check rule format
        if not isinstance(rule, str):
            raise ValueError(f"Invalid rule format: {rule}")
        
        # Minimum length rule
        if rule.startswith('min_length:'):
            try:
                min_len = int(rule.split(':')[1])
                if len(word) < min_len:
                    return False
            except (IndexError, ValueError):
                raise ValueError(f"Invalid min_length rule: {rule}")
        
        # Maximum length rule
        elif rule.startswith('max_length:'):
            try:
                max_len = int(rule.split(':')[1])
                if len(word) > max_len:
                    return False
            except (IndexError, ValueError):
                raise ValueError(f"Invalid max_length rule: {rule}")
        
        # Contains character rule
        elif rule.startswith('contains:'):
            char = rule.split(':')[1]
            if char not in word:
                return False
        
        # Starts with rule
        elif rule.startswith('starts_with:'):
            prefix = rule.split(':')[1]
            if not word.startswith(prefix):
                return False
        
        # Ends with rule
        elif rule.startswith('ends_with:'):
            suffix = rule.split(':')[1]
            if not word.endswith(suffix):
                return False
        
        # Unrecognized rule
        else:
            raise ValueError(f"Unrecognized rule: {rule}")
    
    # If all rules pass
    return True