def count_pairs_with_difference_of_five(numbers):
    """
    Count the number of adjacent pairs in the list with a difference of exactly 5.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: Number of adjacent pairs with a difference of 5
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-integer elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Count pairs with difference of 5
    count = 0
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) == 5:
            count += 1
    
    return count