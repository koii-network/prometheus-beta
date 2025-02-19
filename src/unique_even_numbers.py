def get_unique_even_numbers(numbers):
    """
    Takes a list of integers and returns a new list containing only the unique even numbers 
    in their original order of appearance.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A list of unique even numbers in their original order
    """
    # Use a set to track unique even numbers while preserving order
    unique_evens = []
    seen = set()
    
    for num in numbers:
        # Check if the number is even and not already seen
        if num % 2 == 0 and num not in seen:
            unique_evens.append(num)
            seen.add(num)
    
    return unique_evens