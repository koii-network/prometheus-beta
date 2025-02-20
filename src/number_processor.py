def process_number_array(numbers):
    """
    Process an array of numbers:
    1. Multiply every third number by 2
    2. Find the sum of all even numbers, excluding the modified numbers
    
    Args:
        numbers (list): A list of numbers to process
    
    Returns:
        int: Sum of even numbers not modified by multiplication
    """
    # Create a copy of the input list to avoid modifying the original
    processed_numbers = numbers.copy()
    
    # Multiply every third number by 2
    for i in range(2, len(processed_numbers), 3):
        processed_numbers[i] *= 2
    
    # Sum even numbers, excluding the modified numbers
    even_sum = sum(num for i, num in enumerate(numbers) 
                   if num % 2 == 0 and i % 3 != 2)
    
    return even_sum