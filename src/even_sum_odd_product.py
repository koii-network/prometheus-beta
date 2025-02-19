def calculate_even_sum_odd_product(numbers):
    """
    Calculate the sum of even numbers and the product of odd numbers in the input array.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        tuple: A tuple containing (sum of even numbers, product of odd numbers)
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Calculate sum of even numbers
    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    # Calculate product of odd numbers
    # Handle empty list of odd numbers by returning 1 (multiplicative identity)
    odd_product = 1
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    if odd_numbers:
        odd_product = 1
        for num in odd_numbers:
            odd_product *= num
    
    return even_sum, odd_product