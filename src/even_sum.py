def calculate_even_sum(numbers):
    """
    Calculate the sum of all even numbers in the given array of integers.
    
    Args:
        numbers (list): An array of integers
    
    Returns:
        int: Sum of all even numbers in the array
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-integer elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Calculate and return sum of even numbers
    return sum(num for num in numbers if num % 2 == 0)