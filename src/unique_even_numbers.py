def get_unique_even_numbers(numbers):
    """
    Returns a new list containing only the unique even numbers 
    in their original order of appearance.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A list of unique even numbers in their original order
    """
    # Use a set to track seen unique even numbers while preserving order
    seen_evens = set()
    result = []
    
    for num in numbers:
        # Check if the number is even and not previously seen
        if num % 2 == 0 and num not in seen_evens:
            seen_evens.add(num)
            result.append(num)
    
    return result