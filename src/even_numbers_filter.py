def filter_even_numbers(sorted_list):
    """
    Filter even numbers from a sorted list of unique integers 
    while maintaining their original order.
    
    Args:
        sorted_list (list): A sorted list of unique integers
    
    Returns:
        list: A list containing only the even numbers from the input list
    
    Time Complexity: O(n)
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is not sorted or contains duplicates
    """
    # Type checking
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if sorted_list != sorted(sorted_list):
        raise ValueError("Input list must be sorted")
    
    # Check for duplicates
    if len(sorted_list) != len(set(sorted_list)):
        raise ValueError("Input list must contain unique integers")
    
    # Filter even numbers using list comprehension (O(n) time complexity)
    return [num for num in sorted_list if num % 2 == 0]