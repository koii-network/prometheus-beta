def sum_odd_even_numbers(numbers):
    """
    Calculate the sum of odd and even numbers in the given array.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        tuple: A tuple containing (sum of odd numbers, sum of even numbers)
    """
    # Validate input is a list or iterable
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Use list comprehensions to separate and sum odd and even numbers
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    return odd_sum, even_sum