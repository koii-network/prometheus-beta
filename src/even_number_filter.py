def filter_even_numbers(numbers):
    """
    Filter even numbers from a list of integers with O(n) time complexity.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A new list containing only the even numbers from the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Use a list to store even numbers with linear time complexity
    even_numbers = []
    
    # Iterate through the list once (O(n) time complexity)
    for num in numbers:
        # Validate each element is an integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        
        # Check if number is even using modulo operator
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers