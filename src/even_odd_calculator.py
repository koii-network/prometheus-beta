def calculate_even_sum_odd_product(numbers):
    """
    Calculate the sum of even numbers and the product of odd numbers in the input array.
    
    Args:
        numbers (list): A list of integers to process
    
    Returns:
        tuple: A tuple containing (sum of even numbers, product of odd numbers)
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Special case for empty list
    if not numbers:
        return 0, 1
    
    # Calculate sum of even numbers
    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    # Calculate product of odd numbers
    # Use product of 1 as the default for cases with no odd numbers
    odd_product = 1
    for num in numbers:
        if num % 2 != 0:
            odd_product *= num
    
    return even_sum, odd_product