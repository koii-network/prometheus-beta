def sum_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in the given array of integers.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: The sum of all even numbers in the input list.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate and return sum of even numbers
    return sum(num for num in numbers if num % 2 == 0)