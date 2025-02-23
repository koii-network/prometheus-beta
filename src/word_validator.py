class Queue:
    """
    A simple Queue implementation using a list.
    
    This Queue provides basic queue operations like enqueue, dequeue, 
    and checking if the queue is empty.
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
        rules (list): A list of rule functions that return True or False.
    
    Returns:
        bool: True if the word passes all rules, False otherwise.
    """
    # Validate input types
    if not isinstance(word, str):
        raise TypeError("Word must be a string")
    
    if not isinstance(rules, list):
        raise TypeError("Rules must be a list of functions")
    
    # If no rules are provided, consider the word valid
    if not rules:
        return True
    
    # Check each rule
    for rule in rules:
        if not callable(rule):
            raise TypeError("Each rule must be a callable function")
        
        if not rule(word):
            return False
    
    return True