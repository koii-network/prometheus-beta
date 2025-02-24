def process_array(numbers):
    """
    Process an array of numbers by:
    1. Multiplying every third number by 2
    2. Finding the sum of even numbers, excluding modified numbers

    Args:
        numbers (list): A list of numbers to process

    Returns:
        int: Sum of even numbers that were not modified

    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric elements
    if any(not isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numeric")
    
    # Create a copy of the original list to avoid modifying the input
    processed_numbers = numbers.copy()
    
    # Multiply every third number by 2
    for i in range(2, len(processed_numbers), 3):
        processed_numbers[i] *= 2
    
    # Sum even numbers, excluding modified numbers
    total = 0
    for i, num in enumerate(numbers):
        # Skip numbers that were modified (every third number)
        if i % 3 == 2:
            continue
        
        # Check if the original number is even
        if num % 2 == 0:
            total += num
    
    return total