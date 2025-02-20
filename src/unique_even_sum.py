def sum_unique_even_numbers(numbers):
    """
    Calculate the sum of unique even numbers in the input array.
    
    Args:
        numbers (list): An array of integers
    
    Returns:
        int: Sum of even numbers that appear only once in the array
    """
    # Count occurrences of each number
    number_counts = {}
    for num in numbers:
        number_counts[num] = number_counts.get(num, 0) + 1
    
    # Sum unique even numbers
    unique_even_sum = sum(num for num in numbers 
                           if num % 2 == 0 and number_counts[num] == 1)
    
    return unique_even_sum