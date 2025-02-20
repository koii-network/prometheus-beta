def sum_even_positive_numbers(numbers):
    """
    Calculate the sum of all even positive numbers in the given list.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: Sum of even positive numbers in the list
    """
    return sum(num for num in numbers if num > 0 and num % 2 == 0)