def get_unique_even_numbers(numbers):
    """
    Returns a new list containing only the unique even numbers 
    in their original order of appearance.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A list of unique even numbers in their original order
    """
    # Use a set to track seen even numbers to maintain uniqueness
    seen_evens = set()
    
    # Use a list comprehension with a condition to keep track of unique even numbers
    return [num for num in numbers if num % 2 == 0 and not (num in seen_evens or seen_evens.add(num))]