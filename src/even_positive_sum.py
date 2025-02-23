def sum_even_positive_integers(numbers):
    """
    Calculate the sum of all even positive integers in a given list.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: Sum of even positive integers in the list
    """
    return sum(num for num in numbers if num > 0 and num % 2 == 0)