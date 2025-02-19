def process_numbers(numbers):
    """
    Process a list of numbers to calculate:
    1. Sum of even numbers
    2. Count of odd numbers

    Args:
        numbers (list): A list of integers

    Returns:
        tuple: A tuple containing (sum of even numbers, count of odd numbers)
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    # Use list comprehensions for efficient calculation
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    
    return even_sum, odd_count