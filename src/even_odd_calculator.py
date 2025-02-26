def calculate_even_sum_odd_product(numbers):
    """
    Calculate the sum of even numbers and product of odd numbers in the input array.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        tuple: A tuple containing (sum of even numbers, product of odd numbers)
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate sum of even numbers
    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    # Calculate product of odd numbers
    # Use 1 as initial value to handle empty list of odd numbers
    odd_product = 1
    for num in numbers:
        if num % 2 != 0:
            odd_product *= num
    
    # If no odd numbers were found, return 1 as the product
    odd_product = odd_product if odd_product != 1 or any(num % 2 != 0 for num in numbers) else 0
    
    return even_sum, odd_product