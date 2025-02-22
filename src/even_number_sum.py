def sum_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in the given array.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The sum of all even numbers in the input list
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Sum only the even numbers using list comprehension
    return sum(num for num in numbers if num % 2 == 0)