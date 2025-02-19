def double_even_numbers(numbers):
    """
    Takes an array of numbers and returns a new array with even numbers multiplied by 2.
    
    Args:
        numbers (list): Input list of numbers
    
    Returns:
        list: A new list with even numbers doubled, odd numbers unchanged
    """
    return [num * 2 if num % 2 == 0 else num for num in numbers]