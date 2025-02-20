def filter_even_numbers(numbers):
    """
    Filter even numbers from a list of integers in linear time complexity.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A new list containing only the even numbers from the input list
    """
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers