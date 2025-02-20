def extract_even_numbers(sorted_list):
    """
    Extract even numbers from a sorted list of unique integers while maintaining their original order.
    
    Args:
        sorted_list (list): A sorted list of unique integers
    
    Returns:
        list: A new list containing only the even numbers from the input list
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Use a single pass through the list to extract even numbers
    return [num for num in sorted_list if num % 2 == 0]