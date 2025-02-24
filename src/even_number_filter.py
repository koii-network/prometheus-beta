def filter_even_numbers(numbers):
    """
    Filter even numbers from a list of integers in linear time complexity.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A new list containing only the even numbers from the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Create a list to store even numbers
    even_numbers = []
    
    # Iterate through the list once (linear time complexity)
    for num in numbers:
        # Check if the number is an integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        
        # Check if the number is even
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers