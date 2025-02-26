def sum_odd_even_numbers(numbers):
    """
    Calculate the sum of odd and even numbers in the given array.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        tuple: A tuple containing two integers 
               (sum of odd numbers, sum of even numbers).

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate sum of odd and even numbers
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    return (odd_sum, even_sum)