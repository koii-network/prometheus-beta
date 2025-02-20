def filter_even_numbers(sorted_nums):
    """
    Filter even numbers from a sorted list of unique integers.
    
    Args:
        sorted_nums (list): A sorted list of unique integers
    
    Returns:
        list: A new list containing only the even numbers from the input list,
              maintaining the original order of the even numbers
    
    Time Complexity: O(n)
    """
    # Use list comprehension to filter even numbers 
    # This maintains O(n) time complexity as we iterate through the list once
    return [num for num in sorted_nums if num % 2 == 0]