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
        if not self._items:
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)

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
            int: Number of items in the queue.
        """
        return len(self._items)

def is_word_valid(word, rules):
    """
    Determine if a given word is valid based on a set of rules.
    
    Args:
        word (str): The word to validate.
        rules (list): A list of validation rules to apply.
    
    Returns:
        bool: True if the word is valid according to all rules, False otherwise.
    """
    # Validate input types
    if not isinstance(word, str) or not isinstance(rules, list):
        return False
    
    # Empty word is invalid
    if not word:
        return False
    
    # Apply each rule to the word
    for rule in rules:
        # Minimum length rule
        if rule.startswith('min_length:'):
            min_length = int(rule.split(':')[1])
            if len(word) < min_length:
                return False
        
        # Maximum length rule
        elif rule.startswith('max_length:'):
            max_length = int(rule.split(':')[1])
            if len(word) > max_length:
                return False
        
        # Contains letter rule
        elif rule.startswith('contains:'):
            letter = rule.split(':')[1]
            if letter not in word:
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
        
        # Lowercase rule
        elif rule == 'lowercase':
            if not word.islower():
                return False
        
        # Uppercase rule
        elif rule == 'uppercase':
            if not word.isupper():
                return False
    
    # If all rules pass, the word is valid
    return True