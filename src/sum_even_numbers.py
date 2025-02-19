def sum_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in the given array of integers.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: Sum of all even numbers in the input list
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate and return the sum of even numbers
    return sum(num for num in numbers if num % 2 == 0)