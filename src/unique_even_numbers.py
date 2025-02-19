def get_unique_even_numbers(numbers):
    """
    Returns a new list containing only the unique even numbers 
    in their original order of appearance.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A list of unique even numbers, preserving original order
    """
    seen = set()
    unique_evens = []
    for num in numbers:
        # Check if number is even and not already seen
        if num % 2 == 0 and num not in seen:
            unique_evens.append(num)
            seen.add(num)
    return unique_evens