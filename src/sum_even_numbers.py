def sum_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in the given array of integers.
    
    Args:
        numbers (list): An array of integers
    
    Returns:
        int: Sum of all even numbers in the array
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Sum only even numbers using list comprehension
    return sum(num for num in numbers if num % 2 == 0)