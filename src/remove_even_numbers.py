def remove_even_and_sum(numbers):
    """
    Remove even numbers from the input array and return their sum.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The sum of even numbers that were removed
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    numbers.clear()
    numbers.extend(odd_numbers)
    
    return sum(even_numbers)