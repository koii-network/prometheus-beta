def filter_even_numbers(sorted_list):
    """
    Filter even numbers from a sorted list of unique integers while maintaining their original order.
    
    Args:
        sorted_list (list): A sorted list of unique integers.
    
    Returns:
        list: A new list containing only the even numbers from the input list.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is not sorted or contains duplicates.
    """
    # Check input type
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Check for duplicates first
    if len(sorted_list) != len(set(sorted_list)):
        raise ValueError("Input list must contain unique elements")
    
    # Check if list is sorted 
    if len(sorted_list) > 1 and any(sorted_list[i] >= sorted_list[i+1] for i in range(len(sorted_list)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Filter even numbers in O(n) time complexity
    return [num for num in sorted_list if num % 2 == 0]