def filter_even_numbers(sorted_nums):
    """
    Filter even numbers from a sorted list of unique integers while maintaining original order.
    
    Args:
        sorted_nums (list): A sorted list of unique integers
    
    Returns:
        list: A new list containing only the even numbers from the input list
    
    Time complexity: O(n)
    """
    return [num for num in sorted_nums if num % 2 == 0]