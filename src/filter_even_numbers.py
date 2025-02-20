def filter_even_numbers(sorted_list):
    """
    Filter even numbers from a sorted list of unique integers while maintaining their original order.
    
    Args:
        sorted_list (list): A sorted list of unique integers
    
    Returns:
        list: A new list containing only the even numbers from the input list
    
    Time Complexity: O(n)
    """
    # Check for invalid input
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Use list comprehension for O(n) time complexity
    return [num for num in sorted_list if num % 2 == 0]