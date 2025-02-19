class Queue:
    def __init__(self):
        """
        Initialize an empty queue using a list.
        """
        self._items = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        :param item: The item to be added to the queue
        """
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        :return: The first item in the queue
        :raises IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)

    def is_empty(self):
        """
        Check if the queue is empty.
        
        :return: True if the queue is empty, False otherwise
        """
        return len(self._items) == 0

    def size(self):
        """
        Get the number of items in the queue.
        
        :return: Number of items in the queue
        """
        return len(self._items)

def is_word_valid(word, rules):
    """
    Determine if a given word is valid based on a set of rules.
    
    :param word: The word to validate
    :param rules: A dictionary of validation rules
    :return: True if the word is valid, False otherwise
    """
    # Check if word meets minimum and maximum length requirements
    if 'min_length' in rules and len(word) < rules['min_length']:
        return False
    
    if 'max_length' in rules and len(word) > rules['max_length']:
        return False
    
    # Check for required characters
    if 'required_chars' in rules:
        for char in rules['required_chars']:
            if char not in word:
                return False
    
    # Check for forbidden characters
    if 'forbidden_chars' in rules:
        for char in rules['forbidden_chars']:
            if char in word:
                return False
    
    # Check for character case rules
    if 'case_sensitive' in rules:
        if rules['case_sensitive'] == 'upper' and not word.isupper():
            return False
        if rules['case_sensitive'] == 'lower' and not word.islower():
            return False
    
    # Check for specific pattern
    if 'pattern' in rules:
        import re
        if not re.match(rules['pattern'], word):
            return False
    
    return True