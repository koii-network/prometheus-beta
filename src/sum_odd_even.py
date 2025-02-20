def sum_odd_even(numbers):
    """
    Calculate the sum of odd and even numbers in the given array.
    
    Args:
        numbers (list): An array of integers
    
    Returns:
        tuple: A tuple containing (sum of odd numbers, sum of even numbers)
    """
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    return odd_sum, even_sum