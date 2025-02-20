def remove_even_numbers(numbers):
    """
    Remove even numbers from an input array and return their sum.
    
    Args:
        numbers (list): Input list of integers
    
    Returns:
        tuple: A tuple containing:
            - A list of odd numbers from the original list
            - The sum of removed even numbers
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    even_sum = 0
    odd_numbers = []
    
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        
        if num % 2 == 0:
            even_sum += num
        else:
            odd_numbers.append(num)
    
    return odd_numbers, even_sum